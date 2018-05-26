$(document).ready(function () {
    $("#listar_bd").click(function () {
        $.ajax({
            url: $("#url").val(),
            type: "POST",
            data: $("#form_connection").serialize(),
            success: function (datos) {
                $("#selector_bd").html(datos);
            }
        });
    });

    $("#list_db").click(function (evt) {
        evt.preventDefault();
        $.ajax({
            url: $("#url").val(),
            type: "POST",
            data: $("#form_connection").serialize(),
            success: function (data) {
                if (data.object_list) {
                    disable_input_connecion();
                    $("#alert_success").show().hide(2000);
                    $("#id_dbname").html("");
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
        if ($(this).val() == "mysql") {
            $("#id_port").val(3306);
        }
    });
});

function disable_input_connecion() {
    $("#button_list").hide();
    $("#button_edit").show();
    $("#id_connection_name").attr('disabled',true);
    $("#id_manager_db").attr('disabled',true);
    $("#id_port").attr('disabled',true);
    $("#id_host").attr('disabled',true);
    $("#id_user").attr('disabled',true);
    $("#id_passwd").attr('disabled',true);
}

function enable_input_connection() {
    $("#button_list").show();
    $("#button_edit").hide();
    $("#id_connection_name").attr('disabled',false);
    $("#id_manager_db").attr('disabled',false);
    $("#id_port").attr('disabled',false);
    $("#id_host").attr('disabled',false);
    $("#id_user").attr('disabled',false);
    $("#id_passwd").attr('disabled',false);
}

function check_delete_connection(url, nombre, motor, usuario) {
    $("#spn_nombre").html(nombre);
    $("#spn_motor").html(motor);
    $("#spn_usuario").html(usuario);
    $("#form_confirmacion").attr('action', url);
    $("#mostrarmodal").modal("show");
}

function validar_eliminacion_servicio(url, nombre, rol, descripcion) {
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
}
