from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views


urlpatterns = [
    path('', views.home, name='psinder-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('about/', PostListView.as_view(), name='psinder-about'),
    path('manyviews/', views.manyviews, name='psinder-manyviews'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
