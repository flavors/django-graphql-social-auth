from unittest.mock import MagicMock, PropertyMock

from django.test import TestCase

from graphql_social import pipelines


class PioelinesTests(TestCase):

    def test_associate_signed_user(self):
        strategy_mock = MagicMock()
        type(strategy_mock.request.user).is_authenticated =\
            PropertyMock(return_value=True)

        pipeline = pipelines.associate_signed_user(strategy_mock)
        self.assertIn('user', pipeline)

    def test_associate_anonymous_user(self):
        strategy_mock = MagicMock()
        type(strategy_mock.request.user).is_authenticated =\
            PropertyMock(return_value=False)

        pipeline = pipelines.associate_signed_user(strategy_mock)
        self.assertIsNone(pipeline)
