# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User

admin.site.register(User)
from models import IMG

admin.site.register(IMG)