from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import * 
"""импортируем все функции из views"""

urlpatterns = [
    path('', main, name='main'),
    path('word/', word),
    path('words/<int:word_id>',  show_word, name='show_word'),
    path('words/<int:word_id>/learn',  learn_word, name='learn_word'),
    path('words/<int:word_id>/delete',  delete_word, name='delete_word'),
    path('hello', HelloView.as_view()),
    path('template', MyTemplateView.as_view()),
    # # path('catalog/', catalog),
    # path('products/', pro,ducts),
    # path('feedback/', add_feedback),
    # path('branch/', branch),
    # path('book/add/', add_product),
    # path('news/add/', add_news, name='add_news'),
    # path('news/edit/<slug:news_url>/', edit_news, name='edit_news'),
    # path('news/delete/<slug:news_url>/', delete_news, name='delete_news'),
    # path('news/<slug:news_url>/', show_news, name='show_news'),
    # path('news/', list_news, name='list_news'),
    # path('genre/add/', add_genre),
    # path('genre/delete-genre/<int:genre_id>/', delete_genre, name='delete_genre'),
    # path('genre/edit-genre/<int:genre_id>/', edit_genre, name='edit_genre'),
    # path('branch/add/', add_branch),
    # path('genres/<slug:genre_url>-<int:genres_id>/', genres, name='genre_detail'),
    # path('genres/<slug:genre_url>-<int:genres_id>/book/<slug:book_url>-<int:book_id>/', book, name='book_detail'),
]
# urlpatterns += [
#     re_path(r'^(?P<url>.*)/$', dynamic_page, name='dynamic_page'),
# ]
handler404 = 'web.views.custom_404_view'