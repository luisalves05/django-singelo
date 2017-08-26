from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):

    POST_STATUS = (
        ('publish', 'Publish'),
        ('draft', 'Draft')
    )

    post_id         = models.AutoField(primary_key = True)
    post_title      = models.CharField(max_length = 150, unique = True)
    post_author     = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
    post_created    = models.DateTimeField(auto_now_add = True)
    post_content    = models.TextField()
    post_slug       = models.SlugField(max_length = 150)
    post_status     = models.CharField(max_length = 50, choices = POST_STATUS)

    def save(self, *args, **kwargs):
        self.post_slug = slugify(self.post_title)
        super(Post, self).save(*args, **kwargs)
