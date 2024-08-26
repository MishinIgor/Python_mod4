from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import MyForm

def index(request):
    return render(request,'index.html')

def postuser(request):
    #Получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Underfined")
    age = request.POST.get("age",1)
    return HttpResponse(f"<h2>Name: {name} Age: {age}</h2>")

def search_view(request):
    if request.method == 'GET':
        form = MyForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Делаем что-то с запросом
            # В этом примере просто передадим его в шаблон
            return render(request, 'search_results.html', {'query': query})
    else:
        form = MyForm()
    return render(request, 'search_form.html', {'form': form})