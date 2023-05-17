<?php

$dataArray = array();
$dataArray['Id'] = $_POST['nboleta'];
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

$mysqli = new mysqli("localhost", "root", "", "alumnos");
$SELECT = "SELECT Id from alumnodatos";
$result = $mysqli->query($SELECT);
$resultNum = $result->num_rows;
$result->close();
$mysqli->close();

if ($resultNum<=25){
    $dataArray['Grupo'] = "LAB1";
    $dataArray['Hora'] = "10:00";
} else if ($resultNum>25 && $resultNum<=50){
    $dataArray['Grupo'] = "LAB2";
    $dataArray['Hora'] = "10:00";
} else if ($resultNum>50 && $resultNum<=75){
    $dataArray['Grupo'] = "LAB3";
    $dataArray['Hora'] = "10:00";
} else if ($resultNum>75 && $resultNum<=100){
    $dataArray['Grupo'] = "LAB4";
    $dataArray['Hora'] = "10:00";
} else if ($resultN>100 && $resultNum<=125){
    $dataArray['Grupo'] = "LAB5";
    $dataArray['Hora'] = "10:00";
} else if ($resultNum>125 && $resultNum<=150){
    $dataArray['Grupo'] = "LAB6";
    $dataArray['Hora'] = "10:00";
} else if ($resultNum>150 && $resultNum<=175){
    $dataArray['Grupo'] = "LAB1";
    $dataArray['Hora'] = "12:00";
} else if ($resultNum>175 && $resultNum<=200){
    $dataArray['Grupo'] = "LAB2";
    $dataArray['Hora'] = "12:00";
} else if ($resultNum>200 && $resultNum<=225){
    $dataArray['Grupo'] = "LAB3";
    $dataArray['Hora'] = "12:00";
} else if ($resultNum>225 && $resultNum<=250){
    $dataArray['Grupo'] = "LAB4";
    $dataArray['Hora'] = "12:00";
} else if ($resultNum>250 && $resultNum<=275){
    $dataArray['Grupo'] = "LAB5";
    $dataArray['Hora'] = "12:00";
} else if ($resultNum>275 && $resultNum<=300){
    $dataArray['Grupo'] = "LAB6";
    $dataArray['Hora'] = "12:00";
} else if ($resultNum>300 && $resultNum<=325){
    $dataArray['Grupo'] = "LAB1";
    $dataArray['Hora'] = "14:00";
} else if ($resultNum>325 && $resultNum<=350){
    $dataArray['Grupo'] = "LAB2";
    $dataArray['Hora'] = "14:00";
} else if ($resultNum>350 && $resultNum<=375){
    $dataArray['Grupo'] = "LAB3";
    $dataArray['Hora'] = "14:00";
} else if ($resultNum>375 && $resultNum<=400){
    $dataArray['Grupo'] = "LAB4";
    $dataArray['Hora'] = "14:00";
} else if ($resultNum>400 && $resultNum<=425){
    $dataArray['Grupo'] = "LAB5";
    $dataArray['Hora'] = "14:00";
} else if ($resultNum>425 && $resultNum<=450){
    $dataArray['Grupo'] = "LAB6";
    $dataArray['Hora'] = "14:00";
} else if ($resultNum>450 && $resultNum<=475){
    $dataArray['Grupo'] = "LAB1";
    $dataArray['Hora'] = "16:00";
} else if ($resultNum>475 && $resultNum<=500){
    $dataArray['Grupo'] = "LAB2";
    $dataArray['Hora'] = "16:00";
}

if (empty($_POST['entidad-Fed'])){
    $dataArray['EntidadProcedencia'] = "null";
} else {
    $dataArray['EntidadProcedencia'] = $_POST['entidad-Fed'];
}

session_start();
$_SESSION['dataArray'] = $dataArray;

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Validación de Datos </title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="stylesheet" href="../CSS/clases.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

</head>
<body onload="ocultar()">
    
<div class="container pt-4 text-center">
        <h3>Hola <?php echo $dataArray['Nombre'] ?>, verifica que los datos que ingresaste sean correctos: </h3><br>
