import sys
import grpc
import cloud_storage_pb2
import cloud_storage_pb2_grpc
import os

def upload_file(stub):
    filename = input("Enter filename to upload: ")
    local_path = input("Enter full local path of the file: ")
    
    try:
        with open(local_path, 'rb') as f:
            file_content = f.read()
        
        response = stub.UploadFile(
            cloud_storage_pb2.UploadRequest(
                filename=filename, 
                file_content=file_content
            )
        )
        # No print statements, server will handle messaging
    except Exception as e:
        # Let server handle error messaging
        pass

def download_file(stub):
    # Request file list from server
    response = stub.ListFiles(cloud_storage_pb2.ListFilesRequest())
    
    filename = input("Enter filename to download: ")
    local_path = input("Enter full local path to save the file: ")
    
    try:
        download_response = stub.DownloadFile(
            cloud_storage_pb2.DownloadRequest(filename=filename)
        )
        
        if download_response.success:
            with open(local_path, 'wb') as f:
                f.write(download_response.file_content)
        # No print statements, server will handle messaging
    except Exception as e:
        # Let server handle error messaging
        pass

def delete_file(stub):
    # Request file list from server
    stub.ListFiles(cloud_storage_pb2.ListFilesRequest())
    
    filename = input("Enter filename to delete: ")
    
    try:
        stub.DeleteFile(
            cloud_storage_pb2.DeleteRequest(filename=filename)
        )
        # No print statements, server will handle messaging
    except Exception as e:
        # Let server handle error messaging
        pass

def main():
    # Check if correct number of arguments is provided
    if len(sys.argv) != 2:
        sys.exit(1)
    
    # Parse service selection argument
    try:
        service = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    
    # Create gRPC channel
    channel = grpc.insecure_channel('localhost:50051')
    stub = cloud_storage_pb2_grpc.CloudStorageServiceStub(channel)
    
    # Select service based on argument
    if service == 1:
        upload_file(stub)
    elif service == 2:
        download_file(stub)
    elif service == 3:
        delete_file(stub)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()