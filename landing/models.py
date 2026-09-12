from django.db import models


class Project(models.Model):
	CURRENT = 'current'
	PAST = 'past'
	STATUS_CHOICES = [(CURRENT, 'Current'), (PAST, 'Past')]

	title = models.CharField(max_length=180)
	slug = models.SlugField(unique=True)
	short_description = models.TextField()
	description = models.TextField(blank=True)
	image_url = models.URLField(blank=True)
	image = models.FileField(upload_to='projects/', blank=True)
	registration_url = models.URLField(blank=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=CURRENT)
	year = models.PositiveIntegerField(null=True, blank=True)
	location = models.CharField(max_length=180, blank=True)
	is_featured = models.BooleanField(default=False)
	display_order = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['display_order', '-created_at']

	def __str__(self):
		return self.title


class Partner(models.Model):
	name = models.CharField(max_length=180)
	logo_url = models.URLField(blank=True)
	logo = models.FileField(upload_to='partners/', blank=True)
	website_url = models.URLField(blank=True)
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['display_order', 'name']

	def __str__(self):
		return self.name


class Event(models.Model):
	title = models.CharField(max_length=180)
	date = models.DateField(null=True, blank=True)
	date_label = models.CharField(max_length=80, blank=True)
	location = models.CharField(max_length=180, blank=True)
	description = models.TextField(blank=True)
	image = models.FileField(upload_to='events/', blank=True)
	project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL, related_name='events')
	is_confirmed = models.BooleanField(default=False)
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['date', 'display_order']

	def __str__(self):
		return self.title


class Achievement(models.Model):
	number = models.CharField(max_length=40)
	label = models.CharField(max_length=120)
	note = models.TextField(blank=True)
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['display_order']

	def __str__(self):
		return f'{self.number} - {self.label}'


class MediaMention(models.Model):
	outlet = models.CharField(max_length=180)
	headline = models.CharField(max_length=220, blank=True)
	published_at = models.DateField(null=True, blank=True)
	image_url = models.URLField(blank=True)
	image = models.FileField(upload_to='media/', blank=True)
	article_url = models.URLField(blank=True)
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['-published_at', 'display_order']

	def __str__(self):
		return self.outlet


class TeamMember(models.Model):
	name = models.CharField(max_length=160)
	role = models.CharField(max_length=160)
	bio = models.TextField(blank=True)
	photo_url = models.URLField(blank=True)
	photo = models.FileField(upload_to='team/', blank=True)
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['display_order', 'name']

	def __str__(self):
		return self.name


class FAQ(models.Model):
	CATEGORY_CHOICES = [
		('about', 'About Boristene'),
		('events', 'Events & Activities'),
		('join', 'Getting Involved'),
		('donations', 'Donations & Tax Benefits'),
		('project', 'Unbreakable Ukraine'),
	]

	question = models.CharField(max_length=240)
	answer = models.TextField()
	category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='about')
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['category', 'display_order']

	def __str__(self):
		return self.question


class Activity(models.Model):
	ACTIVITY_TYPES = [
		('event', 'Event'),
		('project', 'Project'),
		('publication', 'Publication'),
		('other', 'Other'),
	]

	title = models.CharField(max_length=180)
	description = models.TextField()
	date = models.DateField(null=True, blank=True)
	activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES, default='event')
	image_url = models.URLField(blank=True)
	image = models.FileField(upload_to='activities/', blank=True)
	link = models.URLField(blank=True)
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['-date', 'display_order']

	def __str__(self):
		return self.title
