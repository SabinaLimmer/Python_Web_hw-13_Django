from django.urls import path
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-quote/', views.add_quote, name='add_quote'),
    path('author/<int:author_id>/', views.view_author, name='view_author'),
    path('about_author/<int:author_id>/', views.view_author, name='about_author'),
    path('authors/', views.all_authors, name='all_authors'),
    path('quotes/', views.all_quotes, name='all_quotes'),
]
