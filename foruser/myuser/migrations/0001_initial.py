# Generated by Django 2.1.7 on 2019-03-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=20)),
            ],
        ),
    ]