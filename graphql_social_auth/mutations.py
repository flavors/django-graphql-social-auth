import graphene

from . import mixins, types
from .decorators import social_auth


class SocialAuthMutation(mixins.SocialAuthMixin, graphene.Mutation):
    social = graphene.Field(types.SocialType)

    class Meta:
        abstract = True

    class Arguments:
        provider = graphene.String(required=True)
        access_token = graphene.String(required=True)

    @classmethod
    @social_auth
    def mutate(cls, root, info, social, **kwargs):
        return cls.do_auth(info, social, **kwargs)


class SocialAuth(mixins.DoAuthMixin, SocialAuthMutation):
    """Social Auth Mutation"""


class SocialAuthJWT(mixins.DoAuthJWTMixin, SocialAuthMutation):
    """Social Auth for JWT (JSON Web Token)"""
