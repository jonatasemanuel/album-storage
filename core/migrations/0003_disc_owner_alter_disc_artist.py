# Generated by Django 4.1.6 on 2023-02-07 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_remove_disc_owner_artist_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='disc',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='disc',
            name='artist',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.artist'),
        ),
    ]