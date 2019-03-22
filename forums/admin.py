from django.contrib import admin

from .models import Forum, Comment

class CommentInline(admin.StackedInline):
	model = Comment

class ForumAdmin(admin.ModelAdmin):
	inlines = [CommentInline]

admin.site.register(Forum, ForumAdmin)
