from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('books/', include('books.urls')),
    path('record/', include('record.urls')),
]
