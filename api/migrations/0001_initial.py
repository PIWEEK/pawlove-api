# Generated by Django 2.0.7 on 2018-07-17 22:22

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(choices=[('Araba', 'Araba'), ('Albacete', 'Albacete'), ('Alicante', 'Alicante'), ('Almería', 'Almería'), ('Asturias', 'Asturias'), ('Ávila', 'Ávila'), ('Badajoz', 'Badajoz'), ('Barcelona', 'Barcelona'), ('Bizkaia', 'Bizkaia'), ('Burgos', 'Burgos'), ('Cáceres', 'Cáceres'), ('Cádiz', 'Cádiz'), ('Cantabria', 'Cantabria'), ('Castellón', 'Castellón'), ('Ceuta', 'Ceuta'), ('Ciudad', 'Ciudad'), ('Córdoba', 'Córdoba'), ('Cuenca', 'Cuenca'), ('Girona', 'Girona'), ('Granada', 'Granada'), ('Guadalajara', 'Guadalajara'), ('Gipuzkoa', 'Gipuzkoa'), ('Huelva', 'Huelva'), ('Huesca', 'Huesca'), ('Islas Baleares', 'Islas Baleares'), ('Jaén', 'Jaén'), ('La Coruña', 'La Coruña'), ('La Rioja', 'La Rioja'), ('Las Palmas', 'Las Palmas'), ('León', 'León'), ('Lleida', 'Lleida'), ('Lugo', 'Lugo'), ('Madrid', 'Madrid'), ('Málaga', 'Málaga'), ('Melilla', 'Melilla'), ('Murcia', 'Murcia'), ('Navarra', 'Navarra'), ('Ourense', 'Ourense'), ('Palencia', 'Palencia'), ('Pontevedra', 'Pontevedra'), ('Salamanca', 'Salamanca'), ('Segovia', 'Segovia'), ('Sevilla', 'Sevilla'), ('Soria', 'Soria'), ('Tarragona', 'Tarragona'), ('Tenerife', 'Tenerife'), ('Teruel', 'Teruel'), ('Toledo', 'Toledo'), ('Valencia', 'Valencia'), ('Valladolid', 'Valladolid'), ('Zamora', 'Zamora'), ('Zaragoza', 'Zaragoza')], max_length=100)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('sex', models.CharField(choices=[('M', 'Macho'), ('H', 'Hembra')], max_length=1)),
                ('specie', models.CharField(choices=[('P', 'Perro'), ('G', 'Gato')], max_length=1)),
                ('race', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('size', models.CharField(choices=[('P', 'Pequeño'), ('M', 'Mediano'), ('G', 'Grande')], max_length=1)),
                ('personality_1', models.TextField(blank=True, null=True)),
                ('personality_2', models.TextField(blank=True, null=True)),
                ('personality_joke', models.TextField(blank=True, null=True)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Association')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PetImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.Pet')),
            ],
        ),
        migrations.CreateModel(
            name='Adopter',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Adopter',
                'verbose_name_plural': 'Adopters',
            },
            bases=('api.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Editor',
                'verbose_name_plural': 'Editors',
            },
            bases=('api.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='association',
            name='editors',
            field=models.ManyToManyField(related_name='associations', to='api.Editor'),
        ),
    ]
