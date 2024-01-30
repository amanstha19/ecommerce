from django.views import View
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import AuthView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HOME, name='home'),
    path('base/', views.BASE, name='base'),
    path('product/', views.product, name='product'),
    path('register/', views.register, name='register'),
    path('main/register/auth/', AuthView.as_view(), name='auth'),
    path('login/', views.user_login, name='login'),
    path('userprofile/',views.userprofile,name='userprofile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
