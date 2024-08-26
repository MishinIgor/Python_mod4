from django.shortcuts import render,redirect
from APP.forms import StudentForm,MyForm,MyPostForm,PersonForm

def index(request):
    student = StudentForm()
    return render(request, "index.html",{'form':student})

def my_form_view(request):
    return render(request,'my_form.html')

def search_view(request):
    if request.method=='GET':
        form = MyForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            #Делаем что-то с запросом
            #В этом примере просто передадим его в шаблон
            return render(request,'search_results.html',{'query':query})
    else:
        form = MyForm()
    return render(request, 'search_form.html', {'form':form})

def my_post_form(request):
    if request.method == 'POST':
        form = MyPostForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            return render(request, 'success.html', {'name': name, 'email': email})
    else:
        form = MyPostForm()
    return render(request,'my_post_form.html',{'form':form})
    
def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = PersonForm()
    return render(request, 'person_form.html', {'form':form})

def success_view(request):
    return render(request, 'person_success.html')