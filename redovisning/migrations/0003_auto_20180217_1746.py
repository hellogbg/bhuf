# Generated by Django 2.0.1 on 2018-02-17 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('redovisning', '0002_user_org_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='org_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redovisning.Organization'),
        ),
    ]
