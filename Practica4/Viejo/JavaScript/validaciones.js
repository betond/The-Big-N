
document.getElementById("nboleta").addEventListener("keyup", validaBol);
document.getElementById("nombre").addEventListener("keyup", validaNom);
document.getElementById("aPaterno").addEventListener("keyup", validaAp);
document.getElementById("aMaterno").addEventListener("keyup", validaAm);
document.getElementById("fNacimiento").addEventListener("keyup", validaFec);
document.getElementById("curp").addEventListener("keyup", validaCurp);
document.getElementById("calle-Num").addEventListener("keyup", validaCaNum);
document.getElementById("colonia").addEventListener("keyup", validaColonia);
document.getElementById("CP").addEventListener("keyup", validaCP);
document.getElementById("telefono").addEventListener("keyup", validaTel);
document.getElementById("email").addEventListener("keyup", validaEmail);
document.getElementById("nom-esc").addEventListener("keyup", validaNomEsc);
document.getElementById("promedio").addEventListener("keyup", validaPro);

document.getElementById("Formulario").addEventListener("submit", myFunction);

function myFunction(event){

    var nboleta = document.getElementById("nboleta").style.borderColor;
    var nombre = document.getElementById("nombre").style.borderColor;
    var aPaterno = document.getElementById("aPaterno").style.borderColor;
    var aMaterno = document.getElementById("aMaterno").style.borderColor;
    var curp = document.getElementById("curp").style.borderColor;
    var calleNum = document.getElementById("calle-Num").style.borderColor;
    var colonia = document.getElementById("colonia").style.borderColor;
    var cp = document.getElementById("CP").style.borderColor;
    var telefono = document.getElementById("telefono").style.borderColor;
    var email = document.getElementById("email").style.borderColor;
    var nomesc = document.getElementById("nom-esc").style.borderColor;
    var promedio = document.getElementById("promedio").style.borderColor;
     
    if (nboleta != 'green' || nombre!='green' || aPaterno!='green' || aMaterno!='green' || curp!='green' || calleNum!='green' || colonia!='green' || cp!='green' || telefono!='green' || email!='green' || promedio != 'green') {
      event.preventDefault(); 
      alert('Revisa que todos tus datos esten correctos');

    }
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

//Valida el Boleta

function validaBol(){
    var enviar = document.getElementById("enviar");
    var bol = document.getElementById("nboleta");
    let mensaje = document.getElementById("rbol");
    const re = new RegExp("^[(0-9)|PP|PE]{2}\\d{8}$", "gi");
    let val = re.test(bol.value);
    
    console.log(val);
    if (bol.value == '' || val==false) {
    	bol.style.borderColor = "red";
        mensaje.innerText = 
      `Boleta inválida.`;
      
    }
    else {
      bol.style.borderColor = "green";
      enviar.disabled=false
      
      mensaje.innerText = ''
    }
  
}

//Valida el nombre
function validaNom(){
        var enviar = document.getElementById("enviar");

    var nom = document.getElementById("nombre");
    let mensaje = document.getElementById("rnom");
    const re = new RegExp("^[a-zA-ZÀ-ÿ\\s]{1,25}$", "gi");
    let val = re.test(nom.value);
    if (nom.value == '' || val==false) {
    	nom.style.borderColor = "red";
        mensaje.innerText = 
      `Nombre inválido.`;
      

    }
    else {
        
      nom.style.borderColor = "green";
      mensaje.innerText = ''
    }
  
}
//Valida el Apellido Paterno
function validaAp(){
        var enviar = document.getElementById("enviar");

    var ap = document.getElementById("aPaterno");
    let mensaje = document.getElementById("rap");
        const re = new RegExp("^[a-zA-ZÀ-ÿ\\s]{1,25}$", "gi");
    let val = re.test(ap.value);
    if (ap.value == '' || val==false) {
    	ap.style.borderColor = "red";
        mensaje.innerText = 
      `Apelldio Paterno inválido.`;
      

    }
    else {
        
      ap.style.borderColor = "green";
      mensaje.innerText = ''
    }
  
}
//Valida el Apellido Materno
function validaAm(){
        var enviar = document.getElementById("enviar");

    var am = document.getElementById("aMaterno");
    let mensaje = document.getElementById("ram");
        const re = new RegExp("^[a-zA-ZÀ-ÿ\\s]{1,25}$", "gi");
    let val = re.test(am.value);
    if (am.value == '' || val==false) {
    	am.style.borderColor = "red";
        mensaje.innerText = 
      `Apellido Materno inválido.`;
      

    }
    else {
        
      am.style.borderColor = "green";
      mensaje.innerText = ''
    }
  
}//Valida el Fecha de nacimiento
function validaFec(){
        var enviar = document.getElementById("enviar");

    var fec = document.getElementById("fNacimiento");
    let mensaje = document.getElementById("rfec");
    if (fec.value == '') {
    	fec.style.borderColor = "red";
        mensaje.innerText = 
      `Fecha inválida.`;
      

    }
    else {
        
      fec.style.borderColor = "green";
      mensaje.innerText = ''
    }
  
}
//Valida el Curp
function validaCurp(){
        var enviar = document.getElementById("enviar");

    var curp = document.getElementById("curp");
    let mensaje = document.getElementById("rcurp");
    const re = new RegExp("^[A-Z]{1}[AEIOU]{1}[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM]{1}(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]{1}[0-9]{1}$", "gi");
    let val = re.test(curp.value);
    if (curp.value == '' || val==false) {
    	curp.style.borderColor = "red";
        mensaje.innerText = 
      `CURP inválido.`;
      

    }
    else {
        
      curp.style.borderColor = "green";
      mensaje.innerText = ''
    }
  
}//Valida el Calle y num
function validaCaNum(){
        var enviar = document.getElementById("enviar");

    var canum = document.getElementById("calle-Num");
    let mensaje = document.getElementById("rcalle-Num");

    if (canum.value == '') {
    	canum.style.borderColor = "red";
        mensaje.innerText = 
      `Calle y numero inválido.`;
      

    }
    else {
        
        canum.style.borderColor = "green";
      mensaje.innerText = ''
    }
  
}
//Valida el Colonia
function validaColonia(){
        var enviar = document.getElementById("enviar");

    var col = document.getElementById("colonia");
    let mensaje = document.getElementById("rcol");

    if (col.value == '') {
    	col.style.borderColor = "red";
        mensaje.innerText = 
      `Colonia inválida.`;
      

    }
    else {
        
      col.style.borderColor = "green";
      mensaje.innerText = ''
    }
  
}//Valida el Codigo postal
function validaCP(){
        var enviar = document.getElementById("enviar");

    var cp = document.getElementById("CP");
    let mensaje = document.getElementById("rcp");
    const re = new RegExp("^\\d{5}$", "gi");
    let val = re.test(cp.value);
    if (cp.value == '' || val==false) {
    	cp.style.borderColor = "red";
        mensaje.innerText = 
      `Codigo Postal inválido.`;
      

    }
    else {
        
      cp.style.borderColor = "green";
      mensaje.innerText = ''
    }
  
}
//Valida el Telefono
function validaTel(){
        var enviar = document.getElementById("enviar");

    var tel = document.getElementById("telefono");
    let mensaje = document.getElementById("rtel");
        const re = new RegExp("^\\d{10}$", "gi");
    let val = re.test(tel.value);
    if (tel.value == '' || val==false) {
    	tel.style.borderColor = "red";
        mensaje.innerText = 
      `Telefono inválido.`;
      

    }
    else {
        
      tel.style.borderColor = "green";
      mensaje.innerText = ''
    }
  
}//Valida el Email
function validaEmail(){
        var enviar = document.getElementById("enviar");

    var email = document.getElementById("email");
    let mensaje = document.getElementById("remail");
    const re = new RegExp("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$", "gi");
    let val = re.test(email.value);
    if (email.value == '' || val==false) {
    	email.style.borderColor = "red";
        mensaje.innerText = 
      `Correo inválido.`;
      

    }
    else {
        
      email.style.borderColor = "green";
      mensaje.innerText = ''
    }
  
}
//Valida el NombreEsc
function validaNomEsc(){
        var enviar = document.getElementById("enviar");

    var nomesc = document.getElementById("nom-esc");
    let mensaje = document.getElementById("resc-Proc");
    
    if (nomesc.value == '') {
    	nomesc.style.borderColor = "red";
        mensaje.innerText = 
      `Nombre de Escuela inválida.`;
      

    }
    else {
        
        nomesc.style.borderColor = "green";
      mensaje.innerText = ''
    }
  
}
//Valida el Promedio
function validaPro(){
        var enviar = document.getElementById("enviar");

    var pro = document.getElementById("promedio");
    let mensaje = document.getElementById("rpro");
    const re = new RegExp("^[0-1]{1}[0-9]{1}.[0-9]{2}$", "gi");
    let val = re.test(pro.value);
    if (pro.value == '' || val==false) {
    	pro.style.borderColor = "red";
        mensaje.innerText = 
      `Promedio inválido.`;
      

    }
    else {
        
      pro.style.borderColor = "green";
      mensaje.innerText = ''
    }
  
}