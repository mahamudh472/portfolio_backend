from django.db import models


class Project(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	tech_stack = models.JSONField(default=list)
	github = models.URLField(blank=True)

	class Meta:
		ordering = ["id"]

	def __str__(self):
		return self.title


class Experience(models.Model):
	entry_type = models.CharField(max_length=50, default="work")
	company = models.CharField(max_length=255)
	role = models.CharField(max_length=255)
	duration = models.CharField(max_length=100)
	summary = models.TextField()

	class Meta:
		ordering = ["id"]

	def __str__(self):
		return f"{self.role} @ {self.company}"


class BlogPost(models.Model):
	slug = models.SlugField(unique=True)
	title = models.CharField(max_length=255)
	excerpt = models.TextField()
	cover_image = models.URLField()
	tags = models.JSONField(default=list)
	published_at = models.DateField()
	reading_time = models.CharField(max_length=50)
	content = models.TextField()

	class Meta:
		ordering = ["-published_at", "id"]

	def __str__(self):
		return self.title


class GalleryItem(models.Model):
	title = models.CharField(max_length=255)
	category = models.CharField(max_length=120)
	description = models.TextField()
	image = models.URLField()

	class Meta:
		ordering = ["id"]

	def __str__(self):
		return self.title


class SiteSectionContent(models.Model):
	SECTION_HOME = "home"
	SECTION_ABOUT = "about"
	SECTION_CONTACT = "contact"

	SECTION_CHOICES = [
		(SECTION_HOME, "Home"),
		(SECTION_ABOUT, "About"),
		(SECTION_CONTACT, "Contact"),
	]

	section = models.CharField(max_length=50, choices=SECTION_CHOICES, unique=True)
	data = models.JSONField(default=dict)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["section"]

	def __str__(self):
		return self.section
