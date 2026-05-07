document.addEventListener('DOMContentLoaded', function () {

    /*
    ============================================
    ABRIR DETALLE EVENTO
    ============================================
    */

    const botonesDetalle = document.querySelectorAll('.btn-ver-detalle');

    botonesDetalle.forEach(function(boton){

        boton.addEventListener('click', function(){

            const eventoId = this.dataset.id;

            const contenedor = document.getElementById('contenidoDetalleEvento');

            contenedor.innerHTML = `
                <div class="text-center p-5">

                    <div class="spinner-border text-primary"></div>

                    <p class="mt-3">
                        Cargando información...
                    </p>

                </div>
            `;

            //let url = "{% url 'detalle_evento_modal' 0 %}";
            let url = boton.dataset.url;

            url = url.replace('/0/', `/${eventoId}/`);

            fetch(url)

                .then(response => response.text())

                .then(html => {

                    contenedor.innerHTML = html;

                })

                .catch(error => {

                    console.error(error);

                    contenedor.innerHTML = `
                        <div class="alert alert-danger">
                            Error cargando el detalle
                        </div>
                    `;
                });

        });

    });

    /*
    ============================================
    EDITAR PREMIO
    FUNCIONA CON AJAX DINÁMICO
    ============================================
    */

    document.addEventListener('click', function(e){

        const boton = e.target.closest('.btn-editar-premio');

        if(!boton) return;

        document.getElementById('edit_id').value =
            boton.dataset.id;

        document.getElementById('edit_nombres').value =
            boton.dataset.nombres;

        document.getElementById('edit_apellidos').value =
            boton.dataset.apellidos;

        document.getElementById('edit_identificacion').value =
            boton.dataset.identificacion;

        document.getElementById('edit_agencia').value =
            boton.dataset.agencia;

        document.getElementById('edit_categoria').value =
            boton.dataset.categoria;

        document.getElementById('edit_puesto_numero').value =
            boton.dataset.puesto_numero;

        document.getElementById('edit_valor_premio').value =
            boton.dataset.valor_premio;

    });

});