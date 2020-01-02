var hidden = parseFloat(document.getElementById("hidden_time").value) * 1000;
var timeToReach = new Date(hidden);
$('.timer_total').countdown(timeToReach, {elapse: true})
    .on('update.countdown', function (event) {
        $(this).html(event.strftime('%M:%S'));
        //$(this).html(event.strftime('<p>Time left for this task: <span style="font-weight: bold">%M:%S</span></p>'));
        if (event.elapsed) {
            $(":text").each(function () {
                if ($(this).val() === "") {
                    $(this).val("NULL")
                }
            });
            $('#form').submit();
        }
    });
/*$('#clock_total').countdown(timeToReach, function (event) {
    $(this).html(event.strftime('%M:%S'));
});*/