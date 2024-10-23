from django.http import HttpResponse, JsonResponse

def greetings(request):
    return HttpResponse("Hello world!")

def personal_data(request):
    return JsonResponse({
        'Name': 'Ryhan',
        'Email': 'ryhannalbert@gmail.com'
    })