# Generated by Django 4.1.1 on 2025-01-14 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magza', '0003_magzalar_guncelleme_zamani_magzalar_olusturma_zamani'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magzalar',
            name='puan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='magza.mpuan'),
        ),
    ]