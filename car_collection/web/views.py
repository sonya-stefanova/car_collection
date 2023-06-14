from car_collection.web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, CarCreateForm, CarEditForm, \
    CarDeleteForm
from car_collection.web.models import Profile, Car
from django.shortcuts import render, redirect


# Create your views here.
def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

def show_home(request):
    profile = get_profile()
    if profile is None:
        return redirect('create profile')

    context = {
        'profile': profile,
    }

    return render(request, template_name='index.html', context=context)
def show_catalogue(request):
    cars = Car.objects.all()

    total_cars = cars.count()
    profile = get_profile()

    context = {
        'profile': profile,
        'cars': cars,
        'total_cars': total_cars,

    }
    return render(request, 'catalogue.html', context=context)

def create_profile(request):
    profile = get_profile()
    if profile is not None:
        return redirect('index')

    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileCreateForm()


    context = {
        'form': form,
        'no profile': True,
    }

    return render(request, 'profile-create.html', context)

def details_profile(request):
    profile = Profile.objects.get()
    cars = Car.objects.all()
    total_price_all_cars = sum(car.price for car in cars)

    context = {
        'profile': profile,
        'total_price_cars': total_price_all_cars,
    }
    return render(request, 'profile-details.html', context)
def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            return redirect('details profile')

    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile-edit.html', context)

def delete_profile(request):
    profile = get_profile()
    cars = Car.objects.all()
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
def create_car(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CarCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('catalogue')
    else:
        form = CarCreateForm()

    context = {
        'form': form,
        'profile':profile,
    }
    return render(request, 'car-create.html', context)
def details_car(request, pk):
    profile = get_profile()
    car = Car.objects.filter(pk=pk).\
        get()
    context = {
        'car': car,
        'profile':profile,
    }
    return render(request, 'car-details.html', context)
def edit_car(request,pk):
    profile = get_profile()
    car = Car.objects.\
        filter(pk=pk).\
        get()

    if request.method == 'POST':
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid:
            form.save()
            return redirect('catalogue')
    else:
        form = CarEditForm(instance=car)

    context = {
        'form': form,
        'profile':profile,
    }
    return render(request, 'car-edit.html', context=context)
def delete_car(request, pk):
    profile = get_profile()
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')
    else:
        form = CarDeleteForm(instance=car)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'car-delete.html', context)