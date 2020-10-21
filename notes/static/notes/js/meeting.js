
$( document ).ready(function() {
    var SubheaderBlock = document.getElementsByClassName("SubheaderBlock");
    var SubsubheaderBlock = document.getElementsByClassName("SubsubheaderBlock");

    for (var i = 0; i < SubheaderBlock.length; i ++){
        SubheaderBlock[i].className += "lead";
    }

    for (var i = 0; i < SubsubheaderBlock.length; i ++){
        SubsubheaderBlock[i].className += "lead";
    }

})