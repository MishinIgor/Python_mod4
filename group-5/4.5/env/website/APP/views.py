from django.shortcuts import render


def main_page(request):
    a = 17
    if a % 2 == 0: 
        my_varriable = 'Привет, мир!'
    else:
        my_varriable = 'И зачем всё это нужно :*( '
    return render(request, "main_page.html",{'my_variable': my_varriable})

def about(request):
    return render(request, "about_us.html")
 
def contacts(request):
    return render(request, "contacts.html")

def my_view(request):
    return render(request, "my_template.html")

def products(request):
    return render(request, 'products.html')