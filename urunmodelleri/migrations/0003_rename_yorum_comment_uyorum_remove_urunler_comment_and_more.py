# Generated by Django 4.1.1 on 2025-01-15 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urunmodelleri', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='yorum',
            new_name='uYorum',
        ),
        migrations.RemoveField(
            model_name='urunler',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='urunler',
            name='puan',
        ),
        migrations.AddField(
            model_name='comment',
            name='urun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='urunmodelleri.urunler'),
        ),
        migrations.AddField(
            model_name='upuan',
            name='urun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='urunmodelleri.urunler'),
        ),
    ]
