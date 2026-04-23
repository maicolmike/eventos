document.addEventListener("DOMContentLoaded", () => {

    const modal = document.getElementById("modalEditarPremio");
    const form = document.getElementById("formEditarPremio");
    const mensaje = document.getElementById("mensajeEditarPremio");

    const campos = [
        "id",
        "nombres",
        "apellidos",
        "identificacion",
        "agencia",
        "categoria",
        "puesto_numero",
        "valor_premio"
    ];

    document.querySelectorAll(".btn-editar-premio").forEach(btn => {
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
                    bootstrap.Modal.getInstance(modal).hide();
                    location.reload();
                }, 800);

            } else {
                mensaje.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
            }

        } catch (error) {
            mensaje.innerHTML = `<div class="alert alert-danger">Error de conexión</div>`;
        }
    });

});