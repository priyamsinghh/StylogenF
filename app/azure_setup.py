from azure.storage.blob import BlobServiceClient
from decouple import config
import os
import uuid


def upload_to_blob_storage():

    connection_string = config('AZURE_CONNECTION_STRING')
    container_name = config('AZURE_STORAGE_CONTAINER_NAME')

    blob_service_client = BlobServiceClient.from_connection_string(
        connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    blob_name = str(uuid.uuid4())  # Generates a new UUID
    blob_client = container_client.get_blob_client(blob_name)
    file_path = "test1.png"

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
    blob_uri = blob_client.url

    return blob_uri
# from azure.storage.blob import BlobServiceClient
# from decouple import config
# import os
# import uuid

# def upload_to_blob_storage(file_path):
#     try:
#         # Retrieving Azure connection string and container name from environment variables
#         connection_string = config('AZURE_CONNECTION_STRING')
#         container_name = config('AZURE_STORAGE_CONTAINER_NAME')

#         # Creating BlobServiceClient
#         blob_service_client = BlobServiceClient.from_connection_string(connection_string)

#         # Getting ContainerClient
#         container_client = blob_service_client.get_container_client(container_name)

#         # Generating a random UUID for blob name
#         blob_name = str(uuid.uuid4())
        
#         # Getting BlobClient for the generated blob name
#         blob_client = container_client.get_blob_client(blob_name)

#         # Uploading the file
#         with open(file_path, "rb") as data:
#             blob_client.upload_blob(data)

#         # Retrieving the URL of the uploaded blob
#         blob_uri = blob_client.url

#         return blob_uri
#     except Exception as e:
#         # Handling any exceptions that might occur
#         print(f"An error occurred: {e}")
#         return None

        
