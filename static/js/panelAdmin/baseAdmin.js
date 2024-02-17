var $ = jQuery.noConflict();

function listarCategorias() {

    $.ajax({
        url: `/panelAdmin/panel/`,
        type: "get",
        dataType: "json",
        success: function (response) {
            $('#tabla_categoria tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i+1) +'</td>';
                fila += '<td>' + response[i]["fields"]['nombre'] + '</td>';
                fila += '<td>' + response[i]["fields"]['orden'] + '</td>';
                fila += '<td><a href="/menu/categorias/edit/' + response[i]["pk"] + '" class="btn btn-primary"  >Editar </a> <a href="/menu/categorias/eliminado/' + response[i]["pk"] + '" class="btn btn-danger"  >Eliminar </a></td>';
                
                fila += '</tr>';
                $('#tabla_categoria tbody').append(fila);
            }
            $('#tabla_categoria').DataTable({
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
    
    listarCategorias();
    
});
