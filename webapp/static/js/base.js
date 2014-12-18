$(window).load(function(){
    $(document).foundation();
});

function openModal(product_id){
    $("#myModal").foundation('reveal', 'open');
    $("#product_price_wrapper").hide();
    $("#product_price_button").hide();
    $("#product_data").html("<br/><center><img src='/static/img/spinner.gif'></center><br/>");
    $.ajax({
       url: '/product/' + product_id + '/',
       success: function(response){
            $("#product_data").html(response);
            var pt = $("#id_product_type");
            pt.unbind('change');
            pt.on("change",function(){
                $("#modal_product_size").html("<center><img src='/static/img/spinner.gif'></center>");
                $("#product_price_wrapper").hide();
                $("#product_price_button").hide();
                if(pt.val()){
                    $.ajax({
                       url: '/product/' + product_id + '/type/' + pt.val() + '/',
                       method: "get",
                       type: 'json',
                       success: function(data) {
                              $("#product_price_wrapper").hide();
                              var html = "<select id='id_product_size'>";
                              html += '<option value="">-- product size --</option>';
                              $.each(data, function (i,item){
                                  html += '<option value="' + item.id + '">' + item.title + '</option>';
                              });
                              html += "</select>";
                              $("#modal_product_size").html(html);
                              var ps = $("#id_product_size");
                              ps.unbind("change");
                              ps.on("change", function(){
                                  $("#product_price_wrapper").hide();
                                  $("#product_price_button").hide();
                                  if(ps.val()){
                                      $.ajax({
                                          url: '/product/' + product_id + '/price/' + ps.val() + '/',
                                          method: "get",
                                          type: 'json',
                                          success: function (response){
                                              $("#id_product_item_id").val(ps.val());
                                              $("#product_price").html(response);
                                              $("#product_price_wrapper").show();
                                              $("#product_price_button").show();
                                          }
                                      })
                                  }
                              })
                       }
                    });
                }else{
                    $("#modal_product_size").html("");
                    $("#product_price_button").hide();
                }

            });
       }
    });
}