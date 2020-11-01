$(document).ready(function () {
    $('.owl-carousel').owlCarousel({
        loop:true,
        margin:10,
        items: 1,
        autoplay:true,
        autoplaySpeed:5000,
        autoplayTimeout: 8000
    })
});


function validacionForm(){

    nom    = document.getElementById('usuario').value;
    correo = document.getElementById('email').value;
    pass1  = document.getElementById('password').value;    
    pass2  = document.getElementById('password2').value;

    expReg = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;

    if(nom = null || nom.length == 0 || /^\s+$/.test(nom)){
        alert('Error... por favor, ingrese su usuario ');
        document.datos.nom.focus();
        return false;
    }

    if(!expReg.test(correo)){
        alert("El correo no es válido")
        return false;
    }

    if(pass1 == null || pass1.length == 0){
        alert('Error... por favor, ingrese una contraseña válida');
        document.datos.pass1.focus();
        return false;
    }

    if(pass2 == null || pass2.length == 0 || pass2 != pass1){
        alert('Error... la contraseña ingresada no coincide con la anterior');
        document.datos.pass2.focus();
        return false;
    }

    console.log("Se ha registrado con exito en Bak4nime!!");
    alert('Se ha registrado con exito en Bak4nime!!')
    document.datos.clear
    return true;

}


function validacionLogin(){

    correo =  document.getElementById("email").value;
    pass   =  document.getElementById("password").value;
    expReg = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;

    if(!expReg.test(correo)){
        alert("El correo no es válido")
        return false;
    }
    
    if(pass == null || pass.length == 0){
        alert('Error... por favor, ingrese una contraseña válida');
        document.datos.pass.focus();
        return false;
    }

    console.log("Se ha Logeado con exito en Bak4nime!!");
    alert('Se ha Logeado con exito en Bak4nime!!')
    document.datos.clear
    return true;
    

}