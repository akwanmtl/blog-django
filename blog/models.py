from django.db import models

from django.utils import timezone

# Create your models here.
class User(models.Model):
  username = models.CharField(max_length=256, blank=False, null=False)
  password = models.CharField(max_length=256, blank=False, null=False)

  def __str__(self):
    """A human representation of the user object"""
    return "username: {0} | password: {1}".format(self.username, self.password) 

class Post(models.Model):
  created = models.DateTimeField(default=timezone.now())

  modified = models.DateTimeField(default=timezone.now())
  
  title = models.CharField(max_length=256, blank=False, null=False)

  body = models.TextField(blank=False, null=False)

  def __str__(self):
    """A human representation of the post object"""
    return "created: {0} | modifed: {1} | title: {2} | body: {3}".format(self.created, self.modified, self.title, self.body)

  def save(self, *args, **kwargs):
    """ Add created_at and updated_at timestamps. """
    
    self.modified = timezone.now()
    if not self.id:
        self.created = timezone.now()


    return super(Post, self).save(*args, **kwargs)