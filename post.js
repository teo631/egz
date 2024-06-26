document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('coolButton').addEventListener('click', (event) => {
      event.preventDefault(); // Prevent the default form submission behavior
      
      const formData = new FormData();
      const imageFile = document.getElementById('upload').files[0];
      formData.append('image', imageFile);
  
      const boolValue1 = document.getElementById("k_v").value;
      const boolValue2 = document.getElementById("bb_v").value;
      const boolValue3 = document.getElementById("eklem_v").value;
      const boolValue4 = document.getElementById("alerji_v").value;
      const boolValue5 = document.getElementById("kabuk_v").value;
      const boolValue6 = document.getElementById("sis_v").value;
      formData.append('boolValue1', boolValue1);
      formData.append('boolValue2', boolValue2);
      formData.append('boolValue3', boolValue3);
      formData.append('boolValue4', boolValue4);
      formData.append('boolValue5', boolValue5);
      formData.append('boolValue6', boolValue6);

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
            console.log('Server response:', data.status);
            console.log('Server response:', data.risk);
            console.log('Server response:', data.seviye);

            document.getElementById("sonuc").innerHTML = data.status;
            document.getElementById("oneri").innerHTML = data.risk
            document.getElementById("resultBoxBox").style.display="block";

            if(data.seviye=="1"){
              document.getElementById("resultBox").style.backgroundColor="white"
            }else if(data.seviye=="2"){
              document.getElementById("resultBox").style.backgroundColor="yellow"
            }else if(data.seviye=="3"){
              document.getElementById("resultBox").style.backgroundColor="red"
            }
          })
        .catch(error => {
          console.error('There was a problem sending the image and data:', error);
        });
    });
  });
// Send the FormData object to the server using fetch
