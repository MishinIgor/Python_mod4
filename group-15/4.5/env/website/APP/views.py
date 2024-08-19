from django.shortcuts import render

def my_view(request):
    my_varriable = 'Привет, мир!'
    return render(request, "my_template.html", {'my_variable': my_varriable})

def contacts(request):
    return render(request, 'contacts.html')

def products(request):
    return render(request, 'products.html')

def about_us(request):
    return render(request, 'about_us.html')

def main_page(request):
    return render(request, 'home.html')