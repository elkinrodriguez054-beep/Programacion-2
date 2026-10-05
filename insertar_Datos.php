 <html>
 <head>
 <title>InsertarDatos.php</title>
 <meta http-equiv='content-type' content='text/html; charset=UTF-8'/>
 </head>
 <body>
 <BODY BACKGROUND="imagenDeFondo.jpg">

 <form action='InsertarDatos.php' method='post'>
	<div>id  : <input type='text' name='id' value=" "/> </div>
	<div>nombre :   <input type='text' name='nombre' value=" "/> </div>
        <div>nacimiento :   <input type='text' name='nacimiento' value=" "/> </div>
         
	<div><input type='submit' name='insert' value='Insertar registro'/></div>
 </form>

 <?php 
	$link = new mysqli("localhost", "root", "", "prueba");
	
	$sql = "INSERT INTO persona (id, nombre, nacimiento) VALUES ('$_POST[id]', '$_POST[nombre]', '$_POST[nacimiento]')";


 if ($link->query($sql) === TRUE) {
    echo "New record created successfully";
 } else {
    echo "Error: " . $sql . "<br>" . $link->error;
 }


 ?>

 </body>
 </html>