# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass


class Upload1(models.Model):
	img = models.ImageField(upload_to = 'upload')
        finder = models.CharField(max_length=10)
        phoneNumber = models.CharField(max_length=10)
        details = models.TextField(max_length=200)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        @property
        def img_url(self):
            if self.img and hasattr(self.img, 'url'):
                return self.img.url
