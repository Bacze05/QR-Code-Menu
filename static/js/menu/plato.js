var $ = jQuery.noConflict();

function listarPlatos() {

    $.ajax({
        url: `/menu/platolist/`,
        type: "get",
        dataType: "json",
        success: function (response) {
            $('#tabla_plato tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i+1) +'</td>';
                fila += '<td>' + response[i]["fields"]['nombre'] + '</td>';
                fila += '<td>' + response[i]["fields"]['descripcion'] + '</td>';
                fila += '<td>' + "$" + response[i]["fields"]['precio'] + '</td>';
                fila += '<td><a href="/menu/plato/edit/' + response[i]["pk"] + '" class="btn btn-primary"  >Editar </a> <a href="/menu/plato/eliminado/' + response[i]["pk"] + '" class="btn btn-danger"  >Eliminar </a></td>';
                
                fila += '</tr>';
                $('#tabla_plato tbody').append(fila);
            }
            $('#tabla_plato').DataTable({
                language: {
                    decimal: "",
                    emptyTable: "No hay información",
                    info: "",
                    infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
                    infoFiltered: "(Filtrado de MAX total entradas)",
                    infoPostFix: "",
                    thousands: ",",
                    lengthMenu: "",
                    loadingRecords: "Cargando...",
                    processing: "Procesando...",
                    search: "Buscar:",
                    zeroRecords: "Sin resultados encontrados",
                    paginate: {
                      first: "Primero",
                      last: "Ultimo",
                      next: "Siguiente",
                      previous: "Anterior",
                    },
                  },
                  
                pageLength: 6,
                columnDefs: [
                    { targets: [ 0,2, 3], searchable: false }  // Desactiva la búsqueda para las columnas 0, 2 y 3
                ],
            });
        },
        error: function (error) {
            console.error("Error al obtener categorias:", error.responseText);
        }
    });
}


$(document).ready(function () {
    
    listarPlatos();
    
});
