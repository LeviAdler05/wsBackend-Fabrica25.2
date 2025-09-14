$(document).ready(function(){
    $("#import-form").submit(function(e){
        e.preventDefault();
        let query = $("input[name='query']").val();
        let limit = $("input[name='limit']").val();
        $.ajax({
            url: $("#import-form").data("url"),
            data: {query: query, limit: limit},
            dataType: "json",
            success: function(data){
                $("#mensagem").html(`<div class="alert alert-success">Importados: ${data.salvos.join(", ")} (Total: ${data.total})</div>`);
                location.reload();
            },
            error: function(xhr, status, error){
                $("#mensagem").html(`<div class="alert alert-danger">Erro ao importar animes: ${error}</div>`);
            }
        });
    });
});
