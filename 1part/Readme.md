# ООсновы языка HTML, структура и элементы веб-страницы, основные атрибуты. Синтаксис языка CSS.

HTML (HyperText Markup Language) и CSS (Cascading Style Sheets) – это основы веб-разработки. \
HTML является языком разметки, используемым для создания веб-страниц, а CSS определяет стиль и внешний вид этих страниц.

## Базовая структура HTML-документа:

```
<!DOCTYPE html> - объявляет тип документа, используемый для веб-страницы
<html> - начало HTML-документа
<head> - секция, содержащая метаданные о документе, например, заголовки и ссылки на внешние файлы
<title> - задает заголовок документа, который отображается в строке заголовка браузера
<body> - содержит основное содержимое документа, такое как текст, изображения и другие элементы
```

## Пример кода HTML-документа:

```html
<!-- объявление типа документа HTML -->
<!DOCTYPE html>
<!-- начало html-документа -->
<html>
<!-- элемент, содержащий информацию о документе, которая не отображается в браузере -->
<head>
    <!-- задает кодировку символов документа -->
    <meta charset="UTF-8">
    <!-- задает заголовок документа, который отображается во вкладке браузера -->
    <title>Моя веб-страница</title>
    <!-- подключает файл стилей style.css, расположенный в том же каталоге, что и html-документ -->
    <link rel="Stylesheet" type="text/css" href="style.css">
</head>
<!-- начало тела html-документа -->
<body>
<!-- Создание элемента заголовка сайта с идентификатором "header" -->
<header id="header">
    <h1>Заголовок страницы</h1>
</header>
<!-- Создание элемента основного содержимого сайта с идентификатором "content" -->
<main id="content">
    <section>
        <h2>Основной контент</h2>
        <p>Здесь находится основной контент страницы</p>
    </section>
</main>

<!-- Создание элемента футера сайта с идентификатором "footer" -->
<footer id="footer">
    <p>Копирайт и дополнительная информация</p>
</footer>
</body>
</html>
```

CSS используется для задания стилей для HTML-элементов, таких как цвет, размер и расположение. \
CSS-стили могут быть определены внутри тегов HTML, внутри файла CSS или в отдельных файлах CSS, которые подключаются к HTML-документу с помощью тега <link>.

## Пример кода файла CSS:

```css
#header {
    background-color: #F69E28; /* изменение цвета фона на оранжевый */
    padding: 20px; /* установка внутренних отступов вокруг содержимого */
    text-align: center; /* выравнивание содержимого по центру */
}

#content {
    display: flex; /* установка контейнера флексбоксом */
    flex-wrap: wrap; /* разрешение переноса элементов внутри контейнера */
}

#content section {
    width: 100%; /* задание ширины секции контента на 100% */
    background-color: #7B4AF3; /* изменение цвета фона на темно-фиолетовый */
    padding: 20px; /* установка внутренних отступов вокруг содержимого */
}


#footer {
    background-color: #FE6B64; /* изменение цвета фона на красный */
    padding: 20px; /* установка внутренних отступов вокруг содержимого */
    text-align: center; /* выравнивание содержимого по центру */
}

h1 {
    color: blue; /* изменение цвета текста на синий */
    font-size: 24px; /* задание размера шрифта */
}

```

