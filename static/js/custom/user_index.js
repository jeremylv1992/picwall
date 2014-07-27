window.onload = function () {
	$(".cancel-btn").click(function() {
		var mid = $(this).next().attr("value");
		$.ajax({ url : CANCEL_MSG,
			type: "POST",
			data : {"mid":mid},
			success: function(data){
				alert(data);
		}});
		$(this).parent().parent().remove();
		var cur = $("#num-of-msgs").text()-1;
		$("#num-of-msgs").text(cur);
	});
};
