"""lost_and_found URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles
from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls',namespace='users')),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
	url(r'^users/home/',views.home),
    url(r'^show', views.showImg,name='show'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
