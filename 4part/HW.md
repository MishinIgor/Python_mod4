# Домашнее задание

# Задача 1

Создайте таблицу, включающую заголовки столбцов "Название", "Жанр", "Год выхода" и несколько строк данных.\
Оформите таблицу с помощью CSS, задав цвет фона, цвет текста, размеры элементов, отступы и выравнивание.

# Решение

`index.html`
```html
<!DOCTYPE html>
<html lang="en"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flexbox Example</title>
    <link href="style.css" rel="stylesheet">
</head>
<body>
    <table>
        <thead>
        <tr>
            <th>Название</th>
            <th>Жанр</th>
            <th>Год выхода</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>Титаник</td>
            <td>драма, романтика</td>
            <td>1997</td>
        </tr>
        <tr>
            <td>Звездные войны: Эпизод IV - Новая надежда</td>
            <td>фантастика, боевик</td>
            <td>1977</td>
        </tr>
        <tr>
            <td>Властелин колец: Братство кольца</td>
            <td>фэнтези, приключения</td>
            <td>2001</td>
        </tr>
        </tbody>
    </table>

</body>
</html>
```

`style.css`
```css
table {
  width: 100%;
  border-collapse: collapse;
  background-color: #f2f2f2;
}

th, td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #4CAF50;
  color: white;
}

```

# Задача 2

Создайте таблицу, включающую заголовки столбцов "Имя", "Фамилия", "Возраст" и несколько строк данных. \
Оформите таблицу с помощью CSS, задав цвет фона, цвет текста, размеры элементов, отступы и выравнивание.

# Решение

`index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flexbox Example</title>
    <link href="style.css" rel="stylesheet">
</head>
<body>
    <table>
        <thead>
        <tr>
            <th>Имя</th>
            <th>Фамилия</th>
            <th>Возраст</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>Иван</td>
            <td>Иванов</td>
            <td>25</td>
        </tr>
        <tr>
            <td>Петр</td>
            <td>Петров</td>
            <td>30</td>
        </tr>
        <tr>
            <td>Сидор</td>
            <td>Сидоров</td>
            <td>35</td>
        </tr>
        </tbody>
    </table>

</body>
</html>
```

`style.css`
```css
table {
  border-collapse: collapse;
  width: 100%;
  margin: 20px 0;
  font-size: 16px;
  color: #333;
  text-align: center;
}

th, td {
  padding: 10px;
  border: 1px solid #ccc;
}

th {
  background-color: #f2f2f2;
  font-weight: bold;
}

tbody tr:nth-child(odd) {
  background-color: #f2f2f2;
}

```

# Задача 3

Оформите HTML форму для связи с пользователем, включающую поля для ввода имени, адреса электронной почты, пола и сообщения.\
Оформите форму с помощью CSS, задав цвет фона, цвет текста, размеры элементов, отступы и выравнивание.

# Решение

`index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flexbox Example</title>
    <link href="style.css" rel="stylesheet">
</head>
<body>
<form>
    <label for="name">Имя:</label>
    <input type="text" id="name" name="name"><br>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br>

    <label for="gender">Пол:</label>
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">Мужской</label>
    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Женский</label><br>

    <label for="message">Сообщение:</label>
    <textarea id="message" name="message"></textarea><br>

    <input type="submit" value="Отправить">
</form>

</body>
</html>
```

`style.css`
```css
form {
  background-color: #f2f2f2;
  padding: 20px;
  border-radius: 5px;
  margin: 20px auto;
  max-width: 500px;
  text-align: center;
}

label {
  display: inline-block;
  width: 100px;
  margin-bottom: 10px;
  text-align: left;
  font-weight: bold;
}

input[type="text"],
input[type="email"],
textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-bottom: 20px;
}

input[type="radio"] {
  display: inline-block;
  margin-right: 10px;
}

input[type="submit"] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

input[type="submit"]:hover {
  background-color: #3e8e41;
}

textarea {
  height: 200px;
}

```

# Задача 4

Создание навигационного меню с использованием списка
Необходимо создать навигационное меню с использованием списка `<ul>` и `<li>`.\
Меню должно содержать несколько пунктов, каждый из которых является ссылкой на другую страницу.\
Необходимо оформить меню с помощью CSS, задав цвет фона, цвет текста, размеры элементов, отступы и выравнивание.

# Решение

`index.html`
```html
<!DOCTYPE html>
<html lang="en"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Навигационное меню</title>
    <link href="style.css" rel="stylesheet">
</head>
<body>
    <nav>
        <ul>
            <li><a href="#">Главная</a></li>
            <li><a href="#">О нас</a></li>
            <li><a href="#">Контакты</a></li>
        </ul>
</nav>
</body>
</html>
```

`style.css`
```css
nav {
    background-color: #333;
    overflow: hidden;
    padding: 10px;
}

nav ul {
    margin: 0;
    padding: 0;
    list-style: none;
    display: flex;
    justify-content: space-between;
}

nav li a {
    display: block;
    color: #fff;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    background-color: #333;
    transition: background-color 0.5s ease;
}

nav li a:hover {
    background-color: #666;
}

```