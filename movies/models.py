from django.db import models

# Create your models here.

class Kategori(models.Model):
    isim=models.CharField(max_length=50)

    def __str__(self):
        return self.isim

class Movie(models.Model):
    isim=models.CharField(max_length=50)
    resim=models.FileField(upload_to="filmler/", verbose_name="Film Resmi", null=True, blank=True)
    kategori=models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.isim
    

    
    
