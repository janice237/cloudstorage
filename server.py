import os
import grpc
from concurrent import futures
import cloud_storage_pb2
import cloud_storage_pb2_grpc
import logging

class CloudStorageServicer(cloud_storage_pb2_grpc.CloudStorageServiceServicer):
    def __init__(self, virtual_disk_path):
        self.virtual_disk_path = virtual_disk_path
        
        # Create virtual disk directory if it doesn't exist
        if not os.path.exists(virtual_disk_path):
            os.makedirs(virtual_disk_path)
        
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def UploadFile(self, request, context):
        try:
            # Construct full file path
            file_path = os.path.join(self.virtual_disk_path, request.filename)
            
            # Check if file already exists
            if os.path.exists(file_path):
                self.logger.warning(f"File {request.filename} already exists. Overwriting.")
                context.set_details("File already exists. Overwriting.")
            
            # Write file to virtual disk
            with open(file_path, 'wb') as f:
                f.write(request.file_content)
            
            self.logger.info(f"File {request.filename} uploaded successfully")
            return cloud_storage_pb2.UploadResponse(
                success=True, 
                message=f"Please enter filename to upload at the prompt."
            )
        except Exception as e:
            self.logger.error(f"Error uploading file: {e}")
            return cloud_storage_pb2.UploadResponse(
                success=False, 
                message=f"Error uploading file. Please try again."
            )

    def DownloadFile(self, request, context):
        try:
            # Construct full file path
            file_path = os.path.join(self.virtual_disk_path, request.filename)
            
            # Check if file exists
            if not os.path.exists(file_path):
                self.logger.warning(f"File {request.filename} not found")
                return cloud_storage_pb2.DownloadResponse(
                    success=False, 
                    message=f"File not found. Please check the filename."
                )
            
            # Read file content
            with open(file_path, 'rb') as f:
                file_content = f.read()
            
            self.logger.info(f"File {request.filename} downloaded successfully")
            return cloud_storage_pb2.DownloadResponse(
                success=True, 
                file_content=file_content,
                message=f"Please enter local path to save the file."
            )
        except Exception as e:
            self.logger.error(f"Error downloading file: {e}")
            return cloud_storage_pb2.DownloadResponse(
                success=False, 
                message=f"Error downloading file. Please try again."
            )

    def DeleteFile(self, request, context):
        try:
            # Construct full file path
            file_path = os.path.join(self.virtual_disk_path, request.filename)
            
            # Check if file exists
            if not os.path.exists(file_path):
                self.logger.warning(f"File {request.filename} not found")
                return cloud_storage_pb2.DeleteResponse(
                    success=False, 
                    message=f"File not found. Please check the filename."
                )
            
            # Delete file
            os.remove(file_path)
            
            self.logger.info(f"File {request.filename} deleted successfully")
            return cloud_storage_pb2.DeleteResponse(
                success=True, 
                message=f"File {request.filename} deleted successfully."
            )
        except Exception as e:
            self.logger.error(f"Error deleting file: {e}")
            return cloud_storage_pb2.DeleteResponse(
                success=False, 
                message=f"Error deleting file. Please try again."
            )

    def ListFiles(self, request, context):
        try:
            # Get list of files in virtual disk
            files = os.listdir(self.virtual_disk_path)
            
            # Prepare a formatted message with files
            if files:
                file_list = "\n".join(files)
                self.logger.info("Files listed successfully")
                context.set_details(f"Available files:\n{file_list}")
            else:
                self.logger.info("No files in virtual disk")
                context.set_details("No files available in the virtual disk.")
            
            return cloud_storage_pb2.ListFilesResponse(files=files)
        except Exception as e:
            self.logger.error(f"Error listing files: {e}")
            context.set_details("Error listing files.")
            return cloud_storage_pb2.ListFilesResponse(files=[])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    virtual_disk_path = './virtual_disk'
    
    cloud_storage_pb2_grpc.add_CloudStorageServiceServicer_to_server(
        CloudStorageServicer(virtual_disk_path), server
    )
    
    server.add_insecure_port('[::]:50051')
    server.start()
    
    print("Cloud Storage Server started. Listening on port 50051...")
    
    server.wait_for_termination()

if __name__ == '__main__':
    serve()