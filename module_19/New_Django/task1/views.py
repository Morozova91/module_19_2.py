# Задача "Время объединять", все данные из task4 модуля urbanProject
# все представления
# представления из task5

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post, Game, Buyer
from .forms import UserRegister

#

# Create your views here.
def post_page(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return  render(request, 'post_page.html', {'page_obj': page_obj})
def platform(request):
    return render(request, 'platform.html')

def cart(request):
    return render(request, 'cart.html')

def menu(request):
    games = Game.objects.all()

    return render(request, 'games.html', {'games':games})
#
#
#
# # Create your views here.
def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                Buyer.objects.create(name=username, balance=800.0, age=age)
                return HttpResponse(f"Приветствуем, {username}!")
            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'



    return render(request, 'registration_page.html', info)


