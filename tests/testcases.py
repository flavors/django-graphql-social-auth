from unittest.mock import MagicMock, Mock

from django.contrib.auth.models import AnonymousUser
from django.core.handlers.wsgi import WSGIRequest
from django.test import Client, RequestFactory, testcases

import graphene
from graphene_django.settings import graphene_settings
from graphql.execution.base import ResolveInfo


class SchemaRequestFactory(RequestFactory):

    def __init__(self, **defaults):
        super().__init__(**defaults)
        self._schema = graphene_settings.SCHEMA

    def schema(self, **kwargs):
        self._schema = graphene.Schema(**kwargs)

    def execute(self, query, **options):
        return self._schema.execute(query, **options)


class RequestClient(Client):

    def request(self, **request):
        request = WSGIRequest(self._base_environ(**request))
        request.user = AnonymousUser()
        request.session = MagicMock()
        return request


class SchemaClient(SchemaRequestFactory, RequestClient):

    def schema(self, **kwargs):
        self._schema = graphene.Schema(**kwargs)

    def execute(self, query, variables=None, **extra):
        context = self.post('/', **extra)
        return super().execute(query, context=context, variables=variables)


class TestCase(testcases.TestCase):
    client_class = RequestClient

    def info(self, user=None, **extra):
        context = self.client.post('/', **extra)

        if user is not None:
            context.user = user

        return Mock(context=context, spec=ResolveInfo)


class SchemaTestCase(testcases.TestCase):
    Mutations = None
    client_class = SchemaClient

    def setUp(self):
        self.client.schema(mutation=self.Mutations)

    def execute(self, variables=None):
        assert self.query, ('`query` property not specified')
        return self.client.execute(self.query, variables)


class RelaySchemaTestCase(SchemaTestCase):

    def execute(self, variables=None):
        return super().execute({'input': variables})
