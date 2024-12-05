import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# Your Pinata API credentials
PINATA_API_KEY = "129de7f9074338e9542b"
PINATA_SECRET_API_KEY = "adfd50ac2f8627f2f6ef7cd4ba59d506e16b40441199dda3e9c84ef906630221"
JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiIxNjE3MjdhMC0zMzAyLTQ0M2EtODdhNi1jOWFiN2IwZjU1ZjEiLCJlbWFpbCI6Im4wcm1hbmMwbWljc0Bwcm90b25tYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6Ik5ZQzEifV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiIxMjlkZTdmOTA3NDMzOGU5NTQyYiIsInNjb3BlZEtleVNlY3JldCI6ImFkZmQ1MGFjMmY4NjI3ZjJmNmVmN2NkNGJhNTlkNTA2ZTE2YjQwNDQxMTk5ZGRhM2U5Yzg0ZWY5MDY2MzAyMjEiLCJleHAiOjE3NjQ4ODE4ODF9.H_ve6jaW6xOAS86RueJwPBo6Jnt1OMw_FfHcfqow5lw"

# Image URL you want to upload
image_url = "https://turquoise-mobile-grasshopper-718.mypinata.cloud/files/bafyb"

# Set up the form data
form_data = MultipartEncoder(
    fields={
        'file': (image_url.split('/')[-1], open(image_url, 'rb'), 'image/png')
    }
)

# Pinata API endpoint
pinata_endpoint = "https://api.pinata.cloud/pinning/pinFileToIPFS"

# Make the API request
response = requests.post(
    pinata_endpoint,
    headers={
        'Authorization': f'Bearer {JWT}',
        'pinata_api_key': PINATA_API_KEY,
        'pinata_secret_api_key': PINATA_SECRET_API_KEY,
        'Content-Type': form_data.content_type
    },
    data=form_data
)

# Check the response from Pinata
if response.status_code == 200:
    print("Image uploaded successfully")
    print("IPFS hash:", response.json())
else:
    print("Error uploading the image:", response.status_code)
    print(response.text)