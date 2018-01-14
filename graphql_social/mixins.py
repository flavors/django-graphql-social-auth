import graphene


class DoAuthMixin(object):

    @classmethod
    def do_auth(cls, info, social, **kwargs):
        return cls(social=social)


class SocialAuthJWTMixin(object):
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
        return cls(social=social, token=get_token(social.user))
