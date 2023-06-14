from django.urls import path
from . import views

urlpatterns = [
    #Add task
    path('add-task/', views.addTask, name='add-task'),
    
    #Done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    
    #Undone
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    
    #Edit
    path('edit_task/<int:pk>/', views.editTask, name='edit-task'),
    
    #Delete
    path('delete_task/<int:pk>/', views.deleteTask, name='delete-task'),
]