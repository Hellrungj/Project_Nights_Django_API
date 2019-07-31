# Generated by Django 2.2 on 2019-07-30 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='junceventtype',
            name='type_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='quickstart.Type'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='junceventtype',
            unique_together={('event_id', 'type_id')},
        ),
        migrations.RemoveField(
            model_name='junceventtype',
            name='user_id',
        ),
    ]