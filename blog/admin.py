from django.contrib import admin
from .models import BlogModel, LikeModel, CommentModel


# Register your models here.
@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
	model = BlogModel
	list_display = ( 'title', 'author', 'publish_date', )
	list_filter = ( 'published', )
	search_fields = ( 'title', 'slug', )
	prepopulated_fields = {
        'slug': ( 'title', )
    }
	date_hierarchy = 'publish_date'
	save_on_top = True


@admin.register(LikeModel)
class LikeModelAdmin(admin.ModelAdmin):
    model = LikeModel


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    model = CommentModel