import sys, os
sys.path.append(os.path.abspath("src"))

from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline


try:    
    logger.info(">>>>> stage 1 started <<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(">>>>> stage 1 completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e