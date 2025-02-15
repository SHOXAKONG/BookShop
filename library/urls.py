from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('books/', list_books, name="list_books"),
    path("books_detail/<int:pk>/", BookDetail.as_view(), name="book_detail"),
    path('books/create', create_book, name="book-create"),
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout, name='logout'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:book_id>', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:book_id>', remove_item, name='remove_item')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)