document.addEventListener('DOMContentLoaded', function(){

    document.querySelectorAll('.btn-editar-premio').forEach(btn => {

        btn.addEventListener('click', function(){

            document.getElementById('edit_id').value = this.dataset.id;
            document.getElementById('edit_nombres').value = this.dataset.nombres;
            document.getElementById('edit_apellidos').value = this.dataset.apellidos;
            document.getElementById('edit_identificacion').value = this.dataset.identificacion;
            document.getElementById('edit_puesto').value = this.dataset.puesto;

            // 🔥 ESTE ERA TU PROBLEMA
            document.getElementById('edit_valor').value = this.dataset.valor;

            document.getElementById('edit_agencia').value = this.dataset.agencia;
            document.getElementById('edit_categoria').value = this.dataset.categoria;

        });

    });

});



document.getElementById('formEditarPremio').addEventListener('submit', function(e){
    e.preventDefault();

    const formData = new FormData(this);

    fetch("{% url 'editar_premio_ajax' %}", {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    .then(res => res.json())
    .then(data => {
        if(data.status === 'success'){
            location.reload();
        }else{
            alert('Error: ' + data.message);
        }
    });
});
