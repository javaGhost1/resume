from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from. import views

app_name = 'info'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)