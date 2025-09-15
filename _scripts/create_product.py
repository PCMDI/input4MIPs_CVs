#!/usr/bin/env python3
"""
Converter for the product collection.
Converts input4MIPs_product.json to ESGVOC format.
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
    """Convert product collection to ESGVOC format."""
    # Define collection name
    collection_name = "product"
    dir_name = f"input4MIPs_{collection_name}"

    # Ensure directory exists
    os.makedirs(dir_name, exist_ok=True)

    try:
        # Read source file
        source_path = Path("CVs") / f"input4MIPs_{collection_name}.json"
        with open(source_path, "r", encoding="utf-8") as f:
            source_data = json.load(f)

        # Create context file with properties
        properties = {"description": "https://schema.org/description"}
        create_context_file(collection_name, "product", properties)

        # Create term files for each product
        for product_id, product_info in source_data.items():
            # Use lowercase for id
            term_id = product_id.lower()

            # Create term file
            term_data = {
                "@context": "000_context.jsonld",
                "id": term_id,
                "type": "product",
                "description": product_info.get("description"),
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
