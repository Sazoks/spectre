$(document).ready(function() {
    // Отправка формы с контактными данными через ajax.
    $('#contacts_form').submit(function() {
        $.ajax({
            url: 'http://127.0.0.1:8000/send_form/application/',
            method: 'post',
            dataType: 'html',
            data: $(this).serialize(),
            success: function(data) {
                alert('Заявка успешно отправлена');
            }
        });
        return false;
    })


    // Отправка формы для подписки на рассылку через ajax.
    $('#subscribe_form').submit(function() {
        $.ajax({
            url: 'http://127.0.0.1:8000/send_form/subscribe_to_news/',
            method: 'post',
            dataType: 'html',
            data: $(this).serialize(),
            success: function(data) {
                alert('Вы успешно подписались на уведомления');
            }
        });

        return false;
    })
})