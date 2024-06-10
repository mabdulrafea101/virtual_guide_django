from django.db import models

# Create your models here.


class EventCategory(models.Model):
    class Meta:
        app_label = "university"
        managed = True
        verbose_name = 'Event Category'
        verbose_name_plural = 'Event Categories'
    name = models.CharField(
        max_length=50, blank=True, null=True)
    description = models.CharField(
        max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="events/categories/",
                              null=True, default="default_img.jpeg")
    
    def __str__(self):
        return self.name


class Event(models.Model):
    class Meta:
        app_label = "university"
        managed = True
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(
        'user.CustomUser',
        related_name='events',
        on_delete=models.CASCADE)
    category = models.ForeignKey(EventCategory,
                                 on_delete=models.PROTECT,
                                 related_name="event")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="events/",
                              null=True, default="default_img.jpeg")
    # Assuming the rating is an integer

    def __str__(self):
        return self.title


# class Image(models.Model):
#     class Meta:
#         app_label = "university"
#         managed = True
#         verbose_name = 'Image'
#         verbose_name_plural = 'Images'
#     post = models.ForeignKey(Event,
#                              on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='blog_images/')

#     def __str__(self):
#         return f"Image for {self.post.title}"


class Comment(models.Model):
    class Meta:
        app_label = "university"
        managed = True
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    post = models.ForeignKey(Event,
                             on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        'user.CustomUser',
        related_name='comments',
        on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
