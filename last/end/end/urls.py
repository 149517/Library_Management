
from django.contrib import admin
from django.urls import path, include
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
<<<<<<< HEAD
    path('books/', include('books.urls')),
    path('record/',include('record.urls'))
=======
    path('books/', include('books.urls'))
>>>>>>> 326b59aa53e211a6e29b8a033e45707b234981e4
]
