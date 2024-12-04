from storage_factory import StorageFactory


def main():
    # Using factory design pattern, we have hide the creation of AWS and Azure Objects
    factory = StorageFactory()
    object = factory.store("AWS", "abc.txt", "./uploads")
    object1 = factory.store("Azure", "abc.txt", "./uploads")
    
    object.upload_file()
    object1.upload_file()

if __name__ == "__main__":
    main()