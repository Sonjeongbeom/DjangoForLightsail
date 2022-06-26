from django.db import models
from datetime import datetime

class Post(models.Model) : 
    title = models.CharField(max_length=100, null=False, blank=False)
    # author = models.ForeignKey(User, on_delete=CASCADE, default=1)
    postDate = models.DateTimeField(default=datetime.now)
    content = models.TextField(null=False, blank=False)

    def __str__(self) :
        return self.title

