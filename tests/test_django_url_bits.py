#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_url_bits
----------------------------------

Tests for `django_url_bits` module.
"""

from django_url_bits.django_url_bits import (
    tokenize,
    replace,
    build_url_regex,
)


def test_tokenize():
    s = "/foo/:bar/{int:baz}/"
    expected = ["/foo/", ":bar", "/", "{int:baz}", "/"]
    assert tokenize(s) == expected


def test_replace():
    assert replace("foo") == "foo"
    assert replace(":year") == "(?P<year>[0-9]{4})"
    assert replace(":month") == "(?P<month>[0-9]{2})"
    assert replace(":day") == "(?P<day>[0-9]{2})"
    assert replace(":foo") == "(?P<foo>[^/]+)"
    assert replace("{:foo}") == "(?P<foo>[^/]+)"
    assert replace("{str:foo}") == "(?P<foo>[^/]+)"
    assert replace("{int:foo}") == "(?P<foo>[0-9]+)"
    assert replace("{uuid:foo}") == (
        r"(?P<foo>"
        r"[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}"
        r"-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
        r")"
    )


def test_build_url_regex():
    s = "/foo/:bar/{int:baz}/"
    expected = "^/foo/(?P<bar>[^/]+)/(?P<baz>[0-9]+)/"
    assert build_url_regex(s) == expected + "$"
    assert build_url_regex(s, namespace=True) == expected
