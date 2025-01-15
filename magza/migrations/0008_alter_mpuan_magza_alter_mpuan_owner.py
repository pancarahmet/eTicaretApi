# Generated by Django 4.1.1 on 2025-01-15 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magza', '0007_alter_mpuan_magza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpuan',
            name='magza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='magza.magzalar'),
        ),
        migrations.AlterField(
            model_name='mpuan',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
