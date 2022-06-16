from django.contrib import admin
from .models import Kelas
from .models import MataKuliah
from .models import Mahasiswa

admin.site.register(Kelas)
admin.site.register(Mahasiswa)
admin.site.register(MataKuliah)