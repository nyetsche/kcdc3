from pinata.models import Page, Notice, Slide, Sponsor, Press_Clipping
from django import forms
from django.contrib import admin
from django.contrib.admin.sites import site
from django.contrib.admin.widgets import ManyToManyRawIdWidget, ForeignKeyRawIdWidget
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_unicode
from django.utils.html import escape



class PageAdmin(admin.ModelAdmin):
	
	fieldsets = [
		(None, {'fields': [
			'title', 'short_title', 'parent', 'path', 'status', 'sort_order',
			]}),
		('Text', {
			'classes': ('grp-collapse grp-open',),
			'fields': [
			#'teaser',
			'main_text'
			]}),
		('Additional Text', {
			'classes': ('grp-collapse grp-closed',),
			'fields': [
			'sidebar_text',
			]}),
	]

	list_display = ('title', 'short_title', 'status', 'parent', 'path', 'sort_order',)
	list_editable = ('status', 'sort_order',)

	class Media:
		js = [
			'tiny_mce/tiny_mce.js',
			'tinymce_setup.js',
		]

admin.site.register(Page, PageAdmin)





class NoticeAdmin(admin.ModelAdmin):
	
	fieldsets = [
		(None, {'fields': [
			'title', 'main_text', 'live', 'sort_order',
			]}),
	]

	list_display = ('title', 'live', 'sort_order',)
	list_editable = ('live', 'sort_order',)

admin.site.register(Notice, NoticeAdmin)





class SlideAdmin(admin.ModelAdmin):
	
	fieldsets = [
		(None, {'fields': [
			'title', 'image', 'main_text', 'live',
			]}),
	]

	list_display = ('title', 'live', 'image',)
	list_editable = ('live',)

admin.site.register(Slide, SlideAdmin)





class SponsorAdmin(admin.ModelAdmin):
	
	fieldsets = [
		(None, {'fields': [
			'title', 
			('group', 'status', 'sort_order',),
			'destination_url', 
			'image',
			# 'main_text',
			]}),
	]

	list_display = ('title', 'status', 'group',)
	list_editable = ('status', 'group',)

	class Media:
		js = [
			'tiny_mce/tiny_mce.js',
			'tinymce_setup.js',
		]

admin.site.register(Sponsor, SponsorAdmin)




class Press_ClippingAdmin(admin.ModelAdmin):
	
	fieldsets = [
		(None, {'fields': [
			'title', 
			'date', 
			'publication',
			'destination_url',
			'main_text',
			'excerpt',
			'status',
			]}),
	]

	list_display = ('title', 'status', 'date',)
	list_editable = ('status',)
	
	class Media:
		js = [
			'tiny_mce/tiny_mce.js',
			'tinymce_setup.js',
		]
	

admin.site.register(Press_Clipping, Press_ClippingAdmin)

