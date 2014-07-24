window.onload = function () {
	$("#create-warn").hide();
	$("#wall-submit-btn").click(function () {
		var title = $("#wall-title").val();
		if (title != "") {
			$("#wall-form").submit();
		} else {
			$('#create-warn').show();
		}
	});

	$('#edit-warn').hide();
	$('#create-warn-cancel-btn').click(function() {
		$('#create-warn').hide();
	});

	$("#edit-submit-btn").click(function () {
		var title = $("#edit-title").val();
		if (title != "") {
			$("#edit-form").submit();
		} else {
			$('#edit-warn').show();
		}
	});
	$('#edit-warn-cancel-btn').click(function() {
		$('#edit-warn').hide();
	});

	$("#change-permission-btn").click(function() {
		$("#change-permission-form").submit();
	});

	$('.my-btn-edit').click(function () {
		var wid = $(this).next().attr('value');
		$.post(GET_PW_INFO, {wid: wid}, function (data, status) {
			$('#edit-title').val(data['name']);
			$('#edit-dsr').val(data['description']);
			$('#edit-wid').val(wid);
		}, "json");
	});

	$('.my-btn-permission').click(function () {
		var wid = $(this).next().attr('value');
		$.post(GET_PW_PERMISSION, {wid: wid}, function (data, status) {
			accessPermission = "#my-"+data['access_permission'];
			$(accessPermission).attr('checked', true);
			$('#permission-wid').val(wid);

			for (i = 0; i < data['managers'].length; i++) {
				var id = "#friend" + data['managers'][i]['id'];
				var isManager = data['managers'][i]['isManager'];
				console.log(id);
				if (isManager) {
					alert('hehe');
					$(id).attr('checked', true);
				} else {
					$(id).attr('checked', false);
				}
			}
		}, "json");
	});
};
