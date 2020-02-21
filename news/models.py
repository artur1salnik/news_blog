from django.db import models
from datetime import datetime

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=200)
    article_text = models.TextField('текст статьи', default="")
    pub_date = models.DateTimeField('дата публикации')
    article_image = models.ImageField('изображение', upload_to='news_images/', default="None")

    def __str__(self):
        return self.article_title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 100)
    comment_text = models.TextField('текст комментария', max_length=1000)
    comment_date = models.DateTimeField('дата комментария', default=datetime.now)

    def __str__(self):
        return self.author_name

# class ArticleImage(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True, default=None)
#     article_image = models.ImageField(upload_to='news_images/')

# class ArticleImage(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.PROTECT, blank=True, null=True, default=None)
#     image = models.ImageField(upload_to='/news_images/')
#
#     def __str__(self):
#         return "%s" % self.id
