
$(function() {

    $(".act_like").on("click", function (e) {
        e.preventDefault();
        var o = $(this);
        $.ajax({
            method: "GET",
            url: "/like/{id}".replace("{id}", o.attr("data-personid")),
            success: function (data) {
                var o = $("#person_likes");
                o.addClass("swing").html(data['likes']);
                window.setTimeout(function () {
                    o.removeClass("swing");
                }, 1000);
            }
        })
    });

    $(".act_dislike").on("click", function (e) {
        e.preventDefault();
        var o = $(this);
        $.ajax({
            method: "GET",
            url: "/dislike/{id}".replace("{id}", o.attr("data-personid")),
            success: function (data) {
                var o = $("#person_dislikes");
                o.addClass("swing").html(data['dislikes']);
                window.setTimeout(function () {
                    o.removeClass("swing");
                }, 1000);
            }
        })
    });

});