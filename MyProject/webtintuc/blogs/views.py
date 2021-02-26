from django.shortcuts import render
from django.http import HttpResponse
from .models import theloai
from .models import baiviet

# Create your views here.

def tatcabaiviet(request):
    list_theloai= theloai.objects.all()
    list_tatcabaiviet = baiviet.objects.all().order_by('-ngay')
    context = {"danhsachmenu": list_theloai, "danhsachbaiviet": list_tatcabaiviet}
    return render(request, "blogs/baivietchinh.html", context)


def baivietcuthe(request, baiviet_id):
    list_theloai = theloai.objects.all()
    q = baiviet.objects.get( pk= baiviet_id )
    context = {"danhsachmenu": list_theloai, "baiviet": q}
    return render(request, "blogs/baivietcuthe.html", context)

def baiviettheloai(request, theloai_id):
    list_theloai = theloai.objects.all()
    q = theloai.objects.get( pk= theloai_id )
    context = {"danhsachmenu": list_theloai, "qs": q}
    return render(request, "blogs/baiviettheloai.html", context)

def lienhe(request):
    list_theloai = theloai.objects.all()
    context = {"danhsachmenu": list_theloai}
    return render(request, "blogs/lienhe.html", context)