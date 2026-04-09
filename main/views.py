from rest_framework import generics

from .models import BlogPost, Experience, GalleryItem, Project, SiteSectionContent
from .serializers import (
	BlogPostSerializer,
	ExperienceSerializer,
	GalleryItemSerializer,
	ProjectSerializer,
	SiteSectionContentSerializer,
)


class ProjectListView(generics.ListAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer


class ExperienceListView(generics.ListAPIView):
	queryset = Experience.objects.all()
	serializer_class = ExperienceSerializer


class BlogPostListView(generics.ListAPIView):
	queryset = BlogPost.objects.all()
	serializer_class = BlogPostSerializer


class BlogPostDetailView(generics.RetrieveAPIView):
	queryset = BlogPost.objects.all()
	serializer_class = BlogPostSerializer
	lookup_field = "slug"


class GalleryItemListView(generics.ListAPIView):
	queryset = GalleryItem.objects.all()
	serializer_class = GalleryItemSerializer


class SiteSectionContentDetailView(generics.RetrieveAPIView):
	queryset = SiteSectionContent.objects.all()
	serializer_class = SiteSectionContentSerializer
	lookup_field = "section"
