import graphene

from . import nodes
from .. import mixins, mutations
from ..decorators import social_auth


class SocialAuthMutation(mixins.SocialAuthMixin,
                         graphene.relay.ClientIDMutation):

    social = graphene.Field(nodes.SocialNode)

    class Meta:
        abstract = True

    class Input(mutations.SocialAuthMutation.Arguments):
        """Social Auth Input"""

    @classmethod
    @social_auth
    def mutate_and_get_payload(cls, root, info, social, **kwargs):
        return cls.resolve(root, info, social, **kwargs)


class SocialAuth(mixins.ResolveMixin, SocialAuthMutation):
    """Social Auth Mutation for Relay"""


class SocialAuthJWT(mixins.JSONWebTokenMixin, SocialAuthMutation):
    """Social Auth for JSON Web Token (JWT)"""
