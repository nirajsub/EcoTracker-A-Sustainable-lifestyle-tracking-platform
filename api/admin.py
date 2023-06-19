from django.contrib import admin
from .models import *


@admin.register(UserFollowers)
class UserFollowersAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(SubActivityCategoryChoices)
class SubActivityCategoryChoicesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SubActivityCategory)
class SubActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'activity_category')


@admin.register(ActivityPost)
class ActivityPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'activity_category', 'sub_activity_category', 'created_at')
    list_filter = ('activity_category', 'sub_activity_category', 'user')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_post', 'created_at')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_post', 'created_at')


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'activity_post')

admin.site.register(ImageClassification)
