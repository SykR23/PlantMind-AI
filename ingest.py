import argparse

from ingestion.ingest_knowledge_base import IngestionPipeline

parser = argparse.ArgumentParser()

parser.add_argument(
    "knowledge_base",
    help="Knowledge base name",
)

args = parser.parse_args()

pipeline = IngestionPipeline()
pipeline.ingest(args.knowledge_base)