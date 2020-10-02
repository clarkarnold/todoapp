from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo_item_list, name='todo_item_list'),
    path('delete/<pk>/', views.delete_item, name='delete_item'),
    path('edit/<pk>/', views.edit_item, name='edit_item'),
    path('new/', views.new_item, name='new_item'),
    path('<pk>/complete/', views.mark_completed, name='mark_completed'),
]