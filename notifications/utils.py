# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User

def slug2id(slug):
    return long(slug) - 110909

def id2slug(id):
    return id + 110909

def setting(name, default=None):
    """ Return setting value for given name or default value. """
    return getattr(settings, name, default)

USER_MODEL = setting('AUTH_USER_MODEL') or \
                                'User'
