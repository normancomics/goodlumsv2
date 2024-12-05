const axios = require('axios');
const fs = require('fs');
const FormData = require('form-data');
const { PinataClient } = require('@pinata/sdk');

// Pinata credentials
const apiKey = '129de7f9074338e9542b';  // Replace with your Pinata API key
const apiSecret = 'adfd50ac2f8627f2f6ef7cd4ba59d506e16b40441199dda3e9c84ef906630221';  // Replace with your Pinata API secret
const jwtToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...';  // Replace with your JWT token

// Create Pinata instance
const pinata = PinataClient({
  apiKey,
  apiSecret,
  jwtToken
});

// Image URL you want to download
const imageUrl = 'https://turquoise-mobile-grasshopper-718.mypinata.cloud/files/bafybeifivwurxjsdebqqzrvwaxvh4wvzsiaooeufhe5iak2ufqwfdx4ol4';

// Download the image
axios.get(imageUrl, { responseType: 'stream' })
  .then((response) => {
    const writer = fs.createWriteStream('temp_image.jpg'); // Save image to a local file

    // Pipe the response stream into the file
    response.data.pipe(writer);

    writer.on('finish', () => {
      console.log('Image downloaded successfully.');

      // Now upload the image to Pinata
      const form = new FormData();
      form.append('file', fs.createReadStream('temp_image.jpg')); // Pass the local file

      pinata.pinFileToIPFS(form, { pinataMetadata: { name: 'My Image' } })
        .then((result) => {
          console.log('Uploaded successfully:', result);
          fs.unlinkSync('temp_image.jpg'); // Clean up the temp file
        })
        .catch((err) => {
          console.log('Error uploading the image:', err);
        });
    });

    writer.on('error', (err) => {
      console.error('Error downloading the image:', err);
    });
  })
  .catch((err) => {
    console.error('Error fetching the image URL:', err);
  });