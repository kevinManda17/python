 // check if button pressed 
 $(document).on('click', '#add-cart', function(e){
    e.preventDefault();
    $.ajax({
        type :'POST',
        url:"{% url 'cart_add'%}",
        data:{
            product_id : $('#add-cart').val(),
            csrfmiddlewaretoken: '{{ csrf_token }}' ,
            action :'post',

        },
        success: function(json){
            console.log(json)
            document.getElementById('#cart_quantity').textContent= json.Qty
        },
        error : function(xhr , errmsg , err){

        }
    });
})