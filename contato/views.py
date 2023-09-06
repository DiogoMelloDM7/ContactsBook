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
        
        
    if 'edit' in request.POST:
        for contato in contatos:
            id = contato.id
            nome = request.POST.get(f'nome{id}')
            numero = request.POST.get(f'numero{id}')
            email = request.POST.get(f'email{id}')
            contato.nome = nome
            contato.telefone = numero
            contato.email = email
            contato.save()

            
    return render(request, 'homepage.html', context)




def excluirContato(request, contato_id):
    if request.method == "DELETE":
        contato = get_object_or_404(Contato, id=contato_id)
        contato.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})