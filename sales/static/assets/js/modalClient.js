// Obtener elementos
const modalClient = document.getElementById("modalClient");
const modalClientBtn = document.getElementById("openModalClientBtn");
const closeModalClient = document.getElementById("closeModalClient");
const formCreateClient = document.getElementById("formCreateClient");
const clientOptions = document.getElementById("clientOptions"); // datalist
const cityOptions = document.getElementById("cityOptions"); // datalist
const inputClient = document.getElementById("input_client");
const inputCountry = document.getElementById("input_country");
const inputCity= document.getElementById("input_city");
// Abrir modal

if(modalClientBtn){
    modalClientBtn.onclick = function () {
        modalClient.style.display = "block";
    }
}


// Cerrar al hacer clic en la X
if(closeModalClient){
    closeModalClient.onclick = function () {
        modalClient.style.display = "none";
    }
}

if(inputCountry){
    inputCountry.addEventListener('change', async(e)=>{
        let country = inputCountry.value.split("-");
        inputCity.value = "";
        cityOptions.innerHTML = "";
        const url = `/api/cities/?country=${country[0]}`;
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        try {
            const response = await fetch(url, {
                method: 'GET',
                credentials: 'same-origin',
                headers: {
                    'X-CSRFToken': csrfToken
                }
            });

            const data = await response.json();
            
            
            // Crear nueva opción en el datalist
            for(city of data){
                // console.log(city)
                const newOption = document.createElement("option");
                newOption.value = `${city.id}-${city.name}`;
                cityOptions.appendChild(newOption);
            }
            

        
        } catch (error) {
            console.error("Error al enviar el formulario:", error);
            alert("Ocurrió un error inesperado.");
        }
    });

}


// Enviar formulario sin recargar la página
if(formCreateClient){
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

}
