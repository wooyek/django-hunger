Django Hunger2
==============

.. image:: https://secure.travis-ci.org/wooyek/django-hunger2.png?branch=master
   :target: http://travis-ci.org/wooyek/django-hunger2

Django-hunger provides a flexible private beta phase for Django
projects.

This is a fork for unsupported http://github.com/joshuakarjala/django-hunger app.

Features and Design Decisions
-----------------------------

- Three ways to get into the beta.

   #. Users self-signup for the beta. An admin can choose to invite
      them at any time.
   #. An admin can grant in-beta users with a limited number of
      invites to invite their friends.
   #. An admin can create a limited number public beta code that
      anybody can use to join the beta. Useful for
      press releases.

- Hunger is a post-registration app, meaning the intended behavior
  is to let users sign up freely, but restrict the rest of the site to
  beta participants. This makes it easy to integrate with social login
  and user management apps.

- Email as the method of choice for communication. Emails are used to
  send people their invites.

- Flexible design with many entry points for customization of default
  behavior.

- TODO: Tracking and user analytics for the beta phase. Want to know
  which users are the most excited about your site? Find out by
  analyzing the invite graph.


Documentation
-------------

Check out the full documentation at http://django-hunger.readthedocs.org/.
