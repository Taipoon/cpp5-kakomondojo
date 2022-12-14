# Generated by Django 4.0.6 on 2022-07-29 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('academic_year', models.IntegerField(verbose_name='開講年度')),
                ('semester', models.CharField(max_length=4, verbose_name='学期')),
                ('credits', models.IntegerField(verbose_name='単位数')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('lecture_number', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kakomon.course')),
            ],
        ),
        migrations.CreateModel(
            name='SampleAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('issue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kakomon.issue')),
            ],
        ),
    ]
