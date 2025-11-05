from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Página principal (frontend)
    path('user/', include('user.urls')),  # URLs de usuarios
]
