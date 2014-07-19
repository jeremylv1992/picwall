window.onload = function () {
	var wallSubmitBtn = document.getElementById('wall-submit-btn');
	var editSubmitBtn = document.getElementById('edit-submit-btn');
	var permissionSubmitBtn = document.getElementById('change-permission-btn');

	var wallForm = document.getElementById('wall-form');
	var editForm = document.getElementById('edit-form'); 
	var permissionForm = document.getElementById('change-permission-form');

	$("#wall-submit-btn").click(function () {
		$("#wall-form").submit();
	});

	$("#edit-submit-btn").click(function () {
		$("#edit-form").submit();
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
				if (isManager) {
					$(id).attr('checked', true);
				} else {
					$(id).attr('checked', false);
				}
			}
		}, "json");
	});
};
