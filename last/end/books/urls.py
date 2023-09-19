from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_view),
    path('query/',views.query_view),
    path('add/', views.add_view),
    path('fix/', views.fix_view),
    path('getList/', views.getList_view)
]
