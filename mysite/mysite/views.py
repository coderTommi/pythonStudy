from django.http import HttpResponse

def first_page(request):
    return HttpResponse('<p> Hello World!</p>')
