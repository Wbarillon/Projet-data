# Generated by Django 3.0.2 on 2020-01-31 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hatvp_app', '0004_auto_20200131_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organigramme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fonction_collaborateur', models.TextField(blank=True, max_length=300, null=True)),
                ('representants_id', models.IntegerField(null=True)),
                ('collaborateur', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
