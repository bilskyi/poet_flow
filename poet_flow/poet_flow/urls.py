from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('register/', users.register_user, name='register'),
    path('login/', users.login_user, name='login'),
    path('logout/', users.logout_user, name='logout'),
    path('explore/', include('explore.urls')),
    path('user/', include('users.urls'))
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)