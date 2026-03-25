$(function () {
  // 🔹 Inicialización del DataTable sobre la tabla con ID #example1
  $("#example1").DataTable({
    "responsive": true,   // Habilita que la tabla sea adaptable a distintos tamaños de pantalla (responsive design)
    "lengthChange": false, // Oculta el selector que permite cambiar el número de registros por página
    "autoWidth": true, // Ajusta automáticamente el ancho de las columnas
    "lengthMenu": [10, 25, 100], // Opciones disponibles para elegir cuántos registros mostrar por página
    "pageLength": 10, // Cantidad de registros que se mostrarán por defecto al cargar la tabla
    "order": [[0, "desc"]],  // Ordenar la tabla por la PRIMERA columna (índice 0) en orden descendente

    // 🔹 Traducción de los textos al español
    "language": {
      "sProcessing": "Procesando...",
      "sLengthMenu": "Mostrar _MENU_ registros",
      "sZeroRecords": "No se encontraron resultados",
      "sEmptyTable": "Ningún dato disponible en esta tabla",
      "sInfo": "_START_ al _END_ de _TOTAL_ registros",
      "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
      "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
      "sSearch": "Buscar:", // Texto de la caja de búsqueda
      "sLoadingRecords": "Cargando...",
      "oPaginate": {
        "sFirst": "Primero",
        "sLast": "Último",
        "sNext": "Siguiente",
        "sPrevious": "Anterior"
      }
    },
    // 🔹 Personaliza la estructura del DOM (dónde se colocan los elementos de búsqueda, tabla y paginación)
    // En este caso:
    //   f → filtro de búsqueda arriba
    //   r → información del procesado
    //   t → tabla
    //   i → información de los registros
    //   p → paginación
    // Con estilos Bootstrap: búsqueda alineada arriba a la derecha con margen inferior
    dom: '<"d-flex justify-content-between align-items-center mb-3"f>rtip'
  });

  // 🔹 Inicialización del DataTable sobre la tabla con ID #example2 para poder ordenar detalleRequerimiento.html
  $("#example2").DataTable({
    "responsive": true,   // Habilita que la tabla sea adaptable a distintos tamaños de pantalla (responsive design)
    "lengthChange": false, // Oculta el selector que permite cambiar el número de registros por página
    "autoWidth": true, // Ajusta automáticamente el ancho de las columnas
    "lengthMenu": [10, 25, 100], // Opciones disponibles para elegir cuántos registros mostrar por página
    "pageLength": 10, // Cantidad de registros que se mostrarán por defecto al cargar la tabla
    "order": [[0, "asc"]],  // Ordenar la tabla por la PRIMERA columna (índice 0) en orden ascendente
    columnDefs: [
      { targets: [0], visible: false } // 👉 oculta la primera columna (Id)
    ],

    // 🔹 Traducción de los textos al español
    "language": {
      "sProcessing": "Procesando...",
      "sLengthMenu": "Mostrar _MENU_ registros",
      "sZeroRecords": "No se encontraron resultados",
      "sEmptyTable": "Ningún dato disponible en esta tabla",
      "sInfo": "_START_ al _END_ de _TOTAL_ registros",
      "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
      "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
      "sSearch": "Buscar:", // Texto de la caja de búsqueda
      "sLoadingRecords": "Cargando...",
      "oPaginate": {
        "sFirst": "Primero",
        "sLast": "Último",
        "sNext": "Siguiente",
        "sPrevious": "Anterior"
      }
    },
    dom: '<"d-flex justify-content-between align-items-center mb-3"f>rtip'
  });


});
