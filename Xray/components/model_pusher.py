import os
import sys

from Xray.entity.artifact_entity import ModelPusherArtifact
from Xray.entity.config_entity import ModelPusherConfig
from Xray.exception import XRayException
from Xray.logger import logging
from Xray.cloudstorage.s3_ops import S3Operation

class ModelPusher:
    def __init__(self,model_pusher_config: ModelPusherConfig):

        self.model_pusher_config = model_pusher_config
        self.s3 = S3Operation()


    
    def initiate_model_pusher(self):

        """
        Method Name :   initiate_model_pusher

        Description :   This method initiates model pusher. 
        
        Output      :    Model pusher artifact 
        """
        logging.info("Entered initiate_model_pusher method of Modelpusher class")
        try:
            # Uploading the best model to s3 bucket
            self.s3.upload_file(
                "model/model.pt",
                "model.pt",
                "xrayimagesdata25",
                remove=False,
            )
            logging.info("Uploaded best model to s3 bucket")
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")


        except Exception as e:
            XRayException.XRayException(
                error_message=e, error_detail=sys
            )
