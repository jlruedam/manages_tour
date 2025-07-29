
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

    e.preventDefault();

    const formData = new FormData(saleForm);
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const url = saleForm.dataset.url;

    try {
        const response = await fetch(url, {
            method: 'POST',
            body: formData,
            credentials: 'same-origin',
            headers: {
                'X-CSRFToken': csrfToken
            }
        });

        const data = await response.json();

        console.log(data);

        alert(data);
        // if (data.success) {
        //     console.log('Venta')
        // } else {
        //     alert(data.message || "Hubo un error al crear el cliente.");
        // }
        location.reload();

    } catch (error) {
        console.error("Error al enviar el formulario:", error);
        alert("Ocurrió un error inesperado.");
    }

});


// Cerrar al hacer clic fuera del contenido
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

