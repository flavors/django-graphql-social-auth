import graphene

from . import mixins, types
from .decorators import social_auth


class SocialAuth(mixins.DoAuthMixin, graphene.Mutation):
    social = graphene.Field(types.SocialType)

    class Arguments:
        provider = graphene.String(required=True)
        access_token = graphene.String(required=True)

    @classmethod
    @social_auth
    def mutate(cls, root, *args, **kwargs):
        return cls.do_auth(*args, **kwargs)


class SocialAuthJWT(mixins.SocialAuthJWTMixin, SocialAuth):
    """Social Auth for JWT (JSON Web Token)"""
