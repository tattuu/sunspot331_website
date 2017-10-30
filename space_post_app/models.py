from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey('Category', related_name='categorys', default="宇宙")
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/media/')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post = models.ForeignKey('Article', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class PopularPost(models.Model):
    """人気記事のモデル"""

    title = models.CharField(max_length=100)
    url = models.CharField('URL', max_length=255)
    page_view = models.IntegerField('ページビュー数')

    def __str__(self):
        return '{0} - {1} - {2}'.format(
            self.url, self.title, self.page_view)
