from Xray.pipeline.training_pipeline import TrainPipeline
from Xray.exception import XRayException
import sys
if __name__ == "__main__":
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        pass
    except Exception as e:
        raise XRayException(e, sys)