# Создание и стилизация веб-страниц, включая различные элементы и компоненты.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>div learn</title>
    <link rel="Stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div id="frame">
        <div id="header">Заголовок сайта</div>
        <div id="content"> Контентная часть сайта </div>
        <div id="sidebar"> Сайдбар (Боковая панель)  </div>
        <div id="footer"> Футер (Нижняя часть сайта) [подвал сайта]</div>
    </div>
</body>
</html>
```

```css
    #frame
    {
        width: 1000px; /* ширина */
        background-color: aqua; /* цвет фона */
        margin: auto; /* Выравнивание по центру */
        display: table; /* Отображение в табличной форме представление в форме таблицы) */
        height: 100%; /* высота */
    }
    #header
    {
        width:940px; /* ширина */
        height: 50px; /* высота */
        background-color: darkorange; /* цвет фона */
        margin: auto; /* Выравнивание по центру */
        margin-top: 10px; /* Отступ от верхней границы сайта */
        padding: 20px; /* внутренний отступ */
        text-align: center; /* Выравнивание текста по центру */
    }
    #footer
    {
        width:940px; /* ширина */
        height: 50px; /* высота */
        background-color: brown; /* цвет фона */
        margin: auto; /* Выравнивание по центру */
        margin-top: 10px; /* Отступ от верхней границы сайта */
        padding: 20px; /* внутренний отступ */
        text-align: center; /* Выравнивание текста по центру */
        display: table-footer-group; /* Представляем как футер (подвал) */
    }
    #content
    {
        height: 900px; /* высота */
        width: 700px; /* ширина */
        background-color: indigo; /* цвет фона */
        float: left; /* выравнивание блока (слева) */
    }
    #sidebar
    {
        background-color: darkgreen; /* цвет фона */
        width:200px; /* ширина */
        height: 700px; /* высота */
        margin: 30px; /* Выравнивание */
        float: right; /* Выравнивание блока (справа) */

    }

```

_______________
_______________

# Домашнее задание

# Задача 

Создайте HTML страницу о вашем любимом фильме. Используйте заголовки для названия фильма и его главных разделов,\
абзацы для описания сюжета и основных персонажей, и изображение для обложки фильма.\
Используйте встроенные CSS стили для изменения цвета текста и фона.
