from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_view),
    path('query/',views.query_view),
]
