document.addEventListener("DOMContentLoaded", function () {
  const avatarInput = document.getElementById("id_avatar");
  const avatarPreview = document.getElementById("avatarPreview");
  const cropperContainer = document.getElementById("cropperContainer");
  const cropButton = document.getElementById("cropButton");
  const closeModal = document.getElementById("closeModal");
  let cropper = null;

  avatarInput.addEventListener("change", function (event) {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      const reader = new FileReader();
      reader.onload = function (e) {
        avatarPreview.src = e.target.result;
        const avatarImage = document.getElementById("avatarImage");
        avatarImage.src = e.target.result;
        cropperContainer.style.display = "block";
        if (cropper) {
          cropper.destroy();
        }
        cropper = initCropper(e.target.result);
      };
      reader.readAsDataURL(selectedFile);
    }
  });

  closeModal.addEventListener("click", function () {
    closeCropModal();
  });

  cropButton.addEventListener("click", function () {
    const croppedData = cropper.getData();
    saveCroppedImage(croppedData);
    closeCropModal();
  });

  function initCropper(imageData) {
      const image = document.getElementById("avatarImage");
      return new Cropper(image, {
        aspectRatio: 1,
        viewMode: 2,
        zoomable: true,
        movable: true,
        autoCropArea: 100, // Set to 100% to ensure the entire image is included in the cropped area
      });
    }
    

  cropButton.addEventListener("click", function () {
      const croppedData = cropper.getData();
      saveCroppedImage(croppedData);
      closeCropModal();
      // Now the form will be submitted with the cropped image data
    });

  function saveCroppedImage(croppedData) {
      const canvas = cropper.getCroppedCanvas();
      const croppedImageDataURL = canvas.toDataURL("image/jpeg"); // Change to desired format
      document.getElementById("croppedImageData").value = croppedImageDataURL;
    }

  function closeCropModal() {
    cropperContainer.style.display = "none";
    if (cropper) {
      cropper.destroy();
    }
  }
});

cropButton.addEventListener("click", function () {
  const croppedData = cropper.getData();
  const croppedCanvas = cropper.getCroppedCanvas();
  const croppedImageDataURL = croppedCanvas.toDataURL('image/jpeg');  // Change to desired format
  document.getElementById("croppedImageData").value = croppedImageDataURL;
  closeCropModal();
  // Now the form will be submitted with the cropped image data
});

avatarInput.addEventListener("change", function (event) {
  const selectedFile = event.target.files[0];
  if (selectedFile) {
    const reader = new FileReader();
    reader.onload = function (e) {
      const image = new Image();
      image.src = e.target.result;

      image.onload = function () {
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext("2d");
        const maxWidth = 300;
        const maxHeight = 300;

        let newWidth = image.width;
        let newHeight = image.height;

        if (newWidth > maxWidth || newHeight > maxHeight) {
          const ratio = Math.min(maxWidth / newWidth, maxHeight / newHeight);
          newWidth *= ratio;
          newHeight *= ratio;
        }

        canvas.width = newWidth;
        canvas.height = newHeight;
        ctx.drawImage(image, 0, 0, newWidth, newHeight);

        avatarPreview.src = canvas.toDataURL("image/jpeg");

        cropperContainer.style.display = "block";
        if (cropper) {
          cropper.destroy();
        }
        cropper = initCropper(canvas.toDataURL("image/jpeg"));
      };

      reader.readAsDataURL(selectedFile);
    };
    reader.readAsDataURL(selectedFile);
  }
});
