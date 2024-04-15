document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('coolButton').addEventListener('click', (event) => {
      event.preventDefault(); // Prevent the default form submission behavior
      
      const formData = new FormData();
      const imageFile = document.getElementById('upload').files[0];
      formData.append('image', imageFile);
  
      const boolValue1 = true;
      const boolValue2 = false;
      formData.append('boolValue1', boolValue1);
      formData.append('boolValue2', boolValue2);
  
      fetch('http://127.0.0.1:5000/upload_image', {
        method: 'POST',
        body: formData,
      })
        .then(response => {
          console.log('Image and data sent to server.');
          console.log(response);
          return response.json();
        })
        .then(data => {
            console.log('Server response:', data);
          })
        .catch(error => {
          console.error('There was a problem sending the image and data:', error);
        });
    });
  });
// Send the FormData object to the server using fetch
