# Generated by Django 4.0.3 on 2022-06-16 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matkul', '0004_alter_kelas_mahasiswa_alter_kelas_matkul'),
        ('olahnilai', '0002_olahnilai_datamahasiswa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olahnilai',
            name='dataKelas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matkul.kelas'),
        ),
        migrations.AlterField(
            model_name='olahnilai',
            name='dataMahasiswa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matkul.mahasiswa'),
        ),
    ]
