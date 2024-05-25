from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import *
from .models import *


menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Профиль', 'url_name': 'profile'},
        {'title': 'История поездок', 'url_name': 'history_trips'}]


def login_and_register(request):
    return render(request=request, template_name='maitaxi/login_and_register.html',
                  context={'title': 'Вход и регистрация'})


def logout_user(request):
    logout(request=request)
    return redirect(to='login_and_register')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'maitaxi/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'maitaxi/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def home(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            taxi_order = form.save(commit=False)
            taxi_order.passenger = request.user  # Привязываем заказ к текущему пользователю
            taxi_order.driver = Driver.objects.filter(id=1).first()
            taxi_order.price = 565
            taxi_order.save()
            return redirect(to='info_order')  # Перенаправляем пользователя на страницу успеха
    else:
        form = TripForm()
    return render(request=request, template_name='maitaxi/home.html',
                  context={'title': 'Главная - заказ такси', 'form': form, 'menu': menu})


def about(request):
    return render(request=request, template_name='maitaxi/about.html', context={'title': 'О сайте', 'menu': menu})


def profile(request):
    return render(request=request, template_name='maitaxi/profile.html', context={'title': 'Профиль', 'menu': menu})


def info_order(request):
    order = Trip.objects.filter(passenger=request.user).order_by('-order_time').first()  # передаем заказ в ордер
    return render(request=request, template_name='maitaxi/info_order.html',
                  context={'title': 'Информация о заказе',
                           'menu': menu,
                           'order': order})


def history_trips(request):
    orders = Trip.objects.filter(passenger=request.user).order_by('-order_time')
    return render(request=request, template_name='maitaxi/history_trips.html',
                  context={'title': 'История поездок',
                           'menu': menu,
                           'orders': orders})


def e_handler404(request, exception):
    return render(request=request, template_name='maitaxi/404.html', context={}, status=404)


def e_handler500(request):
    return render(request=request, template_name='maitaxi/500.html', context={}, status=500)


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправить на страницу профиля после сохранения
    else:
        form = ProfileEditForm(instance=request.user)

    return render(request=request, template_name='maitaxi/profile_edit.html',
                  context={'form': form, 'title': 'Редактирование профиля', 'menu': menu})
