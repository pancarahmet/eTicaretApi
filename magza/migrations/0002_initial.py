# Generated by Django 4.1.1 on 2025-01-14 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpuan',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mcommet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='magzalar',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userMagza', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='magzalar',
            name='puan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='magza.mpuan'),
        ),
        migrations.AddField(
            model_name='bankalar',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magza.magzalar'),
        ),
    ]