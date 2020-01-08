// $("#custom-timer").insertBefore($(".otree_timer"));

var hidden = parseFloat(document.getElementById("hidden_time").value) * 1000;
var timeToReach = new Date(hidden);
$('.timer_total').countdown(timeToReach, {elapse: true})
    .on('update.countdown', function (event) {
        if (!event.elapsed) {
            $(this).html(event.strftime('%M:%S'));
        }
        if (event.elapsed) {
            $(this).html(event.strftime('Expired'));
            $(":text").each(function () {
                if ($(this).val() === "") {
                    $(this).val("NULL")
                }
            });
            $('#form').submit();
        }
    });