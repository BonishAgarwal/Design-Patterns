from aws import AWS
from azure import Azure

class StorageFactory:
    
    def store(self, cloud_provider, file_path, file_name):
        if cloud_provider == "AWS":
            return AWS(file_name, file_path)
        elif cloud_provider == "Azure":
            return Azure(file_name, file_path)
        else:
            return