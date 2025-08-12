
// Obtener elementos
const addPhotoTourModal = document.getElementById("addPhotoTourModal");
const addPhotoTourModalBtn = document.getElementById("addPhotoTourModalBtn");
const closeAddPhotoTourModal = document.getElementById("closeAddPhotoTourModal");


// Abrir modal
addPhotoTourModalBtn.onclick = function() {
addPhotoTourModal.style.display = "block";
}

// Cerrar al hacer clic en la X
closeAddPhotoTourModal.onclick = function() {
addPhotoTourModal.style.display = "none";
}

// addPhotoTourModal.addEventListener('submit', function (e) {
//     e.preventDefault();

//     const formDataImageTour = new FormData(addPhotoTourModal);


// });


// Cerrar al hacer clic fuera del contenido
window.onclick = function(event) {
    if (event.target == addPhotoTourModal) {
        addPhotoTourModal.style.display = "none";
    }
}

