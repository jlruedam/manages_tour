
// Obtener elementos
const modalReferrer = document.getElementById("modalReferrer");
const modalReferrerBtn = document.getElementById("openModalReferrerBtn");
const closeModalReferrer = document.getElementById("closeModalReferrer");


// Abrir modal
modalReferrerBtn.onclick = function() {
modalReferrer.style.display = "block";
}

// Cerrar al hacer clic en la X
closeModalReferrer.onclick = function() {
modalReferrer.style.display = "none";
}

// saleForm.addEventListener('submit'
// )


// Cerrar al hacer clic fuera del contenido
window.onclick = function(event) {
    if (event.target == modalReferrer) {
        modalReferrer.style.display = "none";
    }
}

