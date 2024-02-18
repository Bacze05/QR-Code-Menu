$(document).ready(function() {
    $('#qr_form').submit(function(event) {
        event.preventDefault(); // Evitar que el formulario se envíe normalmente

        var qr_content = $('#qr_content').val();

        $.ajax({
            url: '/generar-qr/', // URL de la vista que genera el QR
            type: 'POST',
            data: {
                'qr_content': qr_content
            },
            success: function(response) {
                // Insertar la imagen del código QR en el HTML
                $('#qr_code').html('<img src="data:image/png;base64,' + response.qr_img_base64 + '">');
            },
            error: function(xhr, status, error) {
                console.error('Error al generar el código QR:', error);
            }
        });
    });
});
