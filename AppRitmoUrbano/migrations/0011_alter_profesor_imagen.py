# Generated by Django 4.0.3 on 2023-02-06 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRitmoUrbano', '0010_alter_curso_profesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/profesores'),
        ),
    ]
