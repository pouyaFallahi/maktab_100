from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/', include('Task.urls')),
    path('passage/', include('User.urls')),
    path('', include('User.urls'))
]
