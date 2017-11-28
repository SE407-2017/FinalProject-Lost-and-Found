from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
	url(r'^home/',views.home, name='home'),
	url(r'^info/',views.info, name='info'),
	url(r'^opinion/',views.opinion, name='opinion'),
	url(r'^change_information/',views.change_information, name='change_information'),
	url(r'^about_us/',views.about_us, name='about'),
        url(r'^delete/',views.delete, name='delete'),
	#url(r'^static/(?P<path>.*)', 'django.views.static.serve', 
	#{'document_root':'C:\pod\lost_and_found\static'}),
]
