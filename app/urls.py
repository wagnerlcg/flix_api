from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),
	path('api/v1/', include('eleitores.urls')),
	path('api/v1/', include('vereadores.urls')),
	path('api/v1/', include('deputados.urls')),
]
