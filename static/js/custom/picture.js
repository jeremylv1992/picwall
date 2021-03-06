﻿window.onload = function () {
	$("#upload-warn").hide();
	$("#photo-submit-btn").click(function () {
		var title = $("#img-title").val();
		if (title != "") {
			$("#photo-form").submit();
		} else {
			$('#upload-warn').show();
		}
	});

	$("#upload-warn-cancel-btn").click(function() {
		$("#upload-warn").hide();
	});

	$("#edit-warn").hide();
	$("#edit-submit-btn").click(function () {
		var title = $("#edit-title").val();
		if (title != "") {
			$("#edit-form").submit();
		} else {
			$('#edit-warn').show();
		}
	});

	$("#edit-warn-cancel-btn").click(function() {
		$("#edit-warn").hide();
	});

	$("#label-warn").hide();
	$("#add-label-btn").click(function(){
		var name = $("#new-label").val();
		if (name != "") {
			$("#add-label-form").submit();
		} else {
			$("#label-warn").show();
		}
	});

	$("#label-warn-cancel-btn").click(function() {
		$("#label-warn").hide();
	});

	$('.my-btn-edit').click(function () {
		var pid = $(this).next().attr('value');
		$.post(GET_PIC_INFO, {"pid": pid}, function (data) {
			$('#edit-title').val(data['name']);
			$('#edit-dsr').val(data['description']);
			$('#edit-pid').val(pid);
		}, "json");
	});

};

function preview(file)
{
	var prevDiv = document.getElementById('preview');
	if (file.files && file.files[0])
	{
		var reader = new FileReader();
		reader.onload = function(evt){
			prevDiv.innerHTML = '<img class="img-rounded" style="width: 300px;padding:2px;" src="' + evt.target.result + '" />';
		}  
		reader.readAsDataURL(file.files[0]);
	}else  
	{
		prevDiv.innerHTML = '<div class="img" style="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale,src=\'' + file.value + '\'"></div>';
	}
}
