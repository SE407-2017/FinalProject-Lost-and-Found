# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User
from .models import Upload1

admin.site.register(User)
admin.site.register(Upload1)
