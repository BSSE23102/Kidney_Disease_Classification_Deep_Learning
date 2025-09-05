import sys, os
sys.path.append(os.path.abspath("src"))

from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline




try:    
    logger.info(">>>>> stage 1 started <<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(">>>>> stage 1 completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Stage 2: Prepare Base Model"
try:    
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e