# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile,Posts,Images
# Register your models here.

admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(Images)