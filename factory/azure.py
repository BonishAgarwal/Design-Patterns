from base import Storage


class Azure(Storage):
    
    def __init__(self, file_name, file_path):
        super().__init__(file_name, file_path)
    
    def upload_file(self):
        print("Uploading file to Azure Blob...")
    