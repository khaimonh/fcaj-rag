from ingestion import loader
from ingestion.chunker_and_summarizer import *

#partition
file_name = 'test.pdf'
file_path = './' + file_name

partitioned = loader(file_path)

chunks_by_title = create_chunks_by_title(partitioned)

summarized = summarise_chunks(chunks_by_title)

