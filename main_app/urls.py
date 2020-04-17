from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_book),
    path('submit_book', views.submit_book),
    path('add_author', views.add_author),
    path('submit_author', views.submit_author),
    path('submitted_book_form', views.submitted_book_form),
    path('submitted_author_form', views.submitted_author_form),
    path('book_info/<int:book_id>', views.book_info),
    path('author_info/<int:author_id>', views.author_info),
    path('update_book_author', views.update_book_author),
    path('update_author_book', views.update_author_book),
]