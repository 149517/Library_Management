from django.urls import path
from . import views

urlpatterns = [
    path('borrow/', views.borrow_view),
    path('getRecord/', views.get_record_view),
]
