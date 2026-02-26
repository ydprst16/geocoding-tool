from dotenv import load_dotenv
load_dotenv()
from utils.logger import setup_logger
from pipeline.processor import run_geocode_pipeline

load_dotenv()
logger = setup_logger()

def main():
    logger.info("Start geocode process")
    run_geocode_pipeline(logger)

if __name__ == "__main__":
    main()