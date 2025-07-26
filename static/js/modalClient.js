
// Obtener elementos
const modalClient = document.getElementById("modalClient");
const modalClientBtn = document.getElementById("openModalClientBtn");
const closeModalClient = document.getElementById("closeModalClient");


// Abrir modal
modalClientBtn.onclick = function() {
modalClient.style.display = "block";
}

// Cerrar al hacer clic en la X
closeModalClient.onclick = function() {
modalClient.style.display = "none";
}

// saleForm.addEventListener('submit'
// )


// Cerrar al hacer clic fuera del contenido
window.onclick = function(event) {
    if (event.target == modalClient) {
        modalClient.style.display = "none";
    }
}

