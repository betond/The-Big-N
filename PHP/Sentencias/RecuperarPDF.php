<?php
require('../MakePDF.php');

$mysqli = new mysqli("localhost", "root", "", "alumnos");
session_start();
$boleta = $_POST['boleta'];

$SEARCH = "SELECT * from alumnodatos where Id = ? limit 1";
$result = $mysqli->prepare($SEARCH);
$result->bind_param("s",$boleta);
$result->execute();
$row = $result->get_result(); 
$resultNum = $row->num_rows;
if($resultNum == 0){
    echo "      Numero de boleta no encontrado!!<br><br>     Registrate en el formulario para poder recuperar tu PDF!!";
}else{
    echo "      Boleta encontrada se mandara por correo tu PDF!!";
    Comprobante($boleta);
}
$result->close();
$mysqli->close();

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> PDF </title>

</head>
<body onload="Cargando()">

    <script src="../../jquery/jquery-3.6.0.min.js"></script>

    <script type="text/javascript">

        const sleep = (milliseconds) => {
            return new Promise(resolve => setTimeout(resolve, milliseconds))
        }

        async function Cargando(){
            await sleep(5000);
            location.href="../../HTML/P_Inicio.html";
        }
    </script>

</body>
</html>