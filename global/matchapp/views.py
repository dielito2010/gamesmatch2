#from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import redirect, render
#from django.contrib.auth.decorators import login_required
from matchapp.models import Perfil
#from matchapp.forms import PerfilForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'home.html')

def cadastro(request):
    return render(request, 'home.html')

def perfil(request):
    perfil = Perfil.objects.all()

    context = {
        'perfil' : perfil
    }
    return render(request, 'perfil.html', context)

def perfil_add(request):
    return render(request, 'perfil_add.html')

#@login_required
#def perfil_add(request):
#    form = PerfilForm()
#    if (request.method == 'POST'):
#
#        form = PerfilForm(request.POST)
#
#        if(form.is_valid()):

def perfil_add(request):
    if request.method == "GET":
        return render (request, 'perfil_add.html')
    else:
        nome = request.POST.get('nome')
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
    
    perfil = Perfil.objects.filter(cpf=cpf).first()
    if perfil:
        messages.info(request, 'Esse CPF já está cadastrado no GamesMatch!')
        return redirect('perfil_add')
    else:
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