from ingestion.test_ingestion import test_full_pipeline_with_real_pdf
from dotenv import load_dotenv

load_dotenv()

test_full_pipeline_with_real_pdf("NASDAQ_AAPL_2025.pdf", True)