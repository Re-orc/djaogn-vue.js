from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('fetch/',views.todo_fetch,name='fetch'),
    path('save/',views.todo_save,name='save'),
]
