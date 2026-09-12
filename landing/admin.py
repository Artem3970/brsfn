from django.contrib import admin
from .models import Activity, Achievement, Event, FAQ, MediaMention, Partner, Project, TeamMember


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'status', 'year', 'is_featured', 'display_order')
	list_filter = ('status', 'is_featured')
	prepopulated_fields = {'slug': ('title',)}


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'location', 'is_confirmed', 'project')
	list_filter = ('is_confirmed', 'date')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
	list_display = ('name', 'website_url', 'display_order')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
	list_display = ('number', 'label', 'display_order')


@admin.register(MediaMention)
class MediaMentionAdmin(admin.ModelAdmin):
	list_display = ('outlet', 'headline', 'published_at', 'article_url')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
	list_display = ('name', 'role', 'display_order')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
	list_display = ('question', 'category', 'display_order')
	list_filter = ('category',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('title', 'activity_type', 'date', 'link', 'display_order')
	list_filter = ('activity_type', 'date')
