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
        {'title': 'История поездок', 'url_name': 'history_trips'}
        ]


def login_and_register(request):
    context = {'title': 'Вход и регистрация'}
    return render(request=request, template_name='maitaxi/login_and_register.html', context=context)


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


# def home(request):
#    context = {'title': 'Главная', 'menu': menu}
#    return render(request, 'maitaxi/home.html', context=context)


def home(request):

    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            taxi_order = form.save(commit=False)
            taxi_order.passenger = request.user  # Привязываем заказ к текущему пользователю
            taxi_order.driver = Driver.objects.filter(id=1).first()
            taxi_order.price = 565
            taxi_order.save()
            return redirect('info_order')  # Перенаправляем пользователя на страницу успеха
    else:
        form = TripForm()
    return render(request, 'maitaxi/home.html', {'title': 'Главная - заказ такси', 'form': form, 'menu': menu})


def about(request):
    context = {'title': 'О сайте', 'menu': menu}
    return render(request, 'maitaxi/about.html', context=context)


def profile(request):
    context = {'title': 'Профиль', 'menu': menu}
    return render(request, 'maitaxi/profile.html', context=context)


def info_order(request):
    order = Trip.objects.filter(passenger=request.user).order_by('-order_time').first()  # передаем заказ в ордер
    context = {'title': 'Информация о заказе',
               'menu': menu,
               'order': order}
    return render(request, 'maitaxi/info_order.html', context=context)


def history_trips(request):
    orders = Trip.objects.filter(passenger=request.user).order_by('-order_time')
    context = {'title': 'История поездок',
               'menu': menu,
               'orders': orders}
    return render(request, 'maitaxi/history_trips.html', context=context)
