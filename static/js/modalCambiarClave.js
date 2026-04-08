document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("formCambiarClave");
    const mensaje = document.getElementById("mensajeClave");

    // CUANDO DAN CLICK EN CAMBIAR CLAVE
    document.querySelectorAll(".btn-cambiar-clave").forEach(btn => {
        btn.addEventListener("click", () => {
            document.getElementById("clave_id").value = btn.dataset.id;
            mensaje.innerHTML = "";
            form.reset();
        });
    });

    // ENVÍO AJAX
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
                    bootstrap.Modal.getInstance(document.getElementById("modalCambiarClave")).hide();
                }, 1000);

            } else {
                mensaje.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
            }

        } catch (error) {
            mensaje.innerHTML = `<div class="alert alert-danger">Error del servidor</div>`;
            console.error(error);
        }
    });

});