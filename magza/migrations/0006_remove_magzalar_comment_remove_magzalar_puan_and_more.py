# Generated by Django 4.1.1 on 2025-01-15 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magza', '0005_magzalar_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magzalar',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='magzalar',
            name='puan',
        ),
        migrations.AddField(
            model_name='mcommet',
            name='magza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='magza.magzalar'),
        ),
        migrations.AddField(
            model_name='mpuan',
            name='magza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='magza.magzalar'),
        ),
    ]
