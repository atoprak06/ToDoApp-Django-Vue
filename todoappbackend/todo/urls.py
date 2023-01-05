from django.urls import path
from . import views

urlpatterns = [
    path('todo/',views.TodoView,name='todo'),
    path('todo/<int:id>',views.TodoDetailView)
]   