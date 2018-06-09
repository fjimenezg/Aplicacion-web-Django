$(document).ready(function () {
    $("#list_db").click(function () {
        $.ajax({
            url: $("#url").val(),
            type: "POST",
            data: $("#form_connection").serialize(),

            beforeSend: function () {
                $("#loader").show();
            },

            success: function (data) {
                $("#loader").hide();
                if (data.object_list) {
                    $("#alert_success").show().hide(2000);
                    disable_input_connecion();
                    $("#id_dbname").html("<option value='' selected disabled>Selecione una base de datos</option>");
                    data.object_list.forEach(element => {
                        $("#id_dbname").append(
                            "<option value='" + element + "'>" + element + "</option>"
                        );
                    });
                } else {
                    $("#loader").hide();
                    $("#alert_error").show().hide(2000);
                }
            },

            error: function () {
                $("#loader").hide();
                $("#alert_error").show().hide(2000);
            }
        });

    });

    $("#id_manager_db").change(function () {
        if ($(this).val() == "mysql") {
            $("#id_port").val(3306);
        }
    });

    $("#enable_edit").click(function () {
        $("#id_dbname").html("<option value='' selected disabled>Selecione una base de datos</option>");
        $("#button_list").show();
        $("#button_edit").hide();
        $("#id_connection_name").removeAttr('readonly');
        $("#id_manager_db").removeAttr('readonly');
        $("#id_port").removeAttr('readonly');
        $("#id_host").removeAttr('readonly');
        $("#id_user").removeAttr('readonly');
        $("#id_passwd").removeAttr('readonly');
    });


});

function disable_input_connecion() {
    $("#button_list").hide();
    $("#button_edit").show();
    $("#id_connection_name").attr('readonly', true);
    $("#id_manager_db").attr('readonly', true);
    $("#id_port").attr('readonly', true);
    $("#id_host").attr('readonly', true);
    $("#id_user").attr('readonly', true);
    $("#id_passwd").attr('readonly', true);
}

function check_connection(url) {
    $.ajax({
        url: url,
        type: "GET",

        beforeSend: function () {
            $("#loader").show();
        },

        success: function (data) {
            $("#loader").hide();
            if (data.object_list) {
                $("#alert_success").show().hide(2000);
                disable_input_connecion();
                $("#id_dbname").html("<option value='' selected disabled>Selecione una base de datos</option>");
                data.object_list.forEach(element => {
                    $("#id_dbname").append(
                        "<option value='" + element + "'>" + element + "</option>"
                    );
                });
            } else {
                $("#loader").hide();
                $("#alert_error").show().hide(2000);
            }
        },

        error: function () {
            $("#loader").hide();
            $("#alert_error").show().hide(2000);
        }
    });
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
