from django.shortcuts import render
from .forms import StudentForm

def main_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None,'Ошибка заполнения формы')
    else:
        form = StudentForm()
        
    return render(request, 'main.html', {'form':form})

def pyth(request):
    return render(request, 'python.html')

def js(request):
    return render(request, 'js.html')

def math(request):
    return render(request, 'math.html')