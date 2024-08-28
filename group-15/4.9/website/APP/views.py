from django.shortcuts import render
from .forms import ClientForm

def main_page(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None,'Ошибка заполнения формы')
    else:
        form = ClientForm()
    return render(request, 'main.html', {'form':form})

def contacts(request):
    return render(request,'contacts.html')

def aboutus(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error('Ошибка заполнения формы')
    else:
        form = ClientForm()
    return render(request, 'aboutus.html')