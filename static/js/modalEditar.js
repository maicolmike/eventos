document.addEventListener("DOMContentLoaded", () => {

    // REFERENCIAS A ELEMENTOS HTML
    const modal = document.getElementById("modalEditar"); // Modal completo
    const form = document.getElementById("formEditarUsuario"); // Formulario
    const mensaje = document.getElementById("mensajeEditar"); // Contenedor de mensajes

    // LISTA DE CAMPOS QUE VAMOS A LLENAR AUTOMÁTICAMENTE DESDE LOS ATRIBUTOS data-* DEL BOTÓN "EDITAR"
    const campos = ["id", "identificacion", "nombres", "username", "email", "agencia"]; // Esto evita repetir muchas líneas de código

    // EVENTO: CUANDO DAN CLICK EN "EDITAR"
    document.querySelectorAll(".btn-editar").forEach(btn => {
        btn.addEventListener("click", () => {
            // Recorremos cada campo y lo llenamos automáticamente
            campos.forEach(campo => { 
                const input = document.getElementById(`edit_${campo}`); // Construye el id dinámicamente: edit_nombre, edit_email, etc.
                input.value = btn.dataset[campo] || "";  // Asigna el valor desde los atributos data-* del botón
            });

            // MANEJO DE BOOLEANOS (True / False) - convertimos a "1" o "0" para los campos de tipo booleano
            document.getElementById("edit_superuser").value = btn.dataset.superuser === "True" ? "1" : "0";
            document.getElementById("edit_active").value = btn.dataset.active === "True" ? "1" : "0";

            // Limpia mensajes anteriores
            mensaje.innerHTML = "";  
        });
    });

    // EVENTO: ENVÍO DEL FORMULARIO (AJAX)
    form.addEventListener("submit", async (e) => {
        e.preventDefault(); // Evita que la página se recargue (CLAVE para AJAX)
        mensaje.innerHTML = `<div class="alert alert-info">Guardando...</div>`; // Mensaje de carga mientras se envía la información

        try {
            // CAPTURAR DATOS DEL FORMULARIO
            const formData = new FormData(form);

            // ENVIAR DATOS A DJANGO (FETCH = AJAX)
            const url = form.getAttribute("data-url"); // ✅ CAMBIO CLAVE: Obtenemos la URL desde el atributo data-url del form
            const response = await fetch(url, { // Usamos la URL dinámica obtenida del atributo data-url
            //const response = await fetch("{% url 'user_update_ajax' %}", {   // cuando no usamos data-url, ponemos la URL directamente aquí, pero es menos flexible
                method: "POST",
                body: formData,
                // Token de seguridad requerido por Django
                headers: {
                    "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            });
            // Convertir respuesta a JSON
            const data = await response.json();

            // MANEJO DE RESPUESTA DEL SERVIDOR
            if (data.status === "success") {
                mensaje.innerHTML = `<div class="alert alert-success">${data.message}</div>`;  // Mostrar mensaje de éxito

                // Esperar un momento antes de cerrar el modal
                setTimeout(() => {
                    bootstrap.Modal.getInstance(modal).hide();  // Cerrar modal
                    location.reload(); // Recargar la página para ver cambios (puede mejorarse)
                }, 1000);

            } else {
                // Mostrar error si algo falló (ej: usuario duplicado)
                mensaje.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
            }

        } catch (error) {
            // ERROR DE CONEXIÓN O FALLA DEL SERVIDOR
            mensaje.innerHTML = `<div class="alert alert-danger">Error de conexión con el servidor</div>`;
            console.error("Error:", error);
        }
    });

});