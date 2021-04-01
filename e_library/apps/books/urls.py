from django.urls import path
from . import views
from django.conf.urls import url
from django_filters.views import FilterView
from apps.management.filters import BookFilter

urlpatterns=[

    path('book/<int:pk>/',views.BookDetailView, name='book-detail'),
    path('book/new/', views.BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update/',views.BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),

   url(r'^search/$', FilterView.as_view(filterset_class=BookFilter,
   template_name='books/search_book_list.html'), name='search_results'),

    path('rating/update/',views.RatingUpdate, name='rating_update'),

]