# Generated by Django 4.2.2 on 2023-06-05 16:24

from django.db import migrations, models
import django.utils.timezone
import todo.utils


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='description',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='completed',
            new_name='done',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='taskName',
        ),
        migrations.AddField(
            model_name='todo',
            name='assignedTo',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='dueDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.IntegerField(choices=[(1, 'NOTSTARTED'), (2, 'INPROGESS'), (3, 'COMPLETE')], default=todo.utils.StatusTypes['NOTSTARTED']),
        ),
    ]
