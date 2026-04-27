document.addEventListener("DOMContentLoaded", () => {

    console.log("JS ELIMINAR CARGADO ✅");

    const form = document.getElementById("formEliminar");
    const mensaje = document.getElementById("mensajeEliminar");

    if (!form) {
        console.error("No existe el formEliminar");
        return;
    }

    // ===============================
    // 🗑️ CLICK EN BOTÓN ELIMINAR
    // ===============================
    document.querySelectorAll(".btn-eliminar").forEach(btn => {
        btn.addEventListener("click", () => {

            console.log("CLICK BOTÓN ELIMINAR 🔥");

            document.getElementById("delete_id").value = btn.dataset.id;
            //document.getElementById("delete_nombres").textContent = btn.dataset.nombres;
            //document.getElementById("delete_apellidos").textContent = btn.dataset.apellidos;
            //document.getElementById("delete_nombre_completo").textContent = btn.dataset.nombres + " " + btn.dataset.apellidos;
            // Es exactamente lo mismo, pero más legible:
            document.getElementById("delete_nombre_completo").textContent = `${btn.dataset.nombres} ${btn.dataset.apellidos}`;
            
            if (mensaje) mensaje.innerHTML = "";
        });
    });

    // ===============================
    // 🚀 ENVIAR ELIMINACIÓN
    // ===============================
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        if (mensaje) {
            mensaje.innerHTML = `<div class="alert alert-info">Eliminando...</div>`;
        }

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

                if (mensaje) {
                    mensaje.innerHTML = `<div class="alert alert-success">${data.message}</div>`;
                }

                setTimeout(() => {
                    const modal = document.getElementById("modalEliminarPremio");
                    bootstrap.Modal.getInstance(modal).hide();
                    location.reload();
                }, 800);

            } else {
                if (mensaje) {
                    mensaje.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
                }
            }

        } catch (error) {
            console.error("🔥 ERROR:", error);

            if (mensaje) {
                mensaje.innerHTML = `<div class="alert alert-danger">Error del servidor</div>`;
            }
        }
    });

});