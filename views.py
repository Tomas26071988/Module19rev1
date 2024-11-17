from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game

def home(request):
    games = ['Atomic Heart', 'Cyberpunk 2077']
    return render(request, 'fourth_task/home.html', {'games': games})

def shop(request):
    items = Game.objects.all()
    return render(request, 'fourth_task/shop.html', {'items': items})

def cart(request):
    return render(request, 'fourth_task/cart.html')

# Псевдо-список пользователей
users = ["user1", "user2", "user3"]

def sign_up_by_django(request):
    return sign_up_handler(request)


def sign_up_by_html(request):
    return sign_up_handler(request)


def sign_up_handler(request):
    info = {}
    form = UserRegister()

    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Логика проверки
            if Buyer.objects.filter(username=username).exists():
                info['error'] = 'Пользователь уже существует'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            else:
                # Если все проверки пройдены
                Buyer.objects.create(username=username, password=password, age=age)
                return render(request, 'fifth_task/registration_page.html',
                              {'info': {'message': f'Приветствуем, {username}!'}})

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', {'info': info})


# Create your views here.
