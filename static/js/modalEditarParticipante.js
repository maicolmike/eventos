document.addEventListener("DOMContentLoaded", function () {

    // 🔹 Cuando dan clic en editar
    document.querySelectorAll(".btn-editar").forEach(btn => {
        btn.addEventListener("click", function () {

            document.getElementById("edit_id").value = this.dataset.id;
            document.getElementById("edit_tipo_participante").value = this.dataset.tipo_participante;
            document.getElementById("edit_identificacion").value = this.dataset.identificacion;
            document.getElementById("edit_nombres").value = this.dataset.nombres;
            document.getElementById("edit_apellidos").value = this.dataset.apellidos;
            document.getElementById("edit_agencia").value = this.dataset.agencia;
        });
    });

    // 🔹 Enviar formulario por AJAX
    document.getElementById("formEditarParticipante").addEventListener("submit", function (e) {
        e.preventDefault();

        let form = this;
        let url = form.dataset.url;
        let formData = new FormData(form);

        fetch(url, {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": form.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            let mensaje = document.getElementById("mensajeEditar");

            if (data.status === "success") {
                mensaje.innerHTML = `<div class="alert alert-success">${data.message}</div>`;

                // 🔥 Recargar tabla automáticamente
                setTimeout(() => {
                    location.reload();
                }, 1000);

            } else {
                mensaje.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });

});