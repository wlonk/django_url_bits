# -*- coding: utf-8 -*-

import re

TOKENIZE_RE = re.compile(r'(\{.*?:.+?\}|:[0-9A-Za-z_]+)')


def tokenize(s):
    return TOKENIZE_RE.split(s)


def replace(bit):
    should_replace = bit.startswith(":") or bit.startswith("{") and ":" in bit
    if should_replace:
        bit = bit.strip("{").rstrip("}")
        type_, tag = bit.split(":", 1)
        if tag == "year" and not type_:
            type_re = "[0-9]{4}"
        elif tag == "month" and not type_:
            type_re = "[0-9]{2}"
        elif tag == "day" and not type_:
            type_re = "[0-9]{2}"
        elif type_ == "uuid":
            type_re = (
                r'[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}'
                r'-[89ab][0-9a-f]{3}-[0-9a-f]{12}'
            )
        elif type_ == "int":
            type_re = "[0-9]+"
        else:
            type_re = "[^/]+"
        return "(?P<{tag}>{type_re})".format(tag=tag, type_re=type_re)
    else:
        return bit


def build_url_regex(s, namespace=False):
    bits = tokenize(s)
    ret = "".join(replace(bit) for bit in bits)
    suffix = "$"
    if namespace:
        suffix = ""
    return "^" + ret + suffix
