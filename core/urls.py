# i have created this file

from django.urls import path
from . import views

# http://127.0.0.1:8000/            calls the index function in views.py folder
# http://127.0.0.1:8000/index       also calls the index function in views.py folder

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("task", views.showAllTasks, name="tasks"),
    path("task/<slug:slug>", views.taskDetails, name="task_details"),
    path("task_by/<int:is_done>", views.task_by_is_done, name="task_by_is_done"),
    path("list/<slug:slug>", views.task_by_list, name="task_by_list"), 
    path('task/<int:id>/toggle/', views.toggle_task_done, name='toggle_task_done'),
    path("add_task/", views.add_task, name="add_task"),
]
