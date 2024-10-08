# Адаптивный веб-дизайн с использованием HTML и CSS

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>адаптивные карточки товаров Flexbox</title>
    <link rel="stylesheet" href="style.css"> 
</head> 
<body>
    <div class="wrapper">
        <div class="services">
        <a href="#">
            <span class="single-img img-one">
                <span class="img-text">
                    <h4>Canon 9587</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Esse, quam.</p>
                    <button>Buy Now</button>
                </span>
            </span>
        </a>
        <a href="#">
            <span class="single-img img-two"> 
                <span class="img-text">
                    <h4>Nikon 3458</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Esse, quam.</p>
                    <button>Buy Now</button>
                </span>
            </span>
        </a>
        <a href="#">
            <span class="single-img img-three">
                <span class="img-text">
                    <h4>Sony 1234</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Esse, quam.</p>
                    <button>Buy Now</button>
                </span>
            </span>
        </a>
    </div>
    </div>
</body>
</html>
```

```css
body{
    background: #252525;
}
a{
    text-decoration: none;
}
.wrapper{
    padding: 125px 0 0 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.services{
    width: 1100px;
    height: auto;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin: 0 auto;
}
.single-img{
    border-radius: 5px;
    display: flex;
    flex-direction: column-reverse;
    flex-wrap: nowrap;
    width: 325px;
    height: 450px;
    overflow: hidden;
    box-shadow: 5px 5px 20px rgba(0,0,0,0.3);
    transform: translate(0, 0);
    transition: .3s;
}
.single-img:hover{
    transform: translate(0, -9px);
}
.img-one{
    background-image: url(1.jpg);
    background-size: cover;
    background-position: center center;
}
.img-two{
    background-image: url(3.jpg);
    background-size: cover;
    background-position: center center;
}
.img-three{
    background-image: url(2.jpg);
    background-size: cover;
    background-position: center center;
}
.img-text{
    background: linear-gradient(to top,rgba(255,255,255,0.9),rgba(255,255,255,0));
    padding: 0 10px 5px 10px;
    width: 100%;
    height: auto;
    position: relative;
    transform: translate(0, 110px);
    line-height: 25px;
    transition: 0.5s ease;
    display: inline-block;
    text-align: center;
    color: #fff;
}
.img-text h4{
    line-height: 15px;
    padding: 0;
    margin: 16px 0;
    font-family: 'Alfa Slab One', cursive;
    font-size: 25px;
}
.services button{
    background: #252525;
    color: #fff;
    padding: 10px 35px;
    border: none;
    border-radius: 50px;
    line-height: 14px;
    display: inline-block;
    margin-bottom: 10px;
}
.single-img:hover .img-text{
    transform: translate(0, 0);
}

@media (max-width: 991px){
    .wrapper{
        padding: 0;
    }
    .services{
        width: 100%;
        display: flex;
        flex-direction: column;
    }
    a{
        margin-bottom: 35px;
    }
}
```