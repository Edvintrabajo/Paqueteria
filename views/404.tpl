<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!--LINK CSS-->
    <link rel="stylesheet" href="/static/css/styleError.css">
    <link rel="stylesheet" href="/static/css/normalize.css">

    <!--GOOGLE FONTS-->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet"> 
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">

    <title>Error Document</title>
</head>
<body class="contenedor-error">

    <div class="contenedor-nav">
        <nav class="nav">
            <a href="/" class="nombre-empresa">Paqueteria</a>
        </nav>
    </div>


    <h1>Parece que se ha producido un error</h1>
    <p class="mensaje">{{error}}</p>
    
</body>
</html>