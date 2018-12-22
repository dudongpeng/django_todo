# Generated by Django 2.1.4 on 2018-12-21 12:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='内容')),
                ('creat_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('status', models.BooleanField(default=False, verbose_name='状态')),
                ('finish_time', models.DateTimeField(auto_now=True, verbose_name='结束时间')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='qid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.User'),
        ),
    ]
