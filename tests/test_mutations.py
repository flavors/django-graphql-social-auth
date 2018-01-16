import graphene

import graphql_social_auth

from . import mixins
from .testcases import GraphQLSocialTestCase


class MutationsTests(mixins.SocialAuthTestsMixin, GraphQLSocialTestCase):

    class Mutations(graphene.ObjectType):
        social_auth = graphql_social_auth.SocialAuth.Field()

    def execute(self, variables):
        query = '''
        mutation SocialAuth($provider: String!, $accessToken: String!) {
          socialAuth(provider: $provider, accessToken: $accessToken) {
            social {
              uid
              extraData
            }
          }
        }'''

        return self.client.execute(query, **variables)


class SocialAuthJWTTests(mixins.SocialAuthTestsMixin,
                         mixins.SocialAuthJWTTestsMixin,
                         GraphQLSocialTestCase):

    class Mutations(graphene.ObjectType):
        social_auth = graphql_social_auth.SocialAuthJWT.Field()

    def execute(self, variables):
        query = '''
        mutation SocialAuth($provider: String!, $accessToken: String!) {
          socialAuth(provider: $provider, accessToken: $accessToken) {
            social {
              uid
              extraData
            }
            token
          }
        }'''

        return self.client.execute(query, **variables)
