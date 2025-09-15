#!/usr/bin/env python3
"""
Converter for the activity_id collection.
Converts input4MIPs_activity_id.json to ESGVOC format.
"""

import json
import logging
import os
from pathlib import Path
from typing import Any, Dict

from scripts.create_context_file import create_context_file

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def convert() -> None:
    """Convert activity_id collection to ESGVOC format."""
    # Define collection name
    collection_name = "activity_id"
    dir_name = f"input4MIPs_{collection_name}"

    # Ensure directory exists
    os.makedirs(dir_name, exist_ok=True)

    try:
        # Read source file
        source_path = Path("CVs") / f"input4MIPs_{collection_name}.json"
        with open(source_path, "r", encoding="utf-8") as f:
            source_data = json.load(f)

        # Create context file with properties
        properties = {
            "URL": "https://schema.org/url",
            "long_name": "https://schema.org/name",
        }
        create_context_file(collection_name, "activity", properties)

        # Create term files
        for activity_id, activity_info in source_data.items():
            # Use lowercase for id
            term_id = activity_id.lower()

            # Create term file
            term_data = {
                "@context": "000_context.jsonld",
                "id": term_id,
                "type": "activity",
                "URL": activity_info.get("URL"),
                "long_name": activity_info.get("long_name"),
            }

            # Write term file
            term_path = Path(dir_name) / f"{term_id}.json"
            with open(term_path, "w", encoding="utf-8") as f:
                json.dump(term_data, f, indent=4)

            logger.info(f"Created term file: {term_path}")

        logger.info(f"Successfully converted {collection_name} collection")

    except Exception as e:
        logger.error(f"Error converting {collection_name}: {str(e)}")
        raise


if __name__ == "__main__":
    convert()
