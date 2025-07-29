
// Obtener elementos
const modal = document.getElementById("myModal");
const btn = document.getElementById("openModalBtn");
const closeModal = document.getElementById("closeModal");;
const saleForm = document.getElementById("saleForm");

// Abrir modal
btn.onclick = function() {
modal.style.display = "block";
}

// Cerrar al hacer clic en la X
closeModal.onclick = function() {
modal.style.display = "none";
}

saleForm.addEventListener('submit', async (e) => {

    
});


// Cerrar al hacer clic fuera del contenido
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

