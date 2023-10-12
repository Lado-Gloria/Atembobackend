# Generated by Django 4.2.5 on 2023-10-12 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('registration', '0007_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='This group belongs to', related_name='customer_set', to='auth.group', verbose_name='groups'),
        ),
    ]
