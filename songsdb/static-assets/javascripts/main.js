function toggleFieldElement(target, buttonId) {
        if (document.getElementById(buttonId).innerHtml == 'Choose from list') {
		document.getElementById(target).style.display = 'none';
        	document.getElementById(buttonId).innerHtml = '+';
	} else {
		document.getElementById(target).style.display = 'block';
                document.getElementById(buttonId).innerHtml = 'Choose from list';
	}
}

function showElement(target){
	document.getElementById(target).style.display = 'block';
}

var $rows = $('#keywords>tbody>tr');
$('#search').keyup(function() {
    var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase();
    
    $rows.show().filter(function() {
        var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
        return !~text.indexOf(val);
    }).hide();
});