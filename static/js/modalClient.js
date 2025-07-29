// Obtener elementos
const modalClient = document.getElementById("modalClient");
const modalClientBtn = document.getElementById("openModalClientBtn");
const closeModalClient = document.getElementById("closeModalClient");
const formCreateClient = document.getElementById("formCreateClient");
const clientOptions = document.getElementById("clientOptions"); // datalist
const inputClient = document.getElementById("input_client");

// Abrir modal
modalClientBtn.onclick = function () {
    modalClient.style.display = "block";
}

// Cerrar al hacer clic en la X
closeModalClient.onclick = function () {
    modalClient.style.display = "none";
}

// Enviar formulario sin recargar la página
formCreateClient.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(formCreateClient);
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const url = formCreateClient.dataset.url;

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
            alert(data.message || "Cliente creado correctamente");

            // Crear nueva opción en el datalist
            const newOption = document.createElement("option");
            newOption.value = `${data.client.num_doc}-${data.client.name}`;
            clientOptions.appendChild(newOption);

            // Establecer el valor del input con el nuevo cliente
            inputClient.value = newOption.value;

            formCreateClient.reset();
            modalClient.style.display = "none";
        } else {
            alert(data.message || "Hubo un error al crear el cliente.");
        }

    } catch (error) {
        console.error("Error al enviar el formulario:", error);
        alert("Ocurrió un error inesperado.");
    }
});
