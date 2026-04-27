document.addEventListener("DOMContentLoaded", function () {
    const moneyInputs = document.querySelectorAll(".money");
    
    function formatNumber(value) {
        // Separa los miles con puntos
        return value.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    }

    moneyInputs.forEach(input => {
        // Formato inicial si ya tiene valor
        if (input.value) {
            input.value = formatNumber(input.value.replace(/\D/g, ""));
        }

        input.addEventListener("input", function () {
            // 1. Elimina todo lo que NO sea número (bloquea letras)
            let raw = this.value.replace(/\D/g, "");
            
            if (raw === "") {
                this.value = "";
                return;
            }
            
            // 2. Aplica el formato de puntos
            this.value = formatNumber(raw);
        });
    });

    // Antes de enviar el formulario, quitar los puntos para que Django no de error
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function () {
            moneyInputs.forEach(input => {
                input.value = input.value.replace(/\./g, "");
            });
        });
    }
});