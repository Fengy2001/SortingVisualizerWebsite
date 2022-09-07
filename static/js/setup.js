// $(document).ready(function(){
//     $.ajax({
//         type: 'GET',
//         url : 'testList',
//         success: function(response) {
//             console.log(typeof response.testVector[0]);
//             $("#display").empty();
//             var temp = "" + response.testVector[0] + response.testVector[1] + response.testVector[2];
//             $("#display").append(temp);
//         },
//         error: function(response) {
//             alert("Error");
//         }
//     });
// })

$(document).on("click", function(asshole){

    asshole.preventDefault();

    $.ajax({
        type: 'POST',
        url: 'testPost',
        data: {input: $('#inputValue').val(), csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()}
    });
})