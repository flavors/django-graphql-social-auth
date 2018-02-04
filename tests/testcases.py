from django.test import Client, RequestFactory, testcases

import graphene
from graphene.types.generic import GenericScalar


class GraphQLRequestFactory(RequestFactory):

    def execute(self, query, **variables):
        return self._schema.execute(query, variable_values=variables)


class GraphQLClient(GraphQLRequestFactory, Client):

    def __init__(self, **defaults):
        super().__init__(**defaults)
        self._schema = None

    def schema(self, **kwargs):
        self._schema = graphene.Schema(**kwargs)


class GraphQLSocialAuthTestCase(testcases.TestCase):

    class Query(graphene.ObjectType):
        test = GenericScalar()

    Mutations = None
    client_class = GraphQLClient

    def setUp(self):
        self.client.schema(query=self.Query, mutation=self.Mutations)
