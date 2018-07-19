# Generated by Django 2.0.7 on 2018-07-19 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_answer_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='adopted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to='api.Tag'),
        ),
    ]