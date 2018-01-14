import graphene

from . import nodes
from .. import mixins, mutations
from ..decorators import social_auth


class SocialAuth(mixins.DoAuthMixin, graphene.relay.ClientIDMutation):
    social = graphene.Field(nodes.SocialNode)

    class Input(mutations.SocialAuth.Arguments):
        """Relay Input"""

    @classmethod
    @social_auth
    def mutate_and_get_payload(cls, root, *args, **kwargs):
        return cls.do_auth(*args, **kwargs)


class SocialAuthJWT(mixins.SocialAuthJWTMixin, SocialAuth):
    """Social Auth for JWT (JSON Web Token)"""

    class Input(mutations.SocialAuth.Arguments):
        """Relay Input cannot be inherited"""
