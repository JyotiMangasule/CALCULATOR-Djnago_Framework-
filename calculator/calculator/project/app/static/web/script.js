// This function clear all the values
function clearScreen() {
    document.getElementById("result").value = "";
}

// This function display values
function display(value) {
    document.getElementById("result").value += value;
}

// This function evaluates the expression and returns result
function calculate() {
    var p = document.getElementById("result").value;
    var q = eval(p);
    document.getElementById("result").value = q;
}

// 

$("#btn_add").click(function (e) {
    //verification

    var formData = new FormData();
    formData.append("first", $("#first").val());
    formData.append("second", $("#second").val());
    formData.append("oper", $("#oper").val());
    formData.append("result", $("#result").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "add");

    // console.log(typeof(formData));

    $.ajax({
        beforeSend: function () {
            $(".btn .spinner-border").show();
            $("#btn_add").attr("disabled", true);
        },
        url: "/getCalcutaion/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (result) {

            alert("Result Saved Successfully");
            location.reload();
            $("#add_modal").modal('hide');

        },
        error: function (request, error) {
            console.error(error);
        },
        complete: function () {
            $(".btn .spinner-border").hide();
            $("#btn_add").attr("disabled", false);
        },
    });

});
