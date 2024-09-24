# backup_tool_onedrive.py


import requests
import os
import msal

CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
TENANT_ID = 'your_tenant_id'
AUTHORITY_URL = f"https://login.microsoftonline.com/{TENANT_ID}"
REDIRECT_URI = 'http://localhost'
SCOPES = ['Files.ReadWrite.All']

def authenticate():
    """Authenticate with Microsoft and obtain an access token."""
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY_URL,
        client_credential=CLIENT_SECRET
    )
    
    token_response = app.acquire_token_for_client(scopes=SCOPES)
    
    if 'access_token' in token_response:
        return token_response['access_token']
    else:
        raise Exception("Authentication failed.")

def upload_to_onedrive(file_path, access_token):
    """Uploads a file to OneDrive using Microsoft Graph API."""
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/octet-stream'
    }
    
    file_name = os.path.basename(file_path)
    upload_url = f"https://graph.microsoft.com/v1.0/me/drive/root:/{file_name}:/content"
    
    with open(file_path, 'rb') as file:
        response = requests.put(upload_url, headers=headers, data=file)
    
    if response.status_code == 201:
        print(f"Uploaded {file_path} to OneDrive.")
    else:
        print(f"Failed to upload {file_path}. Response: {response.content}")

def main(directory):
    """Main function to perform backup to OneDrive."""
    # Authenticate and get access token
    access_token = authenticate()

    # Select files
    files_to_backup = [os.path.join(root, file) for root, _, files in os.walk(directory) for file in files]
    
    # Upload files to OneDrive
    for file in files_to_backup:
        upload_to_onedrive(file, access_token)

if __name__ == "__main__":
    directory = input("Enter the directory to back up: ")
    main(directory)
