function previewAvatar(event) {
    const input = event.target;
    const img = document.getElementById('avatarPreview');
  
    if (input.files && input.files[0]) {
      const reader = new FileReader();
  
      reader.onload = function() {
        img.src = reader.result;
      };
  
      reader.readAsDataURL(input.files[0]);
    }
  }