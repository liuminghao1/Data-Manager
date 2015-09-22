$(document).ready(function() {
    $('button').click(function(){
	var  scores , tasks;
	scores = $(this).attr("data-score");
	tasks = $(this).attr("data-task");
	$.get('/shop/add_score/', {score_id: scores,task_id: tasks}, function(data){
		$('#test2').html(data);  
		$('button').hide();
	});

    });

});

