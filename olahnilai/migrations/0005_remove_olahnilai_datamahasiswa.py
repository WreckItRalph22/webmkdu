# Generated by Django 4.0.3 on 2022-06-16 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olahnilai', '0004_alter_olahnilai_datakelas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='olahnilai',
            name='dataMahasiswa',
        ),
    ]
