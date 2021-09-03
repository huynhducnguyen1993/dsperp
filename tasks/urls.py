from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('', Task_.as_view(), name="list"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('complete_task/', views.completeTask, name="complete_task"),	
	path('uncomplete_task/', views.uncompleteTask, name="uncomplete_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
]