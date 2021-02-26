from django.urls import path
from . import views

urlpatterns = [
    path('lienhe/', views.lienhe, name="lienhe"),
    path('theloai/<int:theloai_id>', views.baiviettheloai, name="baiviettheloai"),
    path('baiviet/<int:baiviet_id>', views.baivietcuthe, name="baivietcuthe"),
    path('', views.tatcabaiviet, name="tatcabaiviet"),
]