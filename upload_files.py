import dropbox, os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            local_path = os.path.join(root, dirs)
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BJN5sXrLOkY2auOrIbytfnozAOpWEpTRiAvqPFyWDR9Ittm0zh1uo7aNcJBEV62-qohXhYMe1gD-S_fiGx9MKV1v5Y-meN3_yLM-cV5fssS5RJRX5eDiR6h23itpNqSRGyLgBzM'

    file_from = input('Enter the current path of the file you want to upload: ')
    file_to = input('Entter the full path you want for the path once it is uploaded: ')  # The full path to upload the file to, including the file name

    transferData = TransferData(access_token)

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()