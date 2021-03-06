# Generated by Django 3.0 on 2021-11-22 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100, verbose_name='توضیحات')),
                ('rate', models.IntegerField(verbose_name='امتیاز')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('time', models.DateField(auto_now_add=True, verbose_name='زمان  انتشار')),
                ('photo', models.ImageField(upload_to='foods/')),
            ],
        ),
    ]
