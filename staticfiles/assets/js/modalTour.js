
// Obtener elementos
const modalTour = document.getElementById("modalTour");
const modalTourBtn = document.getElementById("openModalTourBtn");
const closeModalTour = document.getElementById("closeModalTour");


// Abrir modal
modalTourBtn.onclick = function() {
modalTour.style.display = "block";
}

// Cerrar al hacer clic en la X
closeModalTour.onclick = function() {
modalTour.style.display = "none";
}

// saleForm.addEventListener('submit'
// )


// Cerrar al hacer clic fuera del contenido
window.onclick = function(event) {
    if (event.target == modalTour) {
        modalTour.style.display = "none";
    }
}

