from django.urls import path

from app.views import index, post, add_comment, categories, delete_category, authors

urlpatterns = [
    path('', index, name='index'),
    path('categories', categories, name='categories'),
    path('authors', authors, name='authors'),
    path('post/<int:post_id>', post, name='post'),
    path('delete_category/<int:category_id>', delete_category, name='delete_category'),
    path('add_comment', add_comment, name='add_comment'),

]
