from graphene import relay
from social_django import models as social_models

from .. import types


class SocialNode(types.SocialType):

    class Meta:
        model = social_models.UserSocialAuth
        interfaces = [relay.Node]
        filter_fields = {
            'uid': ['exact', 'in'],
            'provider': ['exact', 'in'],
        }
