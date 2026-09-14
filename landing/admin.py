from django.contrib import admin
from .models import Activity, Achievement, Event, FAQ, MediaMention, Partner, Project, TeamMember

admin.site.site_header = 'BORISTENE'
admin.site.site_title = 'BORISTENE'
admin.site.index_title = 'Website content'


class StudioAdmin(admin.ModelAdmin):
	class Media:
		css = {'all': ('css/admin.css',)}


@admin.register(Project)
class ProjectAdmin(StudioAdmin):
	list_display = ('title', 'status', 'year', 'is_featured', 'display_order')
	list_filter = ('status', 'is_featured')
	search_fields = ('title', 'short_description', 'description', 'location')
	list_editable = ('status', 'is_featured', 'display_order')
	ordering = ('display_order', '-created_at')
	prepopulated_fields = {'slug': ('title',)}
	fieldsets = (
		('Card on the website', {'fields': ('title', 'slug', 'short_description', 'image', 'image_url', 'status', 'is_featured', 'display_order')}),
		('Project facts', {'fields': ('date_label', 'location', 'year', 'goal', 'budget', 'partners', 'participants', 'outcome')}),
		('Full project page', {'fields': ('description', 'website_text', 'registration_url')}),
	)


@admin.register(Event)
class EventAdmin(StudioAdmin):
	list_display = ('title', 'date', 'location', 'is_confirmed', 'project')
	list_filter = ('is_confirmed', 'date')
	search_fields = ('title', 'location', 'description')
	date_hierarchy = 'date'
	ordering = ('date', 'display_order')


@admin.register(Partner)
class PartnerAdmin(StudioAdmin):
	list_display = ('name', 'website_url', 'display_order')
	search_fields = ('name', 'website_url')
	ordering = ('display_order', 'name')


@admin.register(Achievement)
class AchievementAdmin(StudioAdmin):
	list_display = ('number', 'label', 'display_order')
	search_fields = ('number', 'label', 'note')


@admin.register(MediaMention)
class MediaMentionAdmin(StudioAdmin):
	list_display = ('outlet', 'headline', 'published_at', 'article_url')
	search_fields = ('outlet', 'headline', 'article_url')
	list_filter = ('published_at',)


@admin.register(TeamMember)
class TeamMemberAdmin(StudioAdmin):
	list_display = ('name', 'role', 'display_order')
	search_fields = ('name', 'role', 'bio')


@admin.register(FAQ)
class FAQAdmin(StudioAdmin):
	list_display = ('question', 'category', 'display_order')
	list_filter = ('category',)
	search_fields = ('question', 'answer')


@admin.register(Activity)
class ActivityAdmin(StudioAdmin):
	list_display = ('title', 'activity_type', 'date', 'link', 'display_order')
	list_filter = ('activity_type', 'date')
	search_fields = ('title', 'description', 'link')
