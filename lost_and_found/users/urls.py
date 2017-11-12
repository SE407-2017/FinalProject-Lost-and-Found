from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
	url(r'^personal_information/',views.shiyan, name='personal_information')
	#url(r'^static/(?P<path>.*)', 'django.views.static.serve', 
	#{'document_root':'C:\pod\lost_and_found\static'}),
]