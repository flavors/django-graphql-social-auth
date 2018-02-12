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
        return cls.resolve(root, info, social, **kwargs)


class SocialAuth(mixins.ResolveMixin, SocialAuthMutation):
    """Social Auth Mutation"""


class SocialAuthJWT(mixins.JSONWebTokenMixin, SocialAuthMutation):
    """Social Auth for JSON Web Token (JWT)"""
