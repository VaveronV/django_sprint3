from django.contrib import admin
from .models import Category, Location, Post

admin.site.site_header = 'Панель администратора блога'
admin.site.site_title = 'Админ-панель'
admin.site.index_title = 'Управление контентом'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'location',
                    'is_published', 'pub_date', 'created_at'
                    )
    list_filter = ('is_published', 'category', 'location', 'pub_date')
    search_fields = ('title', 'text', 'author__username')
    list_editable = ('is_published',)
    date_hierarchy = 'pub_date'
    filter_horizontal = ()
    raw_id_fields = ('author',)
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'text', 'author')
        }),
        ('Классификация', {
            'fields': ('category', 'location')
        }),
        ('Публикация', {
            'fields': ('is_published', 'pub_date', 'created_at')
        }),
    )
