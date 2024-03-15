from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    created_datetime = models.DateTimeField()
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"Post {self.id}: {self.title}"
