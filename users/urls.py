from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'users'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logut/',views.logout_view,name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
