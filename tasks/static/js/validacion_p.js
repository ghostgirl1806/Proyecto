document.addEventListener('DOMContentLoaded', function() {
    // Tu código aquí
    const $form = document.getElementById('form')
    const $codigo_producto = document.getElementById(codigo_producto)
    const cantidad = this.document.getElementById(cantidad)

    $form.addEventListener(submit, function(e){
        let cantidad1 = String(cantidad.value).trim();
        if(cantidad1=length === 0){
            alert("Debes ingresar un dato")
            e.preventDefault();
        }

    });

});