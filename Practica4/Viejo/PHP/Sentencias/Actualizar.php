<?php
$mysqli = new mysqli("localhost", "root", "", "alumnos");
session_start();
$dataArray = $_SESSION['dataArray'];
$dataArray['Nombre'] = $_POST['nombre'];
$dataArray['ApellidoP'] = $_POST['aPaterno'];
$dataArray['ApellidoM'] = $_POST['aMaterno'];
$dataArray['FechaN'] = $_POST['fNacimiento'];
$dataArray['Genero'] = $_POST['genero'];
$dataArray['CURP'] = $_POST['curp'];
$dataArray['Calle'] = $_POST['calle-Num'];
$dataArray['Colonia'] = $_POST['colonia'];
$dataArray['Alcaldia'] = $_POST['alcaldia'];
$dataArray['CodigoPostal'] = $_POST['CP'];
$dataArray['Telefono'] = $_POST['telefono'];
$dataArray['Correo'] = $_POST['email'];
$dataArray['EscuelaProcedencia'] = $_POST['esc-Proc'];
$dataArray['NombreEscuela'] = $_POST['nom-esc'];
$dataArray['Promedio'] = $_POST['promedio'];
$dataArray['EscomOpcion'] = $_POST['opcion'];
$_SESSION['dataArray'] = $dataArray;

if(mysqli_connect_error()){
    die('connect error('.mysqli_connect_errno().')'.mysqli_connect_error());
}else{
    $UPDATE = "UPDATE alumnodatos SET Nombre=?,
    ApellidoP=?,
    ApellidoM=?,
    FechaN=?,
    Genero=?,
    CURP=?,
    Calle=?,
    Colonia=?,
    Alcaldia=?,
    CodigoPostal=?,
    Telefono=?,
    Correo=?,
    EscuelaProcedencia=?,
    EntidadProcedencia=?,
    NombreEscuela=?,
    Promedio=?,
    EscomOpcion=?
    WHERE Id = ?";
    $result = $mysqli->prepare($UPDATE);
    $result ->bind_param("sssssssssiissssdss",$dataArray['Nombre'],$dataArray['ApellidoP'],$dataArray['ApellidoM'],$dataArray['FechaN'],$dataArray['Genero'],$dataArray['CURP'],$dataArray['Calle'],$dataArray['Colonia'],$dataArray['Alcaldia'],$dataArray['CodigoPostal'],$dataArray['Telefono'],$dataArray['Correo'],$dataArray['EscuelaProcedencia'],$dataArray['EntidadProcedencia'],$dataArray['NombreEscuela'],$dataArray['Promedio'],$dataArray['EscomOpcion'],$dataArray['Id']);
    $result->execute();
    $result->close();
    $mysqli->close();
    echo "Alumno Actualizado correctamente";
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