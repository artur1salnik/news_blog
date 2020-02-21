# Generated by Django 2.2.5 on 2019-11-01 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20191015_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(max_length=500, verbose_name='текст комментария'),
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_image', models.ImageField(upload_to='news_images/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Article')),
            ],
        ),
    ]
