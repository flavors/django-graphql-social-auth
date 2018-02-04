import graphene


class SocialAuthMixin(object):

    @classmethod
    def __init_subclass_with_meta__(cls, name=None, **options):
        assert getattr(cls, 'do_auth', None), (
            '{name}.do_auth method is required in a SocialAuthMutation.'
        ).format(name=name or cls.__name__)

        super().__init_subclass_with_meta__(name=name, **options)


class DoAuthMixin(object):

    @classmethod
    def do_auth(cls, *args, **kwargs):
        return cls()


class DoAuthJWTMixin(object):
    token = graphene.String()

    @classmethod
    def do_auth(cls, info, social, **kwargs):
        try:
            from graphql_jwt.shortcuts import get_token
        except ImportError:
            raise ImportError(
                'django-graphql-jwt not installed.\n'
                'Use `pip install \'django-graphql-social[jwt]\'`.'
            )
        return cls(token=get_token(social.user))
