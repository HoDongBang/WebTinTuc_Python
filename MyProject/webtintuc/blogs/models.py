from django.db import models

# Create your models here.
class theloai(models.Model):
    tentheloai = models.CharField(max_length=50)

class baiviet(models.Model):
    matheloai = models.ForeignKey(theloai, on_delete=models.CASCADE)
    tenbaiviet = models.CharField(max_length=200)
    noidung = models.TextField()
    ngay = models.DateTimeField(auto_now_add=True)
    hinh = models.ImageField(null=True)