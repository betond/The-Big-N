<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;

require 'phpMailer/src/PHPMailer.php';
require 'phpMailer/src/SMTP.php';
require 'phpMailer/src/Exception.php';

function sendCorreo($doc, $correo, $nombre, $curp){

    //Create a new PHPMailer instance
    $mail = new PHPMailer();
    // $doc = generatePDF($curp);
    //Tell PHPMailer to use SMTP
    $mail->isSMTP();
    
    //Enable SMTP debugging
    //SMTP::DEBUG_OFF = off (for production use)
    //SMTP::DEBUG_CLIENT = client messages
    //SMTP::DEBUG_SERVER = client and server messages
    $mail->SMTPDebug = SMTP::DEBUG_OFF;
    
    //Set the hostname of the mail server
    $mail->Host = 'smtp.gmail.com';
    //Use `$mail->Host = gethostbyname('smtp.gmail.com');`
    //if your network does not support SMTP over IPv6,
    //though this may cause issues with TLS
    
    //Set the SMTP port number - 587 for authenticated TLS, a.k.a. RFC4409 SMTP submission
    $mail->Port = 587;
    
    //Set the encryption mechanism to use - STARTTLS or SMTPS
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    
    //Whether to use SMTP authentication
    $mail->SMTPAuth = true;
    
    //Username to use for SMTP authentication - use full email address for gmail
    $mail->Username = 'beto971227@gmail.com';
    
    //Password to use for SMTP authentication
    $mail->Password = 'zdadvvjyzjgxafwn';
    
    //Set who the message is to be sent from
    //$mail->setFrom('Unidad Politécnica de Integración Social - ESCOM', 'Alumnos Nuevo Ingreso - ESCOM');
    $mail->setFrom('beto971227@gmail.com', 'Unidad Politecnica de Integracion Social - ESCOM Alumnos Nuevo Ingreso');
    
    //Set who the message is to be sent to (para quien va)
    $mail->addAddress($correo, $nombre);
    
    //Set the subject line (asunto)
    $mail->Subject = 'ESCOM Horario examen';
    
    //Read an HTML message body from an external file, convert referenced images to embedded,
    //convert HTML into a basic plain-text alternative body
    $mail->msgHTML("
        <h2>Bienvenido alumno/a de nuevo ingreso (periodo Enero 2022) de parte de toda la ESCOMunidad te queremos dar la bienvenida a esta gran institucion academica, de la cual, ya eres parte.</h2>
        <p>
        Sin embargo, aun tienes que realizar un breve examen diagnostico, esto, con la unica funcion de conocer tu nivel de aprendizaje en el nivel educativo anterior, y asi mismo, puedas reforzar aquellas areas de oportunidad que encuentres con dicha evaluacion. No te preocupes, el examen diagnostico no condiciona ni tu horario, ni el turno al cual ya eres asignado. Por lo cual te pedimos atentamente que verifiques los datos que proporcionaste y que se encuentran en este documento, ya que este documento servira como comprobante para tu ingreso a la unidad academica y asi mismo, el ingreso al aula correspondiente.</p>
    ");
    
    //Attach an image file (enviar pdfs)
    $mail->addStringAttachment($doc, $curp.".pdf");
    
    //send the message, check for errors
    if (!$mail->send()) {
        echo $correo;
        echo $mail->ErrorInfo;
        return $mail->ErrorInfo;
    } else {
        return 1;
        //Section 2: IMAP
        //Uncomment these to save your message in the 'Sent Mail' folder.
        #if (save_mail($mail)) {
        #    echo "Message saved!";
        #}
    }
}


?>
