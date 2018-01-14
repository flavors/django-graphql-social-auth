import graphene

import graphql_social

from . import mixins
from .testcases import GraphQLSocialTestCase


class SocialAuthTests(mixins.SocialAuthTestsMixin, GraphQLSocialTestCase):

    class Mutations(graphene.ObjectType):
        social_auth = graphql_social.relay.SocialAuth.Field()

    def execute(self, input):
        query = '''
        mutation SocialAuth($input: SocialAuthInput!) {
          socialAuth(input: $input) {
            social {
              uid
              extraData
            }
            clientMutationId
          }
        }'''

        return self.client.execute(query, input=input)


class SocialAuthJWTTests(mixins.SocialAuthTestsMixin,
                         mixins.SocialAuthJWTTestsMixin,
                         GraphQLSocialTestCase):

    class Mutations(graphene.ObjectType):
        social_auth = graphql_social.relay.SocialAuthJWT.Field()

    def execute(self, input):
        query = '''
        mutation SocialAuth($input: SocialAuthJWTInput!) {
          socialAuth(input: $input) {
            social {
              uid
              extraData
            }
            token
            clientMutationId
          }
        }'''

        return self.client.execute(query, input=input)
