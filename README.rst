Django GraphQL Social
=====================

|Pypi| |Wheel| |Build Status| |Codecov| |Code Climate|

`Python Social Auth`_ support for `Django GraphQL`_


.. _Python Social Auth: http://python-social-auth.readthedocs.io/
.. _Django GraphQL: https://github.com/graphql-python/graphene-django


Dependencies
------------

* Python ≥ 3.4
* Django ≥ 1.11


Installation
------------

Install last stable version from Pypi.

.. code:: sh

    pip install django-graphql-social


See the `documentation`_ for further guidance on setting *Python Social Auth*.

.. _documentation: http://python-social-auth.readthedocs.io/en/latest/configuration/django.html


Add the ``SocialAuth`` mutation to your GraphQL schema.

.. code:: python

    import graphene
    import graphql_social


    class Mutations(graphene.ObjectType):
        social_auth = graphql_social.SocialAuth.Field()


Query

.. code:: graphql

    mutation SocialAuth($provider: String!, $accessToken: String!) {
      socialAuth(provider: $provider, accessToken: $accessToken) {
        social {
          uid
          extraData
        }
      }
    }


JWT (JSON Web Token)
--------------------

Install additional requirements.

.. code:: sh

    pip install 'django-graphql-social[jwt]'


Add the ``SocialAuthJWT`` mutation to your GraphQL schema.

.. code:: python

    import graphene
    import graphql_social


    class Mutations(graphene.ObjectType):
        social_auth = graphql_social.SocialAuthJWT.Field()


Query

.. code:: graphql

    mutation SocialAuth($provider: String!, $accessToken: String!) {
      socialAuth(provider: $provider, accessToken: $accessToken) {
        social {
          uid
        }
        token
      }
    }


Relay
-----

Complete support for `Relay`_.

.. _Relay: https://facebook.github.io/relay/

.. code:: python

    import graphene
    import graphql_social


    class Mutations(graphene.ObjectType):
        social_auth = graphql_social.relay.SocialAuth.Field()


``graphql_social.relay.SocialAuthJWT`` for `JSON Web Token`_.

.. _JSON Web Token: https://jwt.io/


Custom
------

Your mutation must be a subclass of ``SocialAuth`` or ``SocialAuthJWT``.

.. code:: python

    import graphene
    import graphql_social


    class SocialAuth(graphql_social.SocialAuth):
        user = graphene.Field(UserType)

        @classmethod
        def do_auth(cls, info, social, **args):
            return cls(social=social, user=social.user)


.. |Pypi| image:: https://img.shields.io/pypi/v/django-graphql-social.svg
   :target: https://pypi.python.org/pypi/django-graphql-social

.. |Wheel| image:: https://img.shields.io/pypi/wheel/django-graphql-social.svg
   :target: https://pypi.python.org/pypi/django-graphql-social

.. |Build Status| image:: https://travis-ci.org/flavors/django-graphql-social.svg?branch=master
   :target: https://travis-ci.org/flavors/django-graphql-social

.. |Codecov| image:: https://img.shields.io/codecov/c/github/flavors/django-graphql-social.svg
   :target: https://codecov.io/gh/flavors/django-graphql-social

.. |Code Climate| image:: https://api.codeclimate.com/v1/badges/6f8b21f374ecb7918991/maintainability
   :target: https://codeclimate.com/github/flavors/django-graphql-social
