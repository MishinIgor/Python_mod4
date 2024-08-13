_______________
_______________

# Задача 1

Необходимо создать навигационное меню на HTML-странице с использованием списка `<ul>` и `<li>`.

# Решение

```html
<nav>
  <ul>
    <li><a href="#">Главная</a></li>
    <li><a href="#">О нас</a></li>
    <li><a href="#">Услуги</a></li>
    <li><a href="#">Контакты</a></li>
  </ul>
</nav>

```

# Задача 2

Необходимо оформить навигационное меню с помощью CSS, задав цвет фона, цвет текста, размеры элементов, отступы и выравнивание.

# Решение

```css
nav {
  background-color: #333;
  font-family: Arial, sans-serif;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover {
  background-color: #111;
}

```

# Задача 3

Необходимо создать таблицу на HTML-странице, включающую заголовки столбцов и несколько строк данных.

# Решение

```html
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

```

# Задача 4

Необходимо оформить таблицу с помощью CSS, задав цвет фона, цвет текста, размеры элементов, отступы и выравнивание.

# Решение

```css
table {
  border-collapse: collapse;
  width: 100%;
  font-family: Arial, sans-serif;
}

th, td {
  text-align: left;
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #4CAF50;
  color: white;
}

```