$(document).ready(function(){
    $.ajax({
        type: 'GET',
        url : $("#url").attr("data-url"),
        success: function(response) {
            console.log(typeof response.testVector[0]);
            $("#display").empty();
            var temp = "" + response.testVector[0] + response.testVector[1] + response.testVector[2];
            $("#display").append(temp);
        },
        error: function(response) {
            alert("Error");
        }
    });
})