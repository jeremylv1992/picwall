window.onload = function () {
  var wallSubmitBtn = document.getElementById('wall-submit-btn');
  var editSubmitBtn = document.getElementById('edit-submit-btn');

  var wallForm = document.getElementById('wall-form');
  var editForm = document.getElementById('edit-form'); 

  wallSubmitBtn.onclick = function () {
    wallForm.submit();
  };

  editSubmitBtn.onclick = function () {
    editForm.submit();
  };

  $('.my-btn-edit').click(function () {
    var wid = $(this).next().attr('value');
    $.post("#", {wid: wid}, function (data, status) {
      $('#edit-title').val(data['name']);
      $('#edit-dsr').val(data['description']);
      $('#edit-wid').val(wid);
    });
  });
};