// Elementos para el modal de Jalador
const modalReferrer = document.getElementById("modalReferrer");
const modalReferrerBtn = document.getElementById("openModalReferrerBtn");
const closeModalReferrer = document.getElementById("closeModalReferrer");
const formCreateReferrer = document.getElementById("formCreateReferrer");

// Abrir modal
modalReferrerBtn.onclick = function () {
    modalReferrer.style.display = "block";
}

// Cerrar al hacer clic en la X
closeModalReferrer.onclick = function () {
    modalReferrer.style.display = "none";
}

// Enviar formulario sin recargar la página
formCreateReferrer.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(formCreateReferrer);
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const url = formCreateReferrer.dataset.url;

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

        if (data.success) {
            alert(data.message || "Jalador creado correctamente");

            // Agregar nuevo jalador al datalist
            const referrerOptions = document.getElementById("referrerOptions");
            const newOption = document.createElement("option");
            newOption.value = `${data.referrer.num_doc}-${data.referrer.name}`;
            referrerOptions.appendChild(newOption);

            formCreateReferrer.reset();
            modalReferrer.style.display = "none";
        } else {
            alert(data.message || "Hubo un error al crear el jalador.");
        }

    } catch (error) {
        console.error("Error al enviar el formulario:", error);
        alert("Ocurrió un error inesperado.");
    }
});
