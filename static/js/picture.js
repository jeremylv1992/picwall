window.onload = function () {
  var photoSubmitBtn = document.getElementById('photo-submit-btn');
  var editSubmitBtn = document.getElementById('edit-submit-btn');

  var photoForm = document.getElementById('photo-form');
  var editForm = document.getElementById('edit-form');

  photoSubmitBtn.onclick = function () {
    photoForm.submit();
  };

  editSubmitBtn.onclick = function () {
    editForm.submit();
  };

  $('.my-btn-edit').click(function () {
    var pid = $(this).next().attr('value');
    $.post("#", {pid: pid}, function (data, status) {
      $('#edit-title').val(data['name']);
      $('#edit-dsr').val(data['description']);
      $('#edit-pid').val(pid);
    });
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