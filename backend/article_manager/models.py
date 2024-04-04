from django.db import models


class Article(models.Model):
    # 文章编号
    article_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=100)
    author_id = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)

# Create your models here.
