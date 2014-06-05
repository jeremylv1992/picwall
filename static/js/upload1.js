window.onload = function () {
  var submitPhotoBtn = document.getElementById('submitPhotoBtn');
  var submitWallBtn = document.getElementById('submitWallBtn');

  var photoForm = document.getElementById('photoForm');
  var wallForm = document.getElementById('wallForm');

  submitPhotoBtn.onclick = function () {
    photoForm.submit();
  };
  submitWallBtn.onclick = function () {
  	wallForm.submit();
  };
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