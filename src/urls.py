from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('some_app/', include('some_app.urls')),
    path('Cw_20/', include('Cw20.urls')),
    path('hw_21/', include('hw_21.urls')),
]
