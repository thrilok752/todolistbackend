from django.urls import path
from tdlist import views
urlpatterns = [
    path('todolist/',views.todolist_op),
    path('todolist/<int:id>',views.todolist_op)
]