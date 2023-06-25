from django.db import models
from django.contrib.auth.models import User

class UserFollowers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='followers')
    followings = models.ManyToManyField(User, related_name='following')

    def __str__(self):
        return self.user.username

class ActivityCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubActivityCategory(models.Model):
    name = models.CharField(max_length=255)
    activity_category = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SubActivityCategoryChoices(models.Model):
    name = models.CharField(max_length=255)
    sub_activity_category = models.ManyToManyField(SubActivityCategory)

    def __str__(self):
        return self.name

TYPE = (
    ("Had", "Had"),
    ("Prepared", "Prepared"),
)
class ActivityPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_method = models.CharField(
        max_length=20, choices=TYPE, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='activity_images')
    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    carbon_footprint_reduction = models.DecimalField(max_digits=10, decimal_places=2)
    water_saved = models.DecimalField(max_digits=10, decimal_places=2)
    land_saved = models.DecimalField(max_digits=10, decimal_places=2)
    activity_category = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE)
    sub_activity_category = models.ForeignKey(SubActivityCategory, on_delete=models.CASCADE)
    sub_activity_category_choices = models.ForeignKey(SubActivityCategoryChoices, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_post = models.ForeignKey(ActivityPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.activity_post.title}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_post = models.ForeignKey(ActivityPost, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like by {self.user.username} on {self.activity_post.title}'


class Hashtag(models.Model):
    name = models.CharField(max_length=255)
    activity_post = models.ForeignKey(ActivityPost, on_delete=models.CASCADE, related_name='hashtags')

    def __str__(self):
        return self.name

class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    detail = models.TextField()
    location = models.CharField(max_length=255)
    goal = models.CharField(max_length=255)
    targets = models.TextField()
    participants = models.ManyToManyField(User, related_name='events_participated')

    def __str__(self):
        return self.name

class EventContribution(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='contributions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contribution = models.TextField()

    def __str__(self):
        return f'Contribution by {self.user.username} to {self.event.name}'

class EventPost(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post by {self.user.username} on {self.event.name}'

class EventParticipant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_participants')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} joined {self.event.name}'


class ClassifyItem(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images')
    category = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ImageClassification(models.Model):
    image = models.ImageField(upload_to='image_classification')
    predicted_labels = models.CharField(max_length=255, blank=True, null=True)
    saved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)