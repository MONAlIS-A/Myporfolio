from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('projects/', views.Projects, name='projects'),
    path('skills/', views.Skills, name='skills'),
    path('blogs/', views.Blogs, name='blogs'),
    path('contact/', views.Contact, name='contact'),
   


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
