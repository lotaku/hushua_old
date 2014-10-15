$(document).ready(function() {
    /*16ss 注册新用户*/
    $('body').on('click', '#btn', function() {

        $.ajax({
            type: "POST",
            url: '#ajax_test/',
            dataType:'json',
            async:true,
            data: {
                csrfmiddlewaretoken:'{{csrf_token}}'
            },
            success: function(data) {
                console.log(data);

                var data = $.parseJSON(data);
                console.log(data);
                if (data.state) {

                    $('#p').text("我是新数据");

                } else {
                    $('#p').text(data.errMsg);

                }
            }
        });
    });

//    /*16ss 注册新用户*/
//    $('body').on('click', '#user_register_btn2', function() {
//        $('.mask').show();
//        $('.msg').text("处理中...");
//        $.ajax({
//            type: "POST",
//            url: $('#user_register_form').attr('action'),
//            data: $('#user_register_form').serialize(),
//            success: function(data) {
//                console.log(data);
//
//                var data = $.parseJSON(data);
//                if (data.state) {
//                    var ticket = $.parseJSON(data.ticket);
//                    $('.msg').text("注册成功");
//                    setTimeout('$(".mask").fadeOut(1000)',1000);
//                    $('#showtic').hide();
//                } else {
//                    $('.msg').text(data.errMsg);
//                    setTimeout('$(".mask").fadeOut(1000)',1000);
//                }
//            }
//        });
//    });

});