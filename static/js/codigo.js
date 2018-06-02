$(document).ready(function () {

    $("#list_db").click(function () {
        $.ajax({
            url: $("#url").val(),
            type: "POST",
            data: $("#form_connection").serialize(),
            beforeSend: function(){
                $("#loader").show(); 
            },
            success: function (data) {
                $("#loader").hide();
                $("#id_dbname").html("<option value='' selected disabled>Selecione una base de datos</option>");
                if (data.object_list) {
                    disable_input_connecion();
                    $("#alert_success").show().hide(2000);
                    data.object_list.forEach(element => {
                        $("#id_dbname").append(
                            "<option value='"+element+"'>"+element+"</option>"
                        );
                    });
                } else {
                    $("#alert_error").show().hide(2000);;
                }
            }
        });
    });

    $("#id_manager_db").change(function () {
        $("#button_list").show();
        $("#button_edit").hide();
        enable_input_connection();
        if ($(this).val() == "mysql") {
            $("#id_port").val(3306);
        }
    });

});

function disable_input_connecion() {
    $("#button_list").hide();
    $("#button_edit").show();
    $("#id_connection_name").attr('readonly',true);
    $("#id_manager_db").attr('readonly',true);
    $("#id_port").attr('readonly',true);
    $("#id_host").attr('readonly',true);
    $("#id_user").attr('readonly',true);
    $("#id_passwd").attr('readonly',true);
}

function enable_input_connection() {
    $("#button_list").show();
    $("#button_edit").hide();
    $("#id_connection_name").attr('readonly',false);
    $("#id_manager_db").attr('readonly',false);
    $("#id_port").attr('readonly',false);
    $("#id_host").attr('readonly',false);
    $("#id_user").attr('readonly',false);
    $("#id_passwd").attr('readonly',false);
}

function check_delete_connection(url, nombre, motor, usuario) {
    $("#spn_nombre").html(nombre);
    $("#spn_motor").html(motor);
    $("#spn_usuario").html(usuario);
    $("#form_confirmacion").attr('action', url);
    $("#mostrarmodal").modal("show");
}

/*function validar_eliminacion_servicio(url, nombre, rol, descripcion) {
    $("#spn_nombre").html(nombre);
    $("#spn_rol").html(rol);
    $("#spn_descripcion").html(descripcion);
    $("#form_confirmacion").attr('action', url);
    $("#mostrarmodal").modal("show");
}

function validar_eliminacion_directorio(url, dependencia, extension, linea_directa) {
    $("#spn_dependencia").html(dependencia);
    $("#spn_extension").html(extension);
    $("#spn_linea_directa").html(linea_directa);
    $("#form_confirmacion").attr('action', url);
    $("#mostrarmodal").modal("show");
}

function validar_eliminacion_articulo(url, descripcion, fecha) {
    $("#spn_descripcion").html(descripcion);
    $("#spn_fecha").html(fecha);
    $("#form_confirmacion").attr('action', url);
    $("#mostrarmodal").modal("show");
}

function validar_eliminacion_localizacion(url, descripcion, longitud, latitud) {
    $("#spn_descripcion").html(descripcion);
    $("#spn_longitud").html(longitud);
    $("#spn_latitud").html(latitud);
    $("#form_confirmacion").attr('action', url);
    $("#mostrarmodal").modal("show");
}*/
