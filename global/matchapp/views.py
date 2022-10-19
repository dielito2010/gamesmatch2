from django.contrib import messages
from django.shortcuts import redirect, render, resolve_url
from django.contrib.auth.decorators import login_required
from matchapp.models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
#from matchapp.forms import PerfilForm

# Create your views here.

def home(request):
    #tipoMatch = request.POST.get('tipoMatch')
    perfil = Perfil.objects.order_by('game1')[0:5]
    context = {
        'tabela' : perfil
    }    
    return render(request, 'home.html', context)
#######################################################################################

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=usuario, password=senha)
        if user:
            login_django(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Usuário ou senha inválidos!')
            #return redirect('login')
            return render(request, 'login.html')
#######################################################################################

@login_required
def logout(request):
    logout_django(request)
    return render(request, 'home.html')
#######################################################################################

@login_required(login_url='/login')
def perfil(request):
    perfil = Perfil.objects.all()[0:12]
    context = {
        'perfis' : perfil
    }
    return render(request, 'perfil.html', context)
#######################################################################################

@login_required(login_url='/login')
def perfil_edit(request):
    return render(request, 'home.html')
#######################################################################################

@login_required(login_url='/login')
def perfil_del(request):
    return render(request, 'home.html')

#######################################################################################

def perfil_add(request):
    if request.method == "GET":
        #usuario = request
        #user = authenticate(username=usuario)
        #if this.is_authenticated:
        #   messages.info(request, 'Precisa fazer logout/sair para criar outro perfil')
        return render (request, 'perfil_add.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cpf = request.POST.get('cpf')
        game1 = request.POST.get('game1')
        pontuacao1 = request.POST.get('pontuacao1')
        game2 = request.POST.get('game2')
        pontuacao2 = request.POST.get('pontuacao2')
        dat_nasc = request.POST.get('dat_nasc')
        nickname = request.POST.get('nickname')
        image = request.POST.get('image')
        cep = request.POST.get('cep')
        endereco = request.POST.get('endereco')
        zone = request.POST.get('zone')
        if cpf=='' or nome=='' or game1=='' or pontuacao1=='' or dat_nasc=='' or nickname=='' or zone=='' or email=='' or senha=='':
            messages.info(request, 'Campos obrigatórios não foram preenchidos!')
            return redirect('perfil_add')
        if pontuacao2=='':
            pontuacao2=0
        if cep=='':
            cep=0
    perfil = Perfil.objects.filter(cpf=cpf).first()
    if perfil:
        messages.info(request, 'Esse CPF já está cadastrado no GamesMatch!')
        return redirect('perfil_add')
    else:
        user = User.objects.create_user(
            first_name = nome,
            email = email,
            username = nickname,
            password = senha
        )
        user.save()
        perfil = Perfil(
            nome = nome,
            cpf = cpf,
            game1 = game1,
            pontuacao1 = pontuacao1,
            game2 = game2,
            pontuacao2 = pontuacao2,
            dat_nasc = dat_nasc,
            nickname = nickname,
            image = image,
            cep = cep,
            endereco = endereco,
            zone = zone
        )
        perfil.save()
        #messages.info(request, 'Perfil cadastrado com sucesso!')
        return redirect('perfil')