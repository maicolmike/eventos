document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("formEliminar");
    const mensaje = document.getElementById("mensajeEliminar");

    // CUANDO DAN CLICK EN ELIMINAR
    document.querySelectorAll(".btn-eliminar").forEach(btn => {
        btn.addEventListener("click", () => {

            document.getElementById("delete_id").value = btn.dataset.id;
            document.getElementById("delete_nombres").textContent = btn.dataset.nombres;

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

            // 🔥 VALIDAR RESPUESTA HTTP
            if (!response.ok) {
                throw new Error("Error HTTP: " + response.status);
            }

            // 🔥 VALIDAR QUE SEA JSON
            const text = await response.text();

            let data;
            try {
                data = JSON.parse(text);
            } catch (e) {
                console.error("Respuesta no es JSON:", text);
                throw new Error("Respuesta inválida del servidor");
            }

            if (data.status === "success") {
                mensaje.innerHTML = `<div class="alert alert-success">${data.message}</div>`;

                setTimeout(() => {
                    bootstrap.Modal.getInstance(document.getElementById("modalEliminarParticipante")).hide();

                    // 🔥 OPCIONAL: eliminar sin recargar
                    location.reload();
                }, 1000);

            } else {
                mensaje.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
            }

        } catch (error) {
            console.error("ERROR REAL:", error);
            mensaje.innerHTML = `<div class="alert alert-danger">Error del servidor</div>`;
        }
    });

});