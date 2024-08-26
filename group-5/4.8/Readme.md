<h1> Формы в Django </h1>

Веб-формы — это страницы, которые пользователи запрашивают с помощью браузера. Эти страницы могут быть написаны с помощью сочетания HTML, клиентского скрипта, серверных элементов управления и серверного кода. Когда пользователи запрашивают страницу, она компилируется и выполняется на сервере платформой, а затем платформа создает HTML-разметку, которую может отобразить браузер.


Django предоставляет класс Form, который используется для создания HTML-форм. Он описывает форму, ее работу и внешний вид. Он похож на класс ModelForm, который создает форму с помощью модели, но не требует определенной модели.

Каждое поле карты класса Form соответствует элементу HTML-формы < input >, и каждое из них является самим классом, он управляет данными формы и выполняет проверку при отправке формы.

Давайте посмотрим на пример, в котором мы тоже создаем несколько полей.

```py
from django import forms 
class StudentForm(forms.Form): 
    firstname = forms.CharField(label="Enter first name",max_length=50) 
    lastname  = forms.CharField(label="Enter last name", max_length = 100) 
```

Создается StudentForm, содержащий два поля типа CharField.<br> Charfield – это класс, который используется для создания компонента ввода текста HTML в форме.

Метка используется для установки HTML-метки компонента, а max_length устанавливает длину входного значения.

При рендеринге он выводит в браузер следующий HTML-код.

```html
<label for="id_firstname">Enter first name:</label> 
<input type="text" name="firstname" required maxlength="50" id="id_firstname" /> 
<label for="id_lastname">Enter last name:</label> <input type="text" name="lastname" required maxlength="100" id="id_lastname" />
```

Примечание. Django Form не включает теги или кнопку отправки. Мы должны сами указать их в шаблоне.

<b> Создание формы в Django </b>

Предположим, мы хотим создать форму для получения информации о студенте, используем для этого следующий код.
```py
from django import forms 
class StudentForm(forms.Form): 
    firstname = forms.CharField(label="Enter first name",max_length=50) 
    lastname  = forms.CharField(label="Enter last name", max_length = 100) 
```
Поместите этот код в файл forms.py.

Создание экземпляра формы в Django

Теперь нам нужно создать экземпляр формы в файле views.py. (См. приведенный ниже код).

```py
#views.py

from django.shortcuts import render 
from APP.form import StudentForm 
 
def index(request): 
    student = StudentForm() 
    return render(request,"index.html",{'form':student})
```
Передача контекста формы в шаблон индекса, который выглядит следующим образом:
// index.html
```html
<!DOCTYPE html> 
<html lang="en"> 
<head> 
<meta charset="UTF-8"> 
<title>Index</title> 
</head> 
<body> 
<form method="POST" class="post-form"> 
{% csrf_token %} 
{{ form.as_p }} 
<button type="submit" class="save btn btn-default">Save</button> 
</form> 
</body> 
</html>   
```
Укажите URL-адрес в urls.py
```py
from django.contrib import admin 
from django.urls import path 
from APP import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('index/', views.index), 
] 
```
Однако есть и другие варианты вывода для пар <label>/< input>:
```django
{{form.as_table}} отобразит их как ячейки таблицы, заключенные в теги <tr>;
{{form.as_p}} отобразит их заключенными в теги <p>;
{{form.as_ul}} также отобразит их заключенными в теги <li>.
```

<h2> Создание простой HTML - формы </h2>

Для создания простой HTML-формы с полями "Имя" и "Номер телефона" и представления (views function) для обработки этой формы с методом GET, следуйте этим шагам:

Шаг 1: Создайте файл my_form.html в директории templates вашего Django-приложения. В этом файле создайте форму:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Простая HTML-форма</title>
</head>
<body>
    <h1>Простая HTML - форма (GET)</h1>
    <form method="get">
        <label for="name">Имя:</label>
        <input type="text" name="name" id="name"> <br> <br>
        <label for="phone">Номер телефона: </label>
        <input type="text" name="phone" id="phone"> <br> <br>

        <input type="submit" value="Отправить">
    </form>
</body>
</html>
```
Шаг 2: Создайте views функцию в файле views.py вашего Django-приложения, которая будет отображать эту форму:
```py
def my_form_view(request):
    return render(request,'my_form.html')
```

Шаг 3: Настройте URL-маршрут в файле urls.py вашего приложения для связи views функции с URL:
```py
path('my_form/',views.my_form_view,name='my_form')
```

<h2> Создание формы с get запросом </h2>

1. Создайте форму

```py
class MyForm(forms.Form):
    query = forms.CharField(label='Search')
```
2. Создайте представление для обработки формы:
```py
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
```

3. Создайте шаблоны для отображения формы и результатов поиска:

```html
<!--search_form.html-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="get">
        {{form}}
        <button type="submit">Search</button>
    </form>
</body>
</html>
```

```html
<!--search_form.html-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Search Results for "{{query}}" </h1>
    <!--Вывод результатов поиска-->
</body>
</html>
```

4. Настройте маршруты URL:
```py
# urls.py
path('search/',views.search_view,namme='search')
```

Теперь у вас есть форма, которая отправляет GET-запрос с данными в URL. Представление обрабатывает этот запрос, извлекает данные из формы, выполняет необходимую обработку и передает результаты в шаблон для отображения.

<h2> Создание формы с Post запросом </h2>
1. Создайте форму:

```py
class MyPostForm(forms.Form):
    name = forms.CharField(label='Ваше имя')
    email = forms.EmailField(label='Ваш email')
```
2. Создайте представление для обработки формы
```py
#views.py
def my_post_form(request):
    if request.method == 'POST':
        form = MyPostForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            return render(request, 'success.html', {'name': name, 'email': email})
    else:
        return render(request,'my_post_form.html',{'form':form})
```

3. Создайте шаблоны для отображения формы и сообщения об успехе:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Form</title>
</head>
<body>
    <form method="post">
        {%csrf_token%}
        {{form}}
        <button type='submit'>Submit</button>
    </form>
</body>
</html>
```

```html
<!--success.html-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
</head>
<body>
    <h1> Thank you, {{ name }}! </h1>
    <p> Your email ({{email}}) has been successfully submit. </p>
</body>
</html>
```

4. Настройте маршруты URL:

```py
#urls.py
path('form/',views.my_post_form,name='post_form')
```

Теперь у вас есть простая форма, отправляющая POST-запрос. Представление обрабатывает этот запрос, проверяет его на валидность, и в случае успеха выполняет дальнейшие действия (например, сохранение данных) и перенаправляет на страницу успешного завершения.

<h1>Домашнее задание 8.<br>
Тема вебинара: Формы в джанго</h1>

1) Создать модель Person с следующими полями:
* Имя 
* Фамилия
2) Создать форму отправки для модели клиента с записьюданных в базу данных.

<h3> Решение </h3>

```py
#models.py
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

```py
#forms.py
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']
```

```py
from django.shortcuts import render,redirect
from APP.forms import PersonForm

def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = PersonForm()
    return render(request, 'person_form.html', {'form':form})

def succuss_view(request):
    return render(request, 'success.html')
```

```py
#urls.py
path('create/',views.create_person,name='create_person'),
path('success',views.succuss_view, name='success_url'),
```
