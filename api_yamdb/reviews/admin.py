from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role',
    )
    exclude = [
        'last_login', 'is_staff',
        'is_active', 'date_joined',
        'groups', 'user_permissions',
        'password'
    ]
    search_fields = ('username',)
    list_filter = ('id',)


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'category', 'get_genre')
    list_filter = ('year', 'category')
    list_editable = ('category',)
    search_fields = ('name',)

    @admin.display(description='Жанр(-ы)')
    def get_genre(self, obj):
        return ', '.join([genre.name for genre in obj.genre.all()])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'score',
        'pub_date',
    )
    list_filter = ('author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'review',
        'author',
        'pub_date',
    )
    list_filter = ('author',)