</div>
<div class="form-control container">
    <form  method="post" action="Sentencias/Insertar.php" name="Formulario" id="form" >
        <fieldset>
            <legend><strong>Identidad:</strong></legend>
            <label for="nboleta">No. de boleta:</label>
                <input type="text" name="nboleta" id="nboleta" value='<?php echo $dataArray['Id'] ?>'  size="15" maxlength="15" disabled>
                <br><br>
            <label for="nombre">Nombre:</label>
                <input type="text" name="nombre" value='<?php echo $dataArray['Nombre'] ?>' size="30" id="nombre" disabled>
                <br><br>
            <label for="aPaterno">Apellido paterno:</label>
                <input type="text" name="aPaterno" value='<?php echo $dataArray['ApellidoP'] ?>' size="30" id="aPaterno" disabled>
                <br><br>
            <label for="aMaterno">Apellido materno:</label>
                <input type="text" name="aMaterno" value='<?php echo $dataArray['ApellidoM'] ?>' size="30" id="aMaterno" disabled>
                <br><br>
            <label for="fNacimieno">Fecha de nacimiento:</label>
                <input type="date" name="fNacimiento" value='<?php echo $dataArray['FechaN'] ?>' id="fNacimiento" disabled>
                <br><br>
            <label for="genero">Género:</label>
                <select name="genero" id="interes" disabled>
                    <option > --Selecciona una opci&oacute;n-- </option>
                    <option value="Masculino">Masculino</option>
                    <option value="Femenino">Femenino</option>
                    <option value="s.a.">Prefiero no responder</option>
            </select>
            <br><br><label for="curp">CURP:</label>
            <input type="text" name="curp" id="curp" size="22" value='<?php echo $dataArray['CURP'] ?>'  maxlength="18" disabled>
            <br>
        </fieldset>
        <fieldset>
            <legend><strong>Contacto:</strong></legend>
            <label for="calle-Num">Calle y Número:</label>
            <input type="text" name="calle-Num" id="calle-Num" value='<?php echo $dataArray['Calle'] ?>' size="40" maxlength="30" disabled>
            <br><br>
            <label for="colonia">Colonia:</label>
            <input type="text" name="colonia" id="colonia" value='<?php echo $dataArray['Colonia'] ?>' size="40" disabled>
            <br><br>
            <label for="alcaldia">Alcaldia:</label>
            <select name="alcaldia" id="alcaldia" disabled>
                <option disabled selected> --Selecciona una opci&oacute;n-- </option>
                <option value="Álvaro Obregón">Álvaro Obregón</option>                
                <option value="Azcapotzalco">Azcapotzalco</option>
                <option value="Benito Juárez">Benito Juárez</option>
                <option value="Coyoacán">Coyoacán</option>
                <option value="Cuajimalpa">Cuajimalpa</option>
                <option value="Cuauhtémoc">Cuauhtémoc</option>
                <option value="Gustavo A. Madero">Gustavo A. Madero</option>
                <option value="Iztacalco">Iztacalco</option>
                <option value="Iztapalapa">Iztapalapa</option>
                <option value="Magdalena Contreras">Magdalena Contreras</option>
                <option value="Miguel Hidalgo">Miguel Hidalgo</option>
                <option value="Milpa Alta">Milpa Alta</option>
                <option value="Tláhuac">Tláhuac</option>
                <option value="Tlalpan">Tlalpan</option>
                <option value="Venustiano Carranza">Venustiano Carranza</option>
                <option value="Xochimilco">Xochimilco</option>
            </select><br><br>
            <label for="CP">Código Postal:</label>
            <input type="number" name="CP" id="CP" size="7" value='<?php echo $dataArray['CodigoPostal'] ?>' maxlength="7" disabled>
            <br><br>
            <label for="telefono">Teléfono o celular:</label>
            <input type="phone" name="telefono" id="telefono" size="12" value='<?php echo $dataArray['Telefono'] ?>'  maxlength="10" disabled>
            <br><br>
            <label for="email">Correo electrónico:</label>
            <input type="mail" name="email" id="email" size="45" value='<?php echo $dataArray['Correo'] ?>' disabled>
            <br>
        </fieldset>
        <fieldset>
            <legend><strong>Procedencia:</strong></legend>
            <label for="esc-Proc">Escuela de procedencia:</label>
            <select name="esc-Proc" id="esc-Proc" disabled>
                    <option value="null" disabled> --Selecciona una opci&oacute;n-- </option>
                    <option value="cecyt1">CECYT #1 "GONZALO VÁZQUEZ VELA"</option>
                    <option value="cecyt2">CECYT #2 "MIGUEL BERNARD PERALES"</option>
                    <option value="cecyt3">CECYT #3 "ESTANISLAO RAMÍREZ RUIZ"</option>
                    <option value="cecyt4">CECYT #4 "LÁZARO CÁRDENAS DEL RÍO"</option>
                    <option value="cecyt5">CECYT #5 "BENITO JUÁREZ GARCÍA"</option>
                    <option value="cecyt6">CECYT #6 "MIGUEL OTHÓN DE MENDIZÁBAL"</option>
                    <option value="cecyt7">CECYT #7 "CUAUHTÉMOC"</option>
                    <option value="cecyt8">CECYT #8 "NARCISO BASSOLS GARCÍA"</option>
                    <option value="cecyt9">CECYT #9 "JUAN DE DIOS BÁTIZ PAREDES"</option>
                    <option value="cecyt10">CECYT #10 “CARLOS VALLEJO MÁRQUEZ”</option>
                    <option value="cecyt11">CECYT #11 "WILFRIDO MASSIEU PÉREZ"</option>
                    <option value="cecyt12">CECYT #12 "JOSÉ MA. MORELOS Y PAVÓN"</option>
                    <option value="cecyt13">CECYT #13 "RICARDO FLORES MAGÓN"</option>
                    <option value="cecyt14">CECYT #14 "LUIS ENRIQUE ERRO SOLER"</option>
                    <option value="cecyt15">CECYT #15 "DIÓDORO ANTÚNEZ ECHEGARAY"</option>
                    <option value="cet1">CET #1 "WALTER CROSS BUCHANAN"</option>
                    <option value="otro">otro</option>
                </select><br><br>
            <label for="entidad-Fed" id="txtentidad-Fed">Entidad Federativa de Procedencia:</label>
            <select name="entidad-Fed" id="entidad-Fed" disabled>
                    <option value="null" disabled>-- Selecciona una opci&oacute;n --</option>
                    <option value="Aguascalientes">Aguascalientes</option>
                    <option value="Baja California">Baja California</option>
                    <option value="Baja California Sur">Baja California Sur</option>
                    <option value="Campeche">Campeche</option>
                    <option value="Chiapas">Chiapas</option>
                    <option value="Chihuahua">Chihuahua</option>
                    <option value="Ciudad de México">Ciudad de México</option>
                    <option value="Coahuila">Coahuila</option>
                    <option value="Colima">Colima</option>
                    <option value="Durango">Durango</option>
                    <option value="Guanajuato">Guanajuato</option>
                    <option value="Guerrero">Guerrero</option>
                    <option value="Hidalgo">Hidalgo</option>
                    <option value="Jalisco">Jalisco</option>
                    <option value="Estado de México">Estado de México</option>
                    <option value="Michoacán">Michoacán</option>
                    <option value="Morelos">Morelos</option>
                    <option value="Nayarit">Nayarit</option>
                    <option value="Nuevo León">Nuevo León</option>
                    <option value="Oaxaca">Oaxaca</option>
                    <option value="Puebla">Puebla</option>
                    <option value="Querétaro">Querétaro</option>
                    <option value="Quintana Roo">Quintana Roo</option>
                    <option value="San Luis Potosí">San Luis Potosí</option>
                    <option value="Sinaloa">Sinaloa</option>
                    <option value="Sonora">Sonora</option>
                    <option value="Tabasco">Tabasco</option>
                    <option value="Tamaulipas">Tamaulipas</option>
                    <option value="Tlaxcala">Tlaxcala</option>
                    <option value="Veracruz">Veracruz</option>
                    <option value="Yucatán">Yucatán</option>
                    <option value="Zacatecas">Zacatecas</option>
                </select><br><br>
            <label for="nom-esc" id="txtnom-esc">Nombre de la Escuela:</label>
            <input type="text" name="nom-esc" id="nom-esc" size="50" value='<?php echo $dataArray['NombreEscuela'] ?>' maxlength="50" disabled>
            <br><br>
            <label for="promedio">Promedio:</label>
            <input type="number" name="promedio" id="promedio" step="0.01" min="0" max="10" value='<?php echo $dataArray['Promedio'] ?>' disabled>
            <br><br>
            <label for="opcion"> ESCOM fué tu: </label><br>
            <input type="radio" name="opcion" value="1" disabled><label>Primera opción</label><br>
            <input type="radio" name="opcion" value="2" disabled><label>Segunda opción</label><br>
            <input type="radio" name="opcion" value="3" disabled><label>Tercera opción</label><br>
            <input type="radio" name="opcion" value="4" disabled><label>Cuarta opción</label><br>
        </fieldset>
        <br><input id="enviar" type="submit" value="Registrar">
        <input type="button" value="Modificar" id="btn_save">

    </form>
