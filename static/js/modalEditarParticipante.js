document.addEventListener("DOMContentLoaded", () => {

    const modal = document.getElementById("modalEditarParticipante");
    const form = document.getElementById("formEditarParticipante");
    const mensaje = document.getElementById("mensajeEditar");

    // 🔹 CAMPOS REALES DEL MODELO
    const campos = ["id", "tipo_participante", "identificacion", "nombres", "apellidos", "agencia"];

    // 🔹 CLICK EN EDITAR
    document.querySelectorAll(".btn-editar").forEach(btn => {
        btn.addEventListener("click", () => {

            campos.forEach(campo => {
                const input = document.getElementById(`edit_${campo}`);
                if (input) {
                    input.value = btn.dataset[campo] || "";
                }
            });

            mensaje.innerHTML = "";
        });
    });

    // 🔹 ENVIAR FORMULARIO (AJAX)
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        mensaje.innerHTML = `<div class="alert alert-info">Guardando...</div>`;

        try {
            const formData = new FormData(form);
            const url = form.getAttribute("data-url");

            const response = await fetch(url, {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            });

            const data = await response.json();

            if (data.status === "success") {
                mensaje.innerHTML = `<div class="alert alert-success">${data.message}</div>`;

                setTimeout(() => {
                    const modalInstance = bootstrap.Modal.getInstance(modal);
                    modalInstance.hide();
                    location.reload();
                }, 800);

            } else {
                mensaje.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
            }

        } catch (error) {
            console.error(error);
            mensaje.innerHTML = `<div class="alert alert-danger">Error del servidor</div>`;
        }
    });

});