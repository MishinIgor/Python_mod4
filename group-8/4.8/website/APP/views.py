from django.shortcuts import render,redirect
from APP.forms import * 

def add_page(request):
    if request.method == "POST":
        form = ProductPostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None,'Ошибка заполнения формы')
    else:
        form = ProductPostForm()    
    return render(request, 'add.html', {'form':form})