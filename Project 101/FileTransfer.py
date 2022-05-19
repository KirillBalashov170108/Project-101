import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
    
def main():
    access_token='sl.BH1URkWAD9EGp6bM9JQMTalQ881_V9bDiPpgyMPw7bxDPBLUwF7zJdq6QOA5rinrrTnbh1O-AwD-bRPEM0pf4EaA1gT6cyB3tbl_WTka8GfPsOHlZxwc_jamQF9n8rUAsu2X5kpBTL5I'

    t1=TransferData(access_token)
    file_to=input("Enter the full path to upload to Dropbox")
    file_from=input("Enter the full path to transfer from")

    t1.upload_file(file_from,file_to)
    print("File has been moved successfully")
    
main()