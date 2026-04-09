from django.contrib import admin
from .models import BlogPost, Experience, GalleryItem, Project, SiteSectionContent
from unfold.admin import ModelAdmin

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
	list_display = ("id", "title")
	search_fields = ("title", "description")


@admin.register(Experience)
class ExperienceAdmin(ModelAdmin):
	list_display = ("id", "company", "role", "entry_type", "duration")
	list_filter = ("entry_type",)
	search_fields = ("company", "role", "summary")


@admin.register(BlogPost)
class BlogPostAdmin(ModelAdmin):
	list_display = ("id", "title", "slug", "published_at")
	search_fields = ("title", "slug", "excerpt", "content")
	prepopulated_fields = {"slug": ("title",)}


@admin.register(GalleryItem)
class GalleryItemAdmin(ModelAdmin):
	list_display = ("id", "title", "category")
	list_filter = ("category",)
	search_fields = ("title", "description")


@admin.register(SiteSectionContent)
class SiteSectionContentAdmin(ModelAdmin):
	list_display = ("section", "updated_at")
	search_fields = ("section",)
