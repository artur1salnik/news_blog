# Generated by Django 2.2.5 on 2020-04-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_comment_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(default='', verbose_name='текст статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=200, verbose_name='название статьи'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author_name',
            field=models.CharField(max_length=100, verbose_name='имя автора'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(max_length=1000, verbose_name='текст комментария'),
        ),
    ]
