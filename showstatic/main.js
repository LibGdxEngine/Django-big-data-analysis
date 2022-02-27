$(document).ready(function () {
    $('.ui.dropdown')
        .dropdown()
    $('.message .close')
        .on('click', function () {
            $(this)
                .closest('.message')
                .transition('fade')
            ;
        })
    ;



    $("#model-btn").click(function () {
        $('.ui.modal')
            .modal('show')
        ;
    });

});