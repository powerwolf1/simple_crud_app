from django.urls import path  # type: ignore
from .views import index, create, detail, update, delete, filter_by_category, get_categories  # type: ignore

app_name = 'tasks'
urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('detail/<int:task_id>/', detail, name='detail'),
    path('update/<int:task_id>/', update, name='update'),
    path('delete/<int:task_id>/', delete, name='delete'),

    path('filter_by_category/<int:category_id>/', filter_by_category, name='filter_by_category'),

    path('categories/', get_categories, name='categories'),

]