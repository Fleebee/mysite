from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("brands/", views.brands, name="brands"),
    path("colours/", views.colours, name="colours"),
    path(
        "car_detail/<int:car_id>",
        views.car_detail,
        name="car_detail",
    ),
    path("car/create/", views.create_car, name="create_car"),
    path(
        "car/delete/<int:car_id>/", views.confirm_delete_car, name="confirm_delete_car"
    ),
    path(
        "car/delete_car/<int:car_id>/", views.delete_car, name="delete_car"
    ),
    path("brand/create/", views.create_brand, name="create_brand"),
    
]
