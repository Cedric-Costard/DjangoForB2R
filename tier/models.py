from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=150)
    description = models.TextField(max_length=10000)
    dateInit = models.DateTimeField(auto_now=True)
    dateEnd = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.title