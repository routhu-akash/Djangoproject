from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('delete/<int:pk>/', views.delete_record, name='delete_record'),
    path('edit/<int:pk>/', views.edit_record, name='edit_record'),
]
