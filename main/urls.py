from django.urls import path

from .views import (
    BlogPostDetailView,
    BlogPostListView,
    ExperienceListView,
    GalleryItemListView,
    ProjectListView,
    SiteSectionContentDetailView,
)

urlpatterns = [
    path("projects", ProjectListView.as_view(), name="projects-list"),
    path("experience", ExperienceListView.as_view(), name="experience-list"),
    path("blogs", BlogPostListView.as_view(), name="blogs-list"),
    path("blogs/<slug:slug>", BlogPostDetailView.as_view(), name="blogs-detail"),
    path("gallery", GalleryItemListView.as_view(), name="gallery-list"),
    path("sections/<slug:section>", SiteSectionContentDetailView.as_view(), name="section-content-detail"),
]
