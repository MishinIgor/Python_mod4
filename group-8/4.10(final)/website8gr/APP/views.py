from django.shortcuts import render
from .forms import ClientForm
def main_page(request):
    if request.method == "POST":
        form = ClientForm
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None,'Ошибка заполнения формы')
    else:
        form = ClientForm()
        
    return render(request, 'main.html', {'form':form})