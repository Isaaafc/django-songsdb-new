$(document).ready(function(){
    $(".toggleAuthor").click(function(){
        $("#field_id_author").toggle();
	$("#field_id_author").val('');
	$("#field_id_author_choice").val('');
	$("#field_id_author_choice").toggle();
    });
    $(".togglePublisher").click(function(){
        $("#field_id_publisher").toggle();
	$("#field_id_publisher_choice").toggle();
        $("#field_id_publisher").val('');
	$("#field_id_publisher_choice").val('');
    });
    $(".toggleType").click(function(){
        $("#field_id_song_type").toggle();
	$("#field_id_type_choice").toggle();
        $("#field_id_song_type").val('');
	$("#field_id_type_choice").val('');
    });    
});


