<?php
$mysqli = new mysqli("localhost", "root", "", "alumnos");
$dataArray = array();
session_start();

if(mysqli_connect_error()){
    die('connect error('.mysqli_connect_errno().')'.mysqli_connect_error());
}else{
    //Estructura de la tabla
    echo "<div style=\"text-align:center\">";
    echo "<br><h2>Alumnos Listados </h2><br>";
    echo '<div style ="margin-top:10px;">';
    //Formato de la tabla
    echo '<table width ="90%" align="center" cellpadding="12px" cellspacing="0px" border="1px">';
    //Datos de las columnas
    echo '<td align="center" bgcolor="#802434" width="5%">'."<h3>"."Número"."</h3>".'</td>';
    echo '<td align="center" bgcolor="#802434" width="5%">'."<h3>"."Boleta"."</h3>".'</td>';
    echo '<td align="center" bgcolor="#802434" width="5%">'."<h3>"."Apellido Paterno"."</h3>".'</td>';
    echo '<td align="center" bgcolor="#802434" width="5%">'."<h3>"."Apellido Materno"."</h3>".'</td>';
    echo '<td align="center" bgcolor="#802434" width="5%">'."<h3>"."Nombres"."</h3>".'</td>';
    echo '<td align="center" bgcolor="#802434" width="5%">'."<h3>"."Grupo"."</h3>".'</td>';
    echo '<td align="center" bgcolor="#802434" width="5%">'."<h3>"."Horario"."</h3>".'</td>';

    $SELECT = "SELECT * from alumnodatos";
    $result = $mysqli->query($SELECT);
    $contador =1; //unicamente sirve para saber cuantos registros hay en la tabla

    while($row = $result->fetch_assoc()) {
        //Obtiene los datos de la BD y los coloca de acuerdo a las columnas de la tabla
        echo '<tr align ="center">';
        echo "<td>" . $contador++;
        echo "<td>" . $row["Id"] ;
        echo "<td>" . $row["ApellidoP"];
        echo "<td>" . $row["ApellidoM"] ;
        echo "<td>" . $row["Nombre"];
        echo "<td>" . $row["Grupo"];
        echo "<td>" . $row["Hora"];
    }
    $result->close();
    $mysqli->close();
}
?>