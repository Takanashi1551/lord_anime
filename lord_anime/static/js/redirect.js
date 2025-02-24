document.addEventListener("DOMContentLoaded", function() {
    // Obtiene la URL de redirección desde un atributo de la plantilla
    let redirectUrl = document.getElementById("redirect-data")?.getAttribute("data-url");

    if (redirectUrl) {
        window.location.href = redirectUrl;
    }
});