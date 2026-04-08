document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("formEliminar");
    const mensaje = document.getElementById("mensajeEliminar");

    // CUANDO DAN CLICK EN ELIMINAR
    document.querySelectorAll(".btn-eliminar").forEach(btn => {
        btn.addEventListener("click", () => {

            document.getElementById("delete_id").value = btn.dataset.id;
            document.getElementById("delete_username").textContent = btn.dataset.username;

            mensaje.innerHTML = "";
        });
    });

    // ENVÍO AJAX
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        mensaje.innerHTML = `<div class="alert alert-info">Eliminando...</div>`;

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
                    bootstrap.Modal.getInstance(document.getElementById("modalEliminar")).hide();
                    location.reload();
                }, 1000);

            } else {
                mensaje.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
            }

        } catch (error) {
            console.error(error);
            mensaje.innerHTML = `<div class="alert alert-danger">Error del servidor</div>`;
        }
    });

});