# Generated by Django 2.0.7 on 2018-07-18 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180718_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to='api.Tag'),
        ),
    ]