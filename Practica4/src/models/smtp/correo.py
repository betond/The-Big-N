from email.message import EmailMessage
import smtplib

def SendCorreo(destino, msg, asunto):
    remitente = "beto971227@gmail.com"
    destinatario = destino
    mensaje = msg
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = asunto
    email.set_content(mensaje)
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(remitente, "aycxzdgywvmayupx")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()
    
#SendCorreo("beto971227@gmail.com", "hola bb", "holisssss")