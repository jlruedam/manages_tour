const getClientList = async (e) => {
    url = "/api/clients/";
    try {
        const response = await fetch(url, {
            method: 'GET',
            credentials: 'same-origin',
            // headers: {
            //     'X-CSRFToken': csrfToken
            // }
        });

        const data = await response.json();
        console.log("LOS CLIENTES SON:", data);
        $('#tabla-clients-general').DataTable({
            data: data,
            columns: [
                { data: 'id' },
                { data: 'num_doc' },
                { data: 'type_doc' },
                { data: 'name' },
                { data: 'city' },
                { 
                    data: null,
                    render: function (data, type, row) {
                        return `
                            <button class="editar" >Editar</button>
                            <button class="eliminar" >Ver</button>
                        `;
                    }
                }
            ]
        });


        
       
    } catch (error) {
        console.error("Error al enviar el formulario:", error);
        alert("Ocurrió un error inesperado.");
    }
}