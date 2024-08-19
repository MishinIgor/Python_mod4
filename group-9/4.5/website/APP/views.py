from django.shortcuts import render

def main_page(request):
    fraza = 'Привет, мир!'
    return render(request, 'main_page.html', {'fraza': fraza})

def contacts(request):
    return render(request, 'contacts.html')

def about_us(request):
    return render(request, 'about_us.html')

def my_view(request):
    return render(request, "my_template.html")

def products(request):
    products = [("Банан",125),("Аппельсин",-32)]
    return render(request, 'products.html', {'products': products[1][0]})

