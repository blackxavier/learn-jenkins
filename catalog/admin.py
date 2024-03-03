from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance,Language


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('display_book','display_date_due_back', 'display_status')
    list_filter = ('status','due_back')
    readonly_fields = ('created_date', 'modified_date')
    
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
class BooksAdminInline(admin.StackedInline):
    model = Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre','display_language')
    readonly_fields = ('created_date', 'modified_date')
    inlines = [BooksInstanceInline]
    

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    readonly_fields = ('created_date', 'modified_date')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksAdminInline]