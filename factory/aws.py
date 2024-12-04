from base import Storage

class AWS(Storage):
    
    def __init__(self, file_name, file_path):
        super().__init__(file_name, file_path)
    
    def upload_file(self):
        print("Uploading file to AWS S3...")
