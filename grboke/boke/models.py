from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '类别'
class Tag(models.Model):
    name=models.CharField(max_length=100,unique=True,verbose_name='标签')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '标签'
class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题')
    created = models.DateField(auto_now_add=True,verbose_name='创建时间')
    modified = models.DateTimeField(auto_now=True,verbose_name='修改时间')
    # img = models.ImageField(null=True,blank=True)
    desc = RichTextUploadingField()
    content = models.TextField(verbose_name='内容')
    category = models.ForeignKey(Category,verbose_name='类别')
    tags = models.ManyToManyField(Tag,verbose_name='标签')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = '帖子'
