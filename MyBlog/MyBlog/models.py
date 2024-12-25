from django.db import models

#블로그 데이터베이스

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Memo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    
    #제목 표시
    def __str__(self):
        return self.title 