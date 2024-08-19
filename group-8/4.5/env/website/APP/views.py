from django.shortcuts import render

def contacts(request):
    return render(request, 'contacts.html')

def about_us(request):
    return render(request, 'aboutus.html')

def main_page(request):
    return render(request, 'home.html')