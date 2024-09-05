from django.urls import path
from .views import index, create, detail, update, delete


app_name = 'tasks'
urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('detail/<int:task_id>/', detail, name='detail'),
    path('update/<int:task_id>/', update, name='update'),
    path('delete/<int:task_id>/', delete, name='delete'),

]