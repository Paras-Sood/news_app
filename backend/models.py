from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from rest_framework import serializers

class Source(models.Model):
    sid=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=1000)

class Article(models.Model):
    author=models.CharField(max_length=500,null=True)
    title=models.CharField(max_length=1000)
    description=models.CharField(max_length=5000,null=True)
    content=models.CharField(max_length=20000)
    publishedAt=models.DateTimeField()
    url=models.URLField(unique=True,blank=False)
    source=models.ForeignKey(Source,on_delete=CASCADE,related_name="articles")

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Source
        fields=['sid','name']

class ArticleSerializer(serializers.ModelSerializer):
    source=SourceSerializer()
    class Meta:
        model=Article
        fields=['author','title','description','content','publishedAt','url','source']