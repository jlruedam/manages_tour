
// Obtener elementos
const modalVendor = document.getElementById("modalVendor");
const modalVendorBtn = document.getElementById("openModalVendorBtn");
const closeModalVendor = document.getElementById("closeModalVendor");


// Abrir modal
modalVendorBtn.onclick = function() {
modalVendor.style.display = "block";
}

// Cerrar al hacer clic en la X
closeModalVendor.onclick = function() {
modalVendor.style.display = "none";
}

// saleForm.addEventListener('submit'
// )


// Cerrar al hacer clic fuera del contenido
window.onclick = function(event) {
    if (event.target == modalVendor) {
        modalVendor.style.display = "none";
    }
}

