function selectAll(source) {
    checkboxes = document.getElementsByName('ids');
    for (var i = 0, n = checkboxes.length; i < n; i++) {
        checkboxes[i].checked = source.checked;
    }   
}


function selectone(so) {
    checkboxes = document.getElementById('mainbox');
    unbox = document.getElementsByName('ids');
    var box = false;
    for (var i = 0, n = unbox.length; i < n; i++) {
        if (unbox[i].checked == true) {
            box = true;
        } else {
            box = false;
            break;
        }
    }
    checkboxes.checked = box;
}


$(function (){
    setTimeout(function(){
        $('#timeout').fadeOut(1000);
    }, 3000)
})