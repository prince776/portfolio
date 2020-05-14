from django.urls import path
from . import views

app_name = 'aboutme'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('experiences/', views.experiences, name='experiences'),
    path('contact/', views.contact, name='contact'),
    path('mailtome/', views.mail_to_me, name='mailtome'),
    path('certificates/', views.certificates, name='certificates')
]
