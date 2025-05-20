import os
import sys
import Xray.exception as XRayException

class S3Operation:
    def Sync_folder_to_S3(self , folder:str , bucket_name:str , bucket_folder_name:str)->None:
        try:
            command:str = f"aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}"
            os.system(command)
            
            
        except Exception as e:
            XRayException.XRayException(
                error_message=e, error_detail=sys
            )
            
    def Sync_folder_from_S3(self , folder:str , bucket_name:str , bucket_folder_name:str)->None:
        try:
            command = f"aws s3 sync s3://{bucket_name}/{bucket_folder_name} {folder}"
            os.system(command)
            
            
        except Exception as e:
            XRayException.XRayException(
                error_message=e, error_detail=sys
            )
        
        
        # Changes Done
        #ChangesTest