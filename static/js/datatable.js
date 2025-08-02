$(document).ready(function () {
    $('#tabla-ventas-general').DataTable({
        responsive: true,
        // columnDefs: [
        //     { responsivePriority: 1, targets: 0 },  // Nombre = siempre visible
        //     { responsivePriority: 1, targets: 1 },  // Correo = siguiente más importante
        //     { responsivePriority: 1, targets: 2 },  // Nombre = siempre visible
        //     { responsivePriority: 4, targets: 3 }, 
        //     { responsivePriority: 10000, targets: 4 } // Edad = menos importante
        // ],
        language: {
        url: "//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json"
        }
    });
});


// $(document).ready(function () {
//     $('#tabla-payments-general').DataTable({
//         responsive: true,
//         paging:false,
//         searching:false,
//         info:false,
//         // columnDefs: [
//         //     { responsivePriority: 1, targets: 0 },  // Nombre = siempre visible
//         //     { responsivePriority: 1, targets: 1 },  // Correo = siguiente más importante
//         //     { responsivePriority: 1, targets: 2 },  // Nombre = siempre visible
//         //     { responsivePriority: 4, targets: 3 }, 
//         //     { responsivePriority: 10000, targets: 4 } // Edad = menos importante
//         // ],
//         language: {
//         url: "//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json"
//         }
//     });
// });