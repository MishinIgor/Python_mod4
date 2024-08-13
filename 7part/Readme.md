# Адаптивный веб-дизайн с использованием HTML и CSS

```html

<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <title>Адаптивный дизайн HTML && CSS</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="wrapper">
    <div class="box-area">
        <div class="icon-area">
            <i class="lni lni-island"></i>
        </div>
        <h6>Java Script</h6>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Atque, nobis?</p>
    </div>
    <div class="box-area custom">
        <div class="icon-area">
            <i class="lni lni-mashroom"></i>
        </div>
        <h6>HTML</h6>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Atque, nobis?</p>
    </div>
    <div class="box-area">
        <div class="icon-area">
            <i class="lni lni-trees"></i>
        </div>
        <h6>CSS</h6>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Atque, nobis?</p>
    </div>
</div>


</body>
</html>

```

```css
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}
body {
	display: flex;
	align-items: center;
	justify-content: center;
	min-height: 100vh;
	background-color: #0b69ed;
	font-family: poppins;
	text-align: center;
}
.wrapper {
	padding: 40px;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-wrap: wrap;
}
.box-area {
	width: 350px;
	margin: 25px;
	padding: 40px;
	background-color: #f5f5f5;
	transition: all 0.6s ease-in-out;
}
.box-area .icon-area {
	width: 100%;
	margin-bottom: 40px;
}
.icon-area i {
	font-size: 70px;
	color: #262626;
}
.box-area h6 {
	margin-bottom: 10px;
	color: #262626;
	font-size: 50px;
	font-family: bebas neue;
}
.box-area:hover {
	background-color: #161619;
	box-shadow: 15px 15px 30px rgba(0, 0, 0, 0.3);
}
.box-area:hover i {
	color: #fff;
}
.box-area:hover h6 {
	color: #fff;
}
.box-area:hover p {
	color: #fff;
}
```

_____________________________________________________

# Практика (part2)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Адаптивная верстка - практика</title>

    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <nav>
            <div class="logo">
                <h5>2023</h5>
            </div>
            <ul class="menu">
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Portfolio</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
            <div class="bar">
                <div class="bar-1"></div>
                <div class="bar-2"></div>
                <div class="bar-3"></div>
            </div>
        </nav>
    </header>
    <div class="banner">
        <div class="wrapper">
            <div class="content">
                <h2>2023</h2>
                <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Soluta, aliquam iure? Hic quisquam provident aut!</p>

                <a href="#">Learn More</a>

                <h5 class="socials">
                    <i class="fa fa-facebook"></i>
                    <i class="fa fa-twitter"></i>
                    <i class="fa fa-pinterest"></i>
                    <i class="fa fa-linkedin"></i>
                    <i class="fa fa-youtube"></i>
                </h5>
                
            </div>
        </div>
    </div>
    
<!--    JS добавлен для работы меню мобильной верстки-->
    <script>
        const sidenav = () => {
            const menu = document.querySelector('.bar');
            const nav = document.querySelector('.menu');

            menu.addEventListener('click', () => {
               menu.classList.toggle('bar-active');
                nav.classList.toggle('nav-active');
            });
        }
        sidenav();
    </script>
</body>
</html>
```

```css
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: sans-serif;
}
/*nav*/

nav{
    display: -webkit-flex;
    display: -moz-flex;
    display: -ms-flex;
    display: -o-flex;
    display: flex;
    justify-content: space-around;
    align-items: center;
    min-height: 10vh;
    background: #000;
}
.logo {
	color: #fff;
	text-transform: capitalize;
	font-size: 24px;
	cursor: pointer;
	font-weight: 900;
	letter-spacing: 1px;
}
.logo span{
    color: deepskyblue; 
}

.menu{
    display: -webkit-flex;
    display: -moz-flex;
    display: -ms-flex;
    display: -o-flex;
    display: flex;
    justify-content: space-around;
    width: 30%;
}
.menu li{
    list-style: none;
}
.menu a{
    color: #fff;
    text-decoration: none;
    font-size: 15px;
    padding: 30px;
    transition: .9s;
    font-weight: 600;
}
.menu a:hover {
	color: deepskyblue;
	font-weight: 500;
    letter-spacing: 2px;
}
.bar{
    display: none;
    cursor: pointer;
}
.bar div{
    width: 25px;
    height: 3px;
    background-color: #fff;
    margin: 5px;
    transition: all .5s ease;
}
@media screen and (max-width:1024px){
    .menu{
        width: 60%;
    }
}
@media screen and (max-width:768px){
    body{
        overflow-x: hidden;
    }
    .menu{
        position: absolute;
        right: -100%;
        height: 90vh;
        top: 10vh;
        background-color: #000;
        display: -webkit-flex;
        display: -moz-flex;
        display: -ms-flex;
        display: -o-flex;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        transform: translateX(100%);
        transition: transform 0.5s ease-in-out;
    }
    .bar{
        display: block;
    }
}

.nav-active{
    transform: translateX(-100%);
}
.bar-active .bar-1{
    transform: rotate(-45deg) translate(-5px, 6px);
}
.bar-active .bar-2{
    opacity: 0;
}
.bar-active .bar-3{
    transform: rotate(45deg) translate(-5px, -6px);
}


.banner {
	background-image: url(img.png);
	height: 100vh;
	background-size: cover;
	background-position: center;
}

.content h2 {
	font-family: alfa slab one;
	color: #fff;
	font-size: 60px;
}
  .content p {
	width: 50%;
	color: rgba(255,255,255,0.6);
	line-height: 2;
}
  .content a {
    background: deepskyblue;
    text-decoration: none;
    padding: 15px 30px;
    color: #fff;
    display: inline-block;
    margin-top: 20px;
  }
  .socials i {
    color: #fff;
    font-size: 18px;
    margin-right: 25px;
  }
  .socials {
    margin-top: 30px;
  }
  .wrapper {
	width: 1060px;
	margin: auto;
	padding-top: 12%;
}


@media only screen and (min-width: 768px) and (max-width: 991px){
    .wrapper {
        width: 75%;
        padding-top: 26%;
    }
    .content{
        text-align: center;
    }
    .content h2 {
        font-size: 60px;
    }
    .content p {
        width: 100%;
    }
}

@media screen and (max-width: 767px){
    .banner {
        background-position: 60%;
    }
    .wrapper {
        width: 75%;
        padding-top: 26%;
    }
    .content h2 {
        font-size: 30px;
    }
    .content p {
        width: 100%;
    }
}
```