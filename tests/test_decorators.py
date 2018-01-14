from unittest.mock import MagicMock

from django.test import TestCase

from graphql_social import decorators, exceptions


class DecoratorsTests(TestCase):

    def test_missing_backend(self):

        @decorators.social_auth
        def wrapped(self, root, info, provider, *args, **kwargs):
            """Social auth decorated function"""

        with self.assertRaises(exceptions.GraphQLSocialError):
            mock = MagicMock()
            wrapped(self, mock, mock, 'unknown', '-token-')
