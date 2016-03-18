=====
Usage
=====

To use Django URL Bits in a project:

.. code-block:: python

    from django.conf.urls import url
    from django_url_bits import path as _

    from . import views

    urlpatterns = (
        url(
            _("gondor/{uuid:age}/"),
            views.GondorView.as_view(),
            name='gondor',
        ),
        url(
            _("mordor/{int:orcs}/"),
            views.MordorView.as_view(),
            name='mordor',
        ),
        url(
            _("shire/:house/"),
            views.ShireView.as_view(),
            name='shire',
        ),
    )

Ultimately, all ``django_url_bits.path`` does is take a string, and return a
regexier string.

So, of course, you can mix-and-match if you need:

..code-block:: python

    from django.conf.urls import url
    from django_url_bits import path as _

    from . import views

    urlpatterns = (
        url(
            _("gondor/{age:uuid}/"),  # Because who wants to write the regex for a UUID?
            views.GondorView.as_view(),
            name='gondor',
        ),
        url(
            r"mordor/(?P<orcs>\d+)/",
            views.MordorView.as_view(),
            name='mordor',
        ),
        url(
            r"shire/(?P<house>[^/]+)/",
            views.ShireView.as_view(),
            name='shire',
        ),
    )
