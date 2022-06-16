from django.db import models
from matkul.models import Kelas
from matkul.models import Mahasiswa

class OlahNilai (models.Model):
    dataKelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    nilai_absen = models.IntegerField()
    nilai_tugas = models.IntegerField()
    nilai_uts = models.IntegerField()
    nilai_uas = models.IntegerField()

    def __str__(self):
        return self.dataKelas
    
    @property
    def hitungNilai(self):
        hitung1 = self.nilai_absen * (15/100)
        hitung2 = self.nilai_tugas * (35/100)
        hitung3 = self.nilai_uas * (20/100)
        hitung4 = self.nilai_uts * (30/100)
        total = hitung1+hitung2+hitung3+hitung4

        return total