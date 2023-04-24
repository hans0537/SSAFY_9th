from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import BookListSerializer, BookSerializer
from .models import Book

@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    if request.method == "GET":
        books = get_list_or_404(Book)
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    # Q 2.
    elif request.method == "POST":
        book = BookSerializer(data=request.data)
        if book.is_valid(raise_exception=True):
            book.save()
            return Response(book.data, status=status.HTTP_201_CREATED)
