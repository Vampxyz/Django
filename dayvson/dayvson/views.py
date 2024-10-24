from django.http import HttpResponse , JsonResponse


loja_biu = [
    {
        
        'id' : "TFDkmbik185596djg",
        'nome' : "  Bicicleta do biu",
        'preço ': 'R$ 100,00',
        'estoque': 20
    },
    
    {
        'id' : "GHJKkvgor5949fg2r6g",
        'nome' : "  camisas do biu",
        'preço ': 'R$ 50,00',
        'estoque': 50
    },
    {
        'id' : "KJTCY15296dg141er98",
        'nome' : "  boné do biu",
        'preço ': 'R$ 20,00',
        'estoque': 62
    },
    {
        'id' : "OIIHUJ626266fr5gr96b2r",
        'nome' : "  bermuda do biu",
        'preço': 'R$ 86,00',
        'estoque': 200
    }
   
]
    
def id_produto(request,id,):
    for id_produto in loja_biu:
        if id_produto['id'] == id:
            return JsonResponse(id_produto)
    
def biu(request):
    return HttpResponse("BORA BIUUUUUUU")

    

def saudacao(request,name):   
    return  HttpResponse(f"olá, {name} ! Caso Você não saiba seu nome contém {len(name)} caracteres")
        