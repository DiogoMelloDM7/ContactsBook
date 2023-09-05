from django.shortcuts import render
from .models import Contato
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def homepage(request):

    contatos = Contato.objects.all()
    context = {'contatos': contatos}

    if 'add' in request.POST:
        nome = request.POST.get('nome')
        numero = request.POST.get('numero')
        email = request.POST.get('email')
        if Contato.objects.filter(nome=nome, telefone=numero, email=email).exists():
            return render(request, 'homepage.html', context)
        Contato.objects.create(telefone=numero, nome=nome, email=email)
        
        
    for contato_individual in contatos:

        if f'edit{contato_individual.id}' in request.POST:
            id = contato_individual.id
            nome = request.POST.get(f'nome{id}')
            numero = request.POST.get(f'numero{id}')
            email = request.POST.get(f'email{id}')
            contato = Contato.objects.get(id=id)
            contato.nome = nome
            contato.telefone = numero
            contato.email = email
            print(nome, numero, email)
            contato.save()
            return render(request, 'homepage.html', context)
            
        if f'delete{contato_individual.id}' in request.POST:
            id = contato_individual.id
            contato = Contato.objects.get(id=id)
            contato.delete()
            return render(request, 'homepage.html', context)
    
    
    return render(request, 'homepage.html', context)


