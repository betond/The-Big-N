<?php
require('../MakePDF.php');

$mysqli = new mysqli("localhost", "root", "", "alumnos");
session_start();
$dataArray = $_SESSION['dataArray'];

if ($dataArray['EntidadProcedencia'] == "null" && $dataArray['NombreEscuela'] == ""){
    if(mysqli_connect_error()){
        die('connect error('.mysqli_connect_errno().')'.mysqli_connect_error());
    }else{
        $SEARCH = "SELECT Id from alumnodatos where Id = ? limit 1";
        $INSERT = "INSERT INTO alumnodatos (Id,Nombre,ApellidoP,ApellidoM,FechaN,Genero,CURP,Calle,Colonia,Alcaldia,CodigoPostal,Telefono,Correo,EscuelaProcedencia,Promedio,EscomOpcion,Grupo,Hora) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";
        $result = $mysqli->prepare($SEARCH);
        $result->bind_param("s",$dataArray['Id']);
        $result->execute();
        $result->store_result();
        $resultNum = $result->num_rows;
        if($resultNum == 0){
            $result->close();
            $result = $mysqli->prepare($INSERT);
            $result ->bind_param("ssssssssssiissdsss",$dataArray['Id'],$dataArray['Nombre'],$dataArray['ApellidoP'],$dataArray['ApellidoM'],$dataArray['FechaN'],$dataArray['Genero'],$dataArray['CURP'],$dataArray['Calle'],$dataArray['Colonia'],$dataArray['Alcaldia'],$dataArray['CodigoPostal'],$dataArray['Telefono'],$dataArray['Correo'],$dataArray['EscuelaProcedencia'],$dataArray['Promedio'],$dataArray['EscomOpcion'],$dataArray['Grupo'],$dataArray['Hora']);
            $result->execute();
            echo "      Registro Completado!!<br><br>       Se ha enviado el PDF al correo electronico registrado!!";
        }else{
            echo "      Alguien ya registro ese Número de Boleta!!<br><br>       Se ha enviado una copia del PDF al correo electronico registrado!!";
        }
        $result->close();
        $mysqli->close();
    }
} else {
    if(mysqli_connect_error()){
        die('connect error('.mysqli_connect_errno().')'.mysqli_connect_error());
    }else{
        $SEARCH = "SELECT Id from alumnodatos where Id = ? limit 1";
        $INSERT = "INSERT INTO alumnodatos (Id,Nombre,ApellidoP,ApellidoM,FechaN,Genero,CURP,Calle,Colonia,Alcaldia,CodigoPostal,Telefono,Correo,EscuelaProcedencia,EntidadProcedencia,NombreEscuela,Promedio,EscomOpcion,Grupo,Hora) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";
        $result = $mysqli->prepare($SEARCH);
        $result->bind_param("s",$dataArray['Id']);
        $result->execute();
        $result->store_result();
        $resultNum = $result->num_rows;
    }
    if($resultNum == 0){
            $result->close();
            $result = $mysqli->prepare($INSERT);
            $result ->bind_param("ssssssssssiissssdsss",$dataArray['Id'],$dataArray['Nombre'],$dataArray['ApellidoP'],$dataArray['ApellidoM'],$dataArray['FechaN'],$dataArray['Genero'],$dataArray['CURP'],$dataArray['Calle'],$dataArray['Colonia'],$dataArray['Alcaldia'],$dataArray['CodigoPostal'],$dataArray['Telefono'],$dataArray['Correo'],$dataArray['EscuelaProcedencia'],$dataArray['EntidadProcedencia'],$dataArray['NombreEscuela'],$dataArray['Promedio'],$dataArray['EscomOpcion'],$dataArray['Grupo'],$dataArray['Hora']);
            $result->execute();
            echo "      Registro Completado!!<br><br>       Se ha enviado el PDF al correo electronico registrado!!";
        }else{
            echo "      Alguien ya registro ese Número de Boleta!!<br><br>       Se ha enviado una copia del PDF al correo electronico registrado!!";
        }
        $result->close();
        $mysqli->close();
}

Comprobante($dataArray['Id']);

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
            await sleep(10000);
            location.href="../../HTML/P_Inicio.html";
        }
    </script>

</body>
</html>