</div>
    <script src="../jquery/jquery-3.6.0.min.js"></script>
    <script src="../JavaScript/backHistory.js"></script>
    <script type="text/javascript">
        var dataArray = <?php echo json_encode($dataArray); ?>;
        $(function() {
            $("#alcaldia").val(dataArray['Alcaldia']);
        });
        $(function() {
            $("#interes").val(dataArray['Genero']);
        });
        $(function() {
            $("#esc-Proc").val(dataArray['EscuelaProcedencia']);
        });
        $(function() {
            $("#entidad-Fed").val(dataArray['EntidadProcedencia']);
        });

        var radioGroup = document.Formulario.opcion;
        for (var i=0;i<4;i++){       
            if (radioGroup[i].value == dataArray['EscomOpcion'])
                radioGroup[i].checked = true;
        }

        function ocultar(){
            var escuelaProcedencia = document.getElementById("esc-Proc");
            var nombreEscuela = document.getElementById("nom-esc");
            var txtNombreEscuela = document.getElementById("txtnom-esc");
            var entidadFederativa = document.getElementById("entidad-Fed");
            var txtentidadFederativa = document.getElementById("txtentidad-Fed");
            console.log(escuelaProcedencia.value);
            if (escuelaProcedencia.value == "otro" || escuelaProcedencia.value == "null"){
                //nombreEscuela.style.display = 'inline';
                //txtNombreEscuela.style.display = 'inline';
                txtentidadFederativa.style.visibility='visible';
                entidadFederativa.style.visibility='visible';
                nombreEscuela.style.visibility='visible';
                txtNombreEscuela.style.visibility='visible';
            } else {
                //nombreEscuela.style.display = 'none';
                //txtNombreEscuela.style.display = 'none';
                txtentidadFederativa.style.visibility='hidden';
                entidadFederativa.style.visibility='hidden';
                nombreEscuela.style.visibility='hidden';
                txtNombreEscuela.style.visibility='hidden';
            }
        }
    </script>
</body>
</html>