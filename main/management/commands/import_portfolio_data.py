import json
from datetime import date
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from main.models import BlogPost, Experience, GalleryItem, Project, SiteSectionContent


class Command(BaseCommand):
    help = "Import portfolio data from backend data JSON files into the database."

    def handle(self, *args, **options):
        data_dir = Path(settings.BASE_DIR) / "data"

        required_files = {
            "projects": data_dir / "projects.json",
            "experience": data_dir / "experience.json",
            "blogs": data_dir / "blogs.json",
            "gallery": data_dir / "gallery.json",
            "home": data_dir / "home.json",
            "about": data_dir / "about.json",
            "contact": data_dir / "contact.json",
        }

        missing_files = [str(path) for path in required_files.values() if not path.exists()]
        if missing_files:
            raise CommandError(
                f"Missing data files in backend data directory ({data_dir}): {', '.join(missing_files)}"
            )

        with transaction.atomic():
            projects = self._load_json(required_files["projects"])
            experience_records = self._load_json(required_files["experience"])
            blogs = self._load_json(required_files["blogs"])
            gallery_items = self._load_json(required_files["gallery"])
            home_section = self._load_json(required_files["home"])
            about_section = self._load_json(required_files["about"])
            contact_section = self._load_json(required_files["contact"])

            project_count = self._import_projects(projects)
            experience_count = self._import_experience(experience_records)
            blog_count = self._import_blogs(blogs)
            gallery_count = self._import_gallery(gallery_items)
            section_count = self._import_sections(home_section, about_section, contact_section)

        self.stdout.write(self.style.SUCCESS("Portfolio data import completed."))
        self.stdout.write(
            f"Projects: {project_count}, Experience: {experience_count}, Blogs: {blog_count}, Gallery: {gallery_count}, Sections: {section_count}"
        )

    def _load_json(self, file_path: Path):
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def _import_projects(self, rows):
        for row in rows:
            Project.objects.update_or_create(
                id=row["id"],
                defaults={
                    "title": row["title"],
                    "description": row["description"],
                    "tech_stack": row.get("techStack", []),
                    "github": row.get("github", ""),
                },
            )
        return len(rows)

    def _import_experience(self, rows):
        for row in rows:
            Experience.objects.update_or_create(
                id=row["id"],
                defaults={
                    "entry_type": row.get("type", "work"),
                    "company": row["company"],
                    "role": row["role"],
                    "duration": row["duration"],
                    "summary": row["summary"],
                },
            )
        return len(rows)

    def _import_blogs(self, rows):
        for row in rows:
            BlogPost.objects.update_or_create(
                id=row["id"],
                defaults={
                    "slug": row["slug"],
                    "title": row["title"],
                    "excerpt": row["excerpt"],
                    "cover_image": row["coverImage"],
                    "tags": row.get("tags", []),
                    "published_at": self._parse_date(row["publishedAt"]),
                    "reading_time": row["readingTime"],
                    "content": row["content"],
                },
            )
        return len(rows)

    def _import_gallery(self, rows):
        for row in rows:
            GalleryItem.objects.update_or_create(
                id=row["id"],
                defaults={
                    "title": row["title"],
                    "category": row["category"],
                    "description": row["description"],
                    "image": row["image"],
                },
            )
        return len(rows)

    def _import_sections(self, home_section, about_section, contact_section):
        payload_by_section = {
            SiteSectionContent.SECTION_HOME: home_section,
            SiteSectionContent.SECTION_ABOUT: about_section,
            SiteSectionContent.SECTION_CONTACT: contact_section,
        }

        for section_name, section_payload in payload_by_section.items():
            SiteSectionContent.objects.update_or_create(
                section=section_name,
                defaults={
                    "data": section_payload,
                },
            )

        return len(payload_by_section)

    def _parse_date(self, value: str) -> date:
        try:
            return date.fromisoformat(value)
        except ValueError as error:
            raise CommandError(f"Invalid date '{value}' in blogs.json") from error
