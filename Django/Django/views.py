from django.http import HttpResponse, JsonResponse

product_list = [
    {
        'Id': '021NDawnsaI83JdwlaHJ2',
        'Nome': 'Garrafa Térmica',
        'Preço': 'R$ 19,99',
        'Estoque': 7
    },
    {
        'Id': 'aJKHDawd218ASDjkn12',
        'Nome': 'Garrafa Térmica',
        'Preço': 'R$ 15,00',
        'Estoque': 2
    },
    {
        'Id': '89213JSBD2798heDSAb1',
        'Nome': 'Camisa do bob marley',
        'Preço': 'R$ 150,00',
        'Estoque': 1
    }
]

def greetings(request, name):
    return HttpResponse(f"Ola {name}, Seu nome contém {len(name)} letras")

def products(request):
    return HttpResponse(product_list)

def product(request, id):
    for product in product_list:
        if product["Id"] == id:
            return JsonResponse(product)
            
        
    
    
    