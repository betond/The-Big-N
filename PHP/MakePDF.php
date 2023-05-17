<?php
require('../../LibraryPDF/fpdf.php');
require('enviar_correo.php');

function Comprobante($ID){

    class PDF extends FPDF
    {
        // Cabecera de página
        function Header()
        {
            // Logo
            $this->Image('../../Imagenes/encabezado.fw.png',4,8,211.9);
            $this->Image('../../Imagenes/EscudoIPN.png',30,230,50);
            $this->Image('../../Imagenes/EscudoESCOM.png',130,230,50);
            //Imagen de bienvenida.
            //Encabezado
            $this->SetFont('Arial','B',15);
            //Institución      
            $this->SetY(30);
            $this->SetX(70);
            $this -> Cell(51,10,'Instituto Politécnico Nacional');
            //Escuela
            $this -> SetY(40);
            $this -> SetX(69);
            $this -> Cell(48,10,'Escuela Superior de Cómputo');
            $this ->Ln(17);
            //Titulo
            $this->SetFont('Arial','B',17);
            $this -> SetX(70);
            $this->Cell(78,10,'Comprobante de examen',1,0);
            $this->Ln(20);

            $this ->SetX(13);
            $this->SetFont('Arial','B',11);
            $this -> Cell(30,10,"Boleta",1,0,'C',0);
            $this -> Cell(40,10,"Nombre",1,0,'C',0);
            $this -> Cell(40,10,"Apellido Paterno",1,0,'C',0);
            $this -> Cell(40,10,"Apellido Materno",1,0,'C',0);
            $this -> Cell(20,10,"Aula",1,0,'C',0);
            $this -> Cell(20,10,"Hora",1,1,'C',0);
        }

        // Pie de página
        function Footer()
        {
            // Posición: a 1,5 cm del final
            $this->SetY(-15);
            // Arial italic 8
            $this->SetFont('Arial','I',10);
            // Número de página
            $this->Cell(0,10,'Página '.$this->PageNo().'/1',0,0,'C');
        }
        
    }

    $mysqli = new mysqli("localhost", "root", "", "alumnos");
    //lineas de prueba
    $consulta = "SELECT Id,Nombre,ApellidoP,ApellidoM,Grupo,Hora,CURP,Correo FROM alumnodatos WHERE Id = ?";
    $resultado = $mysqli -> prepare($consulta);

    $result = $mysqli->prepare($consulta);
    $result->bind_param('s',$ID);
    $result->execute();
    $resultado = $result->get_result();

    //echo "<script>console.log( 'Debug Objects: " . $resultado . "' );</script>";


    $pdf = new PDF('P','mm',array(215.9,279.4));
    $pdf->AddPage();
    $pdf->SetFont('Arial','',10);
    //$pdf->Cell(40,10,'¡Hola, Mundo!');

    while($row = $resultado -> fetch_assoc()){
        $pdf ->SetX(13);
        $pdf -> Cell(30,10,$row['Id'],1,0,'C',0);
        $nombre = $row['Id'];
        $pdf -> Cell(40,10,$row['Nombre'],1,0,'C',0);
        $pdf -> Cell(40,10,$row['ApellidoP'],1,0,'C',0);
        $pdf -> Cell(40,10,$row['ApellidoM'],1,0,'C',0);
        $nombreCOMP = $row['Nombre'].' '.$row['ApellidoP'].' '.$row['ApellidoM'];
        $pdf -> Cell(20,10,$row['Grupo'],1,0,'C',0);
        $pdf -> Cell(20,10,$row['Hora'],1,1,'C',0);
        $CURP = $row['CURP'];
        $correo = $row['Correo'];
    }
    $pdf -> Ln(15);
    $pdf -> Line(20,110,195.4,110);
    $pdf -> Ln(10);
    $pdf -> Write(8, "Bienvenido alumno/a de nuevo ingreso (periodo Enero 2022) de parte de toda la ESCOMunidad te queremos dar la bienvenida a esta gran institución académica, de la cual, ya eres parte.

    Sin embargo, aún tienes que realizar un breve examen diagnóstico, estó, con la única función de conocer tu nivel de aprendizaje en el nivel educativo anterior, y así mismo, puedas reforzar aquellas áreas de oportunidad que encuentres con dicha evaluación. No te preocupes, el examen diagnóstico no condiciona ni tu horario, ni el turno al cual ya eres asignado. Por lo cual te pedimos atentamente que verifiques los datos que proporcionaste y que se encuentran en este documento, ya que este documento servirá como comprobante para tu ingreso a la unidad académica y así mismo, el ingreso al aula correspondiente.");

    $pdf -> Image('../../Imagenes/LogoBienvenidos.png',60,200,100); //Para poner hasta abajo, como despedida

    $ID = $nombre.".pdf";
    $modo = 'I';
    //$pdf->Output($ID,$modo);

    $docc = $pdf->Output('S',"",true);

    sendCorreo($docc,$correo,$nombreCOMP,$CURP);

}

?>