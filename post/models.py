from django.db import models
import uuid as uuid_lib

from user.models import User

# Create your models here.
class Post(models.Model):
  EVAL_LEVEL = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
  )
  id = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False) 
  post_title = models.CharField(max_length=50, blank=False)
  created_at = models.DateField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
  movie = models.CharField(max_length=100, blank=False)
  evaluation = models.IntegerField(choices=EVAL_LEVEL)
  impression = models.CharField(max_length=2000)

  def __str__(self):
    return self.post_title