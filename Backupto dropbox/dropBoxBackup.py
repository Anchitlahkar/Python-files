import dropbox

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken
        
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.accessToken)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    AccessToken = 'yGNCqYxnD6QAAAAAAAAAAQxm9ZwFySM4SnlKYaE4_qW4v2TCtO3OibEsfmEZdWjR'
    transferData= TransferData(AccessToken)

    file_from = input("Please enter the file location\n")
    file_to = input("\nPlease enter dropbox file location\n")


    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()