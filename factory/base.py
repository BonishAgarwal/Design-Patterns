from abc import ABC, abstractmethod

class Storage:
    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path = file_path
    
    @abstractmethod
    def upload_file(self):
        pass