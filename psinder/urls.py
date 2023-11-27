from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views


urlpatterns = [
    path('', views.home, name='psinder-home'),
    path('about/', views.about, name='psinder-about'),
    path('manyviews/', views.manyviews, name='psinder-manyviews'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
