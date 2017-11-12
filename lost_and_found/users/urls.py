from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
	url(r'^home/',views.home, name='home'),
	url(r'^info/',views.info, name='info')
	#url(r'^static/(?P<path>.*)', 'django.views.static.serve', 
	#{'document_root':'C:\pod\lost_and_found\static'}),
]