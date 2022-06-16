# Generated by Django 4.0.3 on 2022-06-16 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matkul', '0004_alter_kelas_mahasiswa_alter_kelas_matkul'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kelas',
            name='kelas',
            field=models.CharField(max_length=4, null=True, verbose_name='Kelas'),
        ),
        migrations.AlterField(
            model_name='kelas',
            name='matkul',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matkul.matakuliah'),
        ),
    ]
