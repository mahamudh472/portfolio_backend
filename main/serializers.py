from rest_framework import serializers

from .models import BlogPost, Experience, GalleryItem, Project, SiteSectionContent


class ProjectSerializer(serializers.ModelSerializer):
    techStack = serializers.JSONField(source="tech_stack")

    class Meta:
        model = Project
        fields = ["id", "title", "description", "techStack", "github"]


class ExperienceSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="entry_type")

    class Meta:
        model = Experience
        fields = ["id", "type", "company", "role", "duration", "summary"]


class BlogPostSerializer(serializers.ModelSerializer):
    coverImage = serializers.URLField(source="cover_image")
    publishedAt = serializers.DateField(source="published_at")
    readingTime = serializers.CharField(source="reading_time")

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "slug",
            "title",
            "excerpt",
            "coverImage",
            "tags",
            "publishedAt",
            "readingTime",
            "content",
        ]


class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = ["id", "title", "category", "description", "image"]


class SiteSectionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSectionContent
        fields = ["section", "data", "updated_at"]
