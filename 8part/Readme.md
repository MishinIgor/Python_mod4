# Создание анимаций с помощью HTML и CSS. Создание анимаций на веб-страницах с помощью CSS.

`index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Создание пузырькового эффекта средствами html и css</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="wrapper">
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
</div>
<div class="banner">
    <div class="content">
        <h2>Анимированный <b>Фон</b></h2>
    </div>
</div>
</body>
</html>

```

Мы реализоваи структуру HTML страницы, включая метаданные в заголовке, подключение CSS файла и основной контент внутри тега body.

Первый контейнер div с классом `wrapper` содержит 10 пустых тегов span. Они будут использоваться для создания пузырьков на фоне.

Второй контейнер div с классом `banner` содержит дополнительный контент, который будет размещен на верхней части страницы.

# создадим файл стилей style.css

```css
body{
    background-image: linear-gradient(to top,fuchsia,peachpuff);
    height: 100vh;
}

```

Этот код задает основной фоновый градиент, используя свойство `background-image`. \
Здесь мы используем линейный градиент, идущий от фуксии к светло-желтому оттенку  `peachpuff`. \
`height` задает высоту контейнера в 100% высоты окна.

```css
.wrapper span{
    position: fixed;
    bottom: -50px;
    height: 50px;
    width: 50px;
    border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
    background-color: #fff;
    animation: animate 10s linear infinite;
}

```

Этот блок стилей стилизует пузырьки. \
Мы используем селектор `.wrapper span` для выбора всех тегов `span` внутри контейнера с классом `wrapper.`\
Свойство `position: fixed` фиксирует пузырьки на месте в видимой области окна. \
`bottom: -50px` перемещает пузырьки вниз на 50 пикселей от нижней границы окна. \
`height` и `width` устанавливают размеры пузырьков в 50 пикселей.\
`border-radius` задает скругленные углы для пузырьков, используя значения радиуса для каждой из четырех углов. \
Значения делятся на 2 группы, чтобы определить горизонтальный и вертикальный радиусы.

`background-color: #fff`; задает белый цвет для заполнения пузырьков.

`animation: animate 10s linear infinite;` используется для задания анимации для пузырьков.\
Здесь мы используем название анимации `animate`, которое определено ниже, а также устанавливаем продолжительность в 10 секунд, тип анимации на linear и задаем бесконечный цикл анимации.

```css
.wrapper span:nth-child(1){
    left: 0;
    animation-delay: 0.6s;
}
.wrapper span:nth-child(2){
    left: 10%;
    animation-delay: 3s;
}
.wrapper span:nth-child(3){
    left: 20%;
    animation-delay: 2s;
}
.wrapper span:nth-child(4){
    left: 30%;
    animation-delay: 5s;
}
.wrapper span:nth-child(5){
    left: 40%;
    animation-delay: 1s;
}
.wrapper span:nth-child(6){
    left: 50%;
    animation-delay: 7s;
}
.wrapper span:nth-child(7){
    left: 60%;
    animation-delay: 6s;
}
.wrapper span:nth-child(8){
    left: 70%;
    animation-delay: 8s;
}
.wrapper span:nth-child(9){
    left: 80%;
    animation-delay: 6s;
}
.wrapper span:nth-child(10){
    left: 90%;
    animation-delay: 4s;
}

```

Этот блок стилей определяет расположение и задержку анимации для каждого пузырька, используя селекторы `:nth-child()` для выбора определенного пузырька. \
`left` задает расстояние от левой границы окна до левого края пузырька.\
`animation-delay` определяет задержку перед началом анимации пузырька.

```css
.banner{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

```
