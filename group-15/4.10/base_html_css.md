# Правила и принципы структурирования HTML документа.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Простой веб сайт</title>
    <link rel="Stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div id="frame">
        <div id="header">=-)</div>
        <div id="menu">
            <a href="">Главная страница</a>
            <a href="">Предметы</a>
            <a href="">Контакты</a>
        </div>

        <div id="inMenu">
            <a href="">Программирование</a>
            <ul>
                <li>el1</li>
                <li>el2</li>
            </ul>
            <a href="">Физика</a>
            <a href="">Математика</a>
        </div>

        <div id="content">Контент (Содержимое страницы)</div>
        <div id="sidebar">Сайдбар (боковая панель)</div>
        <div id="footer">q10sn1k</div>
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
    display: table-footer-group;
    width: 950px;
    height: 50px;
    background-color: darkgreen;
    margin: auto;
    padding: 20px;
    text-align: center;
}
#content
{
    width: 500px;
    height: 500px;
    background-color: yellow;
    margin: 25px;
    float: left;
}
#sidebar
{
    width: 200px;
    height: 200px;
    background-color: yellowgreen;
    margin: 15px;
    float: right;
}
#menu
{
    background: yellowgreen;
    padding: 10px;
    margin: 10px;
    color: black;
    font-size: 20px;
    font-family: "Arial Black";
    text-align: center;
}
#inMenu
{
    float: left;
    background: yellowgreen;
    margin: 10px;
    margin-top: 25px;
    font-size: 20px;
    font-family: "Comic Sans MS";
    text-align: center;
}
#inMenu a
{
    display: block;
}

```
