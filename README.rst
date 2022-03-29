=====
DjangoForB2R
=====

DjangoForB2R is a Django app to conduct web-based DjangoForB2R. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "DjangoForB2R" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'DjangoForB2R',
    ]

2. Include the DjangoForB2R URLconf in your project urls.py like this::

    path('DjangoForB2R/', include('DjangoForB2R.urls')),

3. Run ``python manage.py migrate`` to create the DjangoForB2R models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/DjangoForB2R/ to participate in the poll.