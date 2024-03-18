from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Count

# Create your views here.


def home(request):

    cars = Car.objects.all()
    context = {"cars": cars}

    return render(request, "home.html", context)


def brands(request):

    brands = Brand.objects.all()
    brands_totals = []

    total_car_count = Car.objects.values("brand_id").annotate(total_cars=Count("id"))

    new_car_count = (
        Car.objects.filter(condition="NEW")
        .values("brand_id")
        .annotate(total_cars=Count("id"))
    )
    new_car_dict = {}
    for i in new_car_count:
        new_car_dict[i["brand_id"]] = i["total_cars"]
    print(new_car_dict)

    used_car_count = (
        Car.objects.filter(condition="USED")
        .values("brand_id")
        .annotate(total_cars=Count("id"))
    )
    used_car_dict = {}
    for i in used_car_count:
        used_car_dict[i["brand_id"]] = i["total_cars"]
    print(used_car_dict)

    for i in total_car_count:
        for brand in brands:
            if brand.id == i["brand_id"]:
                select_id = i["brand_id"]
                data = {
                    "id": brand.id,
                    "name": brand.name,
                    "total_car_count": i["total_cars"],
                    "new_car_count": new_car_dict.get(i["brand_id"], 0),
                    "used_car_count": used_car_dict.get(i["brand_id"], 0),
                }
                brands_totals.append(data)
        print(brands_totals)
    # I could have done the same dict selector for total cars. I realsied this late!

    context = {"brands": brands_totals}

    return render(request, "brands.html", context)


def colours(request):

    colours = Colour.objects.all()
    context = {"colours": colours}

    return render(request, "colours.html", context)


def car_detail(request, car_id):

    car = Car.objects.filter(id=car_id).first()

    previous_owners = Owner.objects.filter(car=car).all()

    context = {"car": car, "previous_owners": previous_owners}

    return render(request, "car_detail.html", context)


def create_car(request, car_id=None):

    if car_id:
        car = get_object_or_404(Car, id=car_id)
    else:
        car = None

    if request.method == "POST":
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    if request.method == "GET":

        form = CreateCarForm(instance=car)

        context = {"car": car, "form": form}

    return render(request, "create_car.html", context)


def confirm_delete_car(request, car_id=None):

    car = get_object_or_404(Car, id=car_id)

    context = {"car": car}

    return render(request, "confirm_delete_car.html", context)


def delete_car(request, car_id):

    car = get_object_or_404(Car, pk=car_id)
    car.delete()
    return redirect("home")


def create_brand(request, brand_id=None):

    if brand_id:
        brand = get_object_or_404(Brand, id=brand_id)
    else:
        brand = None

    if request.method == "POST":
        form = CreateBrandForm(request.Post)
        if form.is_valid():
            form.save()
            return redirect("home")

    if request.method == "GET":

        form = CreateBrandForm(instance=brand)

        context = {"brand": brand, "form": form}

    return render(request, "create_brand.html", context)


