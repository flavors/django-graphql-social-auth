Django GraphQL Social Auth
==========================

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
    import graphql_social_auth


    class Mutations(graphene.ObjectType):
        social_auth = graphql_social_auth.SocialAuth.Field()

Authenticate via *access_token*.


.. code:: graphql

    mutation SocialAuth($provider: String!, $accessToken: String!) {
      socialAuth(provider: $provider, accessToken: $accessToken) {
        social {
          uid
          extraData
        }
      }
    }


JSON Web Token (JWT)
--------------------

Authentication solution based on `JSON Web Token`_.

Install additional requirements.

.. code:: sh

    pip install 'django-graphql-social-auth[jwt]'


Add the ``SocialAuthJWT`` mutation to your GraphQL schema.

.. code:: python

    import graphene
    import graphql_social_auth


    class Mutations(graphene.ObjectType):
        social_auth = graphql_social_auth.SocialAuthJWT.Field()


Authenticate via *access_token* to obtain a JSON Web Token.

.. code:: graphql

    mutation SocialAuth($provider: String!, $accessToken: String!) {
      socialAuth(provider: $provider, accessToken: $accessToken) {
        social {
          uid
        }
        token
      }
    }

.. _JSON Web Token: https://jwt.io/


Relay
-----

Complete support for `Relay`_.

.. _Relay: https://facebook.github.io/relay/

.. code:: python

    import graphene
    import graphql_social_auth


    class Mutations(graphene.ObjectType):
        social_auth = graphql_social_auth.relay.SocialAuth.Field()


``graphql_social_auth.relay.SocialAuthJWT`` for `JSON Web Token (JWT)`_ authentication.


Customizing
-----------

Some kinds of projects may have authentication requirements for which ``SocialAuth`` mutation is not always appropriate.

You can override the default *payload* by providing a subclass of ``SocialAuth`` or ``SocialAuthJWT``.

.. code:: python

    import graphene
    import graphql_social_auth


    class SocialAuth(graphql_social_auth.SocialAuth):
        user = graphene.Field(UserType)

        @classmethod
        def do_auth(cls, info, social, **kwargs):
            return cls(social=social, user=social.user)


----

Gracias `Matías`_.

.. _Matías: https://github.com/omab


.. |Pypi| image:: https://img.shields.io/pypi/v/django-graphql-social-auth.svg
   :target: https://pypi.python.org/pypi/django-graphql-social

.. |Wheel| image:: https://img.shields.io/pypi/wheel/django-graphql-social-auth.svg
   :target: https://pypi.python.org/pypi/django-graphql-social

.. |Build Status| image:: https://travis-ci.org/flavors/django-graphql-social-auth.svg?branch=master
   :target: https://travis-ci.org/flavors/django-graphql-social

.. |Codecov| image:: https://img.shields.io/codecov/c/github/flavors/django-graphql-social-auth.svg
   :target: https://codecov.io/gh/flavors/django-graphql-social

.. |Code Climate| image:: https://api.codeclimate.com/v1/badges/6f8b21f374ecb7918991/maintainability
   :target: https://codeclimate.com/github/flavors/django-graphql-social
