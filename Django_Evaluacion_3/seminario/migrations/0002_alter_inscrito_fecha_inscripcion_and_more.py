# Generated by Django 4.2.4 on 2023-12-18 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscrito',
            name='fecha_inscripcion',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='inscrito',
            name='hora_inscripcion',
            field=models.TimeField(),
        ),
    ]
