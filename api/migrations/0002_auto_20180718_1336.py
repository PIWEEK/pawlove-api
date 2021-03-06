# Generated by Django 2.0.7 on 2018-07-18 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='pet',
            name='association',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='api.Association'),
        ),
        migrations.AddField(
            model_name='pet',
            name='tags',
            field=models.ManyToManyField(related_name='pets', to='api.Tag'),
        ),
    ]
