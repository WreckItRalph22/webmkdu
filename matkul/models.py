from django.db import models

class Mahasiswa (models.Model):
    nim = models.CharField(max_length=14)
    nama = models.CharField(max_length=255)
    prodi = models.CharField(max_length=60)

    def __str__(self):
        return self.nim

class MataKuliah (models.Model):
    mataKuliah = models.CharField('Mata Kuliah',max_length=60)
    dosen_pengajar = models.CharField('Dosen Pengajar',max_length=255)
    
    def __str__(self):
        return self.mataKuliah

class Kelas (models.Model):
    kelas = models.CharField('Kelas',null=True, max_length=4)
    matkul = models.ForeignKey(MataKuliah, null=True, on_delete=models.CASCADE)
    mahasiswa = models.ManyToManyField(Mahasiswa)

    def __str__(self):
        return self.kelas
