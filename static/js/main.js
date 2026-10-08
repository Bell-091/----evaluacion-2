/**
 * Script de interactividad para CineHub
 */
document.addEventListener('DOMContentLoaded', () => {
    // Tooltips de Bootstrap inicializados
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    console.log("CineHub - Proyecto Django Evaluación 2 cargado correctamente.");
});
