from django.test import Client, RequestFactory, testcases

import graphene


class SchemaRequestFactory(RequestFactory):

    def execute(self, query, **variables):
        return self._schema.execute(query, variables=variables)


class SchemaClient(SchemaRequestFactory, Client):

    def __init__(self, **defaults):
        super().__init__(**defaults)
        self._schema = None

    def schema(self, **kwargs):
        self._schema = graphene.Schema(**kwargs)


class SchemaTestCase(testcases.TestCase):
    Mutations = None
    client_class = SchemaClient

    def setUp(self):
        self.client.schema(mutation=self.Mutations)
