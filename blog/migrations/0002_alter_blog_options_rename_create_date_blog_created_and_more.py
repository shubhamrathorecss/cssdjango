# Generated by Django 4.2.3 on 2023-08-02 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish']},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='create_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='modified_date',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='blog',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='slug', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(),
        ),
        migrations.AddIndex(
            model_name='blog',
            index=models.Index(fields=['-publish'], name='blog_blog_publish_1d1149_idx'),
        ),
    ]
