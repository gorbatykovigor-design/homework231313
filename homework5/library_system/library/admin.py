from django.contrib import admin
from .models import Loan, Reader, Book, Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'birth_year']
    search_fields = ['name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'pages', 'publication_year', 'is_available']
    search_fields = ['title']


class ReaderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']


class LoanAdmin(admin.ModelAdmin):
    list_display = ['reader', 'book', 'loan_date', 'return_date']
    search_fields = ['reader__name', 'book__title']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Reader, ReaderAdmin)
admin.site.register(Loan, LoanAdmin)

# Register your models here.
