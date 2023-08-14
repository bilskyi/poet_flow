document.addEventListener("DOMContentLoaded", function () {
  const avatarInput = document.getElementById("id_avatar");
  const avatarPreview = document.getElementById("avatarPreview");
  const cropperContainer = document.getElementById("cropperContainer");
  const cropButton = document.getElementById("cropButton");
  let cropper = null;
  let croppedData = null;

  avatarInput.addEventListener("change", function (event) {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      const reader = new FileReader();
      reader.onload = function (e) {
        avatarPreview.src = e.target.result;
        cropperContainer.style.display = "block";
        if (cropper) {
          cropper.destroy();
        }
        cropper = initCropper(e.target.result);
      };
      reader.readAsDataURL(selectedFile);
    }
  });

  cropButton.addEventListener("click", function () {
    croppedData = cropper.getData();
    cropper.getCroppedCanvas().toBlob(function (blob) {
      croppedData.cropped_image = blob;
      saveCroppedImage(croppedData);
      closeCropModal();
    }, "image/jpeg"); // Change the format if needed
  });

  function initCropper(imageData) {
    const image = document.getElementById("avatarImage");
    return new Cropper(image, {
      aspectRatio: 1,
      viewMode: 2,
      zoomable: true,
      movable: true,
      autoCropArea: 1, // Set to 1 to ensure the entire image is included in the cropped area
    });
  }

  function closeCropModal() {
    cropperContainer.style.display = "none";
    if (cropper) {
      cropper.destroy();
    }
  }
});
