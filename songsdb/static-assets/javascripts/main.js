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
