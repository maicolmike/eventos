<script>
document.addEventListener("DOMContentLoaded", () => {

    // ================================
    // 🔹 REFERENCIAS A ELEMENTOS HTML
    // ================================
    const modal = document.getElementById("modalEditar"); // Modal completo
    const form = document.getElementById("formEditarUsuario"); // Formulario
    const mensaje = document.getElementById("mensajeEditar"); // Contenedor de mensajes

    // =====================================
    // 🔹 LISTA DE CAMPOS QUE VAMOS A LLENAR
    // =====================================
    // Esto evita repetir muchas líneas de código
    const campos = [
        "id",
        "identificacion",
        "nombres",
        "username",
        "email",
        "agencia"
    ];

    // ==========================================
    // 🔹 EVENTO: CUANDO DAN CLICK EN "EDITAR"
    // ==========================================
    document.querySelectorAll(".btn-editar").forEach(btn => {

        btn.addEventListener("click", () => {

            // Recorremos cada campo y lo llenamos automáticamente
            campos.forEach(campo => {

                // Construye el id dinámicamente: edit_nombre, edit_email, etc.
                const input = document.getElementById(`edit_${campo}`);

                // Asigna el valor desde los atributos data-* del botón
                input.value = btn.dataset[campo] || "";
            });

            // ==========================================
            // 🔹 MANEJO DE BOOLEANOS (True / False)
            // ==========================================
            // Django envía "True" o "False", pero el select usa "1" o "0"
            document.getElementById("edit_superuser").value =
                btn.dataset.superuser === "True" ? "1" : "0";

            document.getElementById("edit_active").value =
                btn.dataset.active === "True" ? "1" : "0";

            // Limpia mensajes anteriores
            mensaje.innerHTML = "";
        });
    });

    // ==========================================
    // 🔹 EVENTO: ENVÍO DEL FORMULARIO (AJAX)
    // ==========================================
    form.addEventListener("submit", async (e) => {

        // Evita que la página se recargue (CLAVE para AJAX)
        e.preventDefault();

        // Mensaje de carga mientras se envía la información
        mensaje.innerHTML = `<div class="alert alert-info">Guardando...</div>`;

        try {
            // ==========================================
            // 🔹 CAPTURAR DATOS DEL FORMULARIO
            // ==========================================
            const formData = new FormData(form);

            // ==========================================
            // 🔹 ENVIAR DATOS A DJANGO (FETCH = AJAX)
            // ==========================================
            const response = await fetch("{% url 'user_update_ajax' %}", {
                method: "POST",
                body: formData,

                // Token de seguridad requerido por Django
                headers: {
                    "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            });

            // Convertir respuesta a JSON
            const data = await response.json();

            // ==========================================
            // 🔹 MANEJO DE RESPUESTA DEL SERVIDOR
            // ==========================================
            if (data.status === "success") {

                // Mostrar mensaje de éxito
                mensaje.innerHTML = `<div class="alert alert-success">${data.message}</div>`;

                // Esperar un momento antes de cerrar el modal
                setTimeout(() => {

                    // Cerrar modal
                    bootstrap.Modal.getInstance(modal).hide();

                    // Recargar la página para ver cambios (puede mejorarse)
                    location.reload();

                }, 1000);

            } else {
                // Mostrar error si algo falló (ej: usuario duplicado)
                mensaje.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
            }

        } catch (error) {
            // ==========================================
            // 🔹 ERROR DE CONEXIÓN O FALLA DEL SERVIDOR
            // ==========================================
            mensaje.innerHTML = `<div class="alert alert-danger">Error de conexión con el servidor</div>`;

            console.error("Error:", error);
        }
    });

});
</script>