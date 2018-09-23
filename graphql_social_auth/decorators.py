from functools import wraps

from django.contrib.auth import login
from django.utils.translation import ugettext_lazy as _

from promise import Promise, is_thenable
from social_core.exceptions import MissingBackend
from social_django.utils import load_backend, load_strategy

from . import exceptions, mixins


def psa(f):
    @wraps(f)
    def wrapper(cls, root, info, provider, access_token, **kwargs):
        strategy = load_strategy(info.context)
        try:
            backend = load_backend(strategy, provider, redirect_uri=None)
        except MissingBackend:
            raise exceptions.GraphQLSocialAuthError(_('Provider not found'))

        user = backend.do_auth(access_token)

        if user is None:
            raise exceptions.InvalidTokenError(_('Invalid token'))

        user_model = strategy.storage.user.user_model()

        if not isinstance(user, user_model):
            msg = _('`{}` is not a user instance').format(type(user).__name__)
            raise exceptions.DoAuthError(msg, user)

        if not issubclass(cls, mixins.JSONWebTokenMixin):
            login(info.context, user)

        social = user.social_auth.get(provider=provider)

        return f(cls, root, info, social, **kwargs)
    return wrapper


def social_auth(f):
    @psa
    @wraps(f)
    def wrapper(cls, root, info, social, **kwargs):
        def on_resolve(payload):
            payload.social = social
            return payload

        result = f(cls, root, info, social, **kwargs)

        if is_thenable(result):
            return Promise.resolve(result).then(on_resolve)
        return on_resolve(result)
    return wrapper
