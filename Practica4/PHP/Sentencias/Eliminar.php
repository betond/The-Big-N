<?php
$mysqli = new mysqli("localhost", "root", "", "alumnos");
$dataArray = array();
session_start();
$dataArray = $_SESSION['dataArray'];

if(mysqli_connect_error()){
    die('connect error('.mysqli_connect_errno().')'.mysqli_connect_error());
}else{
    $DELETE = "DELETE FROM alumnodatos WHERE Id = ?";
    $result = $mysqli->prepare($DELETE);
    $result ->bind_param("s",$dataArray['Id']);
    $result ->execute();
    $result->close();
    $mysqli->close();
    echo "Alumno eliminado";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Recepcion Datos </title>

</head>
<body onload="Cargando()">

    <script src="../../jquery/jquery-3.6.0.min.js"></script>

    <script type="text/javascript">

        const sleep = (milliseconds) => {
            return new Promise(resolve => setTimeout(resolve, milliseconds))
        }

        async function Cargando(){
            await sleep(5000);
            location.href="../../HTML/Administrador.html";
        }
    </script>

</body>
</html>