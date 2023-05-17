<?php
$mysqli = new mysqli("localhost", "root", "", "alumnos");
$dataArray = array();
session_start();
$boleta = $_POST['boleta'];

if(mysqli_connect_error()){
    die('connect error('.mysqli_connect_errno().')'.mysqli_connect_error());
}else{
    $SEARCH = "SELECT * from alumnodatos where Id = ? limit 1";
    $result = $mysqli->prepare($SEARCH);
    $result->bind_param("s",$boleta);
    $result->execute();
    $row = $result->get_result(); 
    $resultNum = $row->num_rows;
    if($resultNum == 0){
        echo "Esa boleta no existe";
    }else{
        $data = $row->fetch_assoc();
        $dataArray['Id'] = $data['Id'];
        $dataArray['Nombre'] = $data['Nombre'];
        $dataArray['ApellidoP'] = $data['ApellidoP'];
        $dataArray['ApellidoM'] = $data['ApellidoM'];
        $dataArray['FechaN'] = $data['FechaN'];
        $dataArray['Genero'] = $data['Genero'];
        $dataArray['CURP'] = $data['CURP'];
        $dataArray['Calle'] = $data['Calle'];
        $dataArray['Colonia'] = $data['Colonia'];
        $dataArray['Alcaldia'] = $data['Alcaldia'];
        $dataArray['CodigoPostal'] = $data['CodigoPostal'];
        $dataArray['Telefono'] = $data['Telefono'];
        $dataArray['Correo'] = $data['Correo'];
        $dataArray['EscuelaProcedencia'] = $data['EscuelaProcedencia'];
        $dataArray['EntidadProcedencia'] = $data['EntidadProcedencia'];
        $dataArray['NombreEscuela'] = $data['NombreEscuela'];
        $dataArray['Promedio'] = $data['Promedio'];
        $dataArray['EscomOpcion'] = $data['EscomOpcion'];
        $dataArray['Grupo'] = $data['Grupo'];
        $dataArray['Hora'] = $data['Hora'];
        $_SESSION['dataArray'] = $dataArray;
        header('Location: ../AlumnoEncontrado.php');
    }
    $result->close();
    $mysqli->close();
}
?>