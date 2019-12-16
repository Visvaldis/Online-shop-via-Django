$(document).ready(function () {
    var form = $('#form-buy');

    function basketUpdating(product_id, amount, price) {
        var data = {};
        data.product_id = product_id;
        data.amount = amount;
        data.price = price;
        var csrf_token = $('#form-buy [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");
        console.log(data);
        $.ajax(url, {
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
            },
            error: function () {
                console.log("error")
            }
        })

    }


    form.on('submit', function (e) {
        e.preventDefault();
        var tmp = $('#quantity').val();
        var amount = tmp.substr(0, tmp.length - 3);
        console.log(amount);
        var button = $('#button-buy');
        var product_id = button.data('product_id');
        var price = button.data('price');
        console.log(product_id);

        basketUpdating(product_id, amount, price)
    })
});