Определены стили для элементов заголовка (#header), основного контента (#content), секции контента (#content section), подвала (#footer) и заголовков первого уровня (h1).

Стили для заголовка (#header) включают изменение цвета фона на оранжевый, установку внутренних отступов и выравнивание содержимого по центру.

Стили для контейнера основного контента (#content) включают установку контейнера флексбоксом и разрешение переноса элементов внутри контейнера.

Стили для секции контента (#content section) включают задание ширины секции контента на 100%, изменение цвета фона на темно-фиолетовый и установку внутренних отступов вокруг содержимого.

Стили для подвала (#footer) включают изменение цвета фона на красный, установку внутренних отступов и выравнивание содержимого по центру.

Стили для заголовков первого уровня (h1) включают изменение цвета текста на синий и задание размера шрифта.

Это один из способов использования CSS для изменения стилей элементов на веб-странице. \
CSS (Cascading Style Sheets) - это язык стилей, который используется для определения внешнего вида элементов HTML на веб-странице.\
Он позволяет разделять описание стилей и разметки, что делает код более читаемым и легко поддерживаемым.

Другие примеры использования CSS могут включать выбор и изменение цвета фона, шрифта, размера и расположения элементов, использование изображений в качестве фона, создание анимаций и многое другое.

Чтобы добавить CSS к HTML-странице, вы можете использовать тег `<style>`, который должен находиться внутри блока `<head>`:

```html

<!DOCTYPE html>
<html>
<head>
    <title>Моя страница</title>
    <style>
        /* Ваши стили здесь */
    </style>
</head>
<body>
    <!-- Остальной код здесь -->
</body>
</html>

```


Вы также можете использовать внешний файл CSS, который будет содержать все ваши стили.\
Чтобы подключить внешний файл CSS, вы можете использовать тег <link>, который также должен находиться внутри блока <head>:
```html

<!DOCTYPE html>
<html>
<head>
    <title>Моя страница</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <!-- Остальной код здесь -->
</body>
</html>

```
В этом примере мы используем атрибут href, чтобы указать путь к файлу CSS. Это означает, что все стили будут загружены из внешнего файла style.css.

CSS является мощным инструментом для изменения внешнего вида элементов на веб-странице, и его использование может значительно упростить разработку и поддержку веб-сайтов.


#### Создадим HTML-страницу, включающую заголовок, текст и изображение.

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Моя страница</title>
</head>
<body>
	<h1>Добро пожаловать на мою страницу</h1>
	<p>Здесь вы найдете много интересного контента.</p>
	<img src="myimage.jpg" alt="Мое изображение">
</body>
</html>

```
#### Оформим страницу с помощью CSS, задав цвет фона, цвет текста, размеры элементов, отступы и выравнивание.

```css
body {
	background-color: #f7f7f7; /* цвет фона страницы */
	color: #333; /* цвет текста на странице */
	font-family: Arial, sans-serif; /* шрифт */
	font-size: 16px; /* размер шрифта */
	margin: 0; /* удаление отступов */
	padding: 20px; /* внутренний отступ страницы */
}

h1 {
	font-size: 36px; /* размер заголовка */
	text-align: center; /* выравнивание по центру */
	margin-top: 0; /* удаление верхнего отступа */
}

p {
	line-height: 1.5; /* межстрочный интервал */
}

img {
	max-width: 100%; /* максимальная ширина изображения */
	height: auto; /* сохранение пропорций изображения */
	display: block; /* удаление отступов вокруг изображения */
	margin: 20px auto; /* выравнивание изображения по центру */
}

```

#### Создадим форму на HTML-странице, включающую текстовые поля, радиокнопки и кнопку отправки.

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Моя форма</title>
</head>
<body>
	<h1>Заполните форму</h1>
	<form>
		<label for="name">Имя:</label>
		<input type="text" id="name" name="name"><br>

		<label for="email">Email:</label>
		<input type="email" id="email" name="email"><br>

		<label for="age">Возраст:</label>
		<input type="number" id="age" name="age"><br>

		<p>Выберите свой пол:</p>
		<label for="male">Мужской</label>
		<input type="radio" id="male" name="gender" value="male">
		<label for="female">Женский</label>
		<input type="radio" id="female" name="gender" value="female"><br>

		<label for="message">Сообщение:</label>
		<textarea id="message" name="message"></textarea><br>

		<input type="submit" value="Отправить">
	</form>
</body>
</html>

```

#### Чтобы оформить форму с помощью CSS, можно использовать селекторы для каждого элемента формы и задавать стили для них.

```html
<form>
  <label for="name">Имя:</label>
  <input type="text" id="name" name="name">
  <br>
  <label for="email">Email:</label>
  <input type="email" id="email" name="email">
  <br>
  <label for="message">Сообщение:</label>
  <textarea id="message" name="message"></textarea>
  <br>
  <input type="submit" value="Отправить">
</form>

```

```css
form {
  background-color: #eee;
  padding: 20px;
  width: 400px;
  margin: 0 auto;
}

label {
  display: block;
  margin-bottom: 10px;
  font-weight: bold;
}

input[type="text"],
input[type="email"],
textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border-radius: 5px;
  border: none;
  background-color: #fff;
  font-size: 16px;
}

input[type="submit"] {
  background-color: #428bca;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
  font-size: 16px;
  cursor: pointer;
}

input[type="submit"]:hover {
  background-color: #3071a9;
}

```

Мы задали общие стили для формы, такие как цвет фона, отступы, ширину и центрирование. \
Затем мы задали стили для каждого элемента формы: метки (label), текстовые поля `(input[type="text"] и textarea)` и кнопку отправки `(input[type="submit"])`. \
Мы задали ширину, отступы, радиус скругления углов, цвет фона, размер шрифта и другие стили для каждого элемента. \
Мы задали стили для наведения курсора на кнопку отправки.

_______________
_______________

# Домашнее задание

# Задача 1 

Необходимо создать навигационное меню на HTML-странице с использованием списка `<ul>` и `<li>`.

# Задача 2

Необходимо оформить навигационное меню с помощью CSS, задав цвет фона, цвет текста, размеры элементов, отступы и выравнивание.


# Задача 3

Необходимо создать таблицу на HTML-странице, включающую заголовки столбцов и несколько строк данных.

# Задача 4

Необходимо оформить таблицу с помощью CSS, задав цвет фона, цвет текста, размеры элементов, отступы и выравнивание.