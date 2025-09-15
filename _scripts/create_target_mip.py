#!/usr/bin/env python3
"""
Converter for the target_mip collection.
Converts input4MIPs_target_mip.json to ESGVOC format.
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
    """Convert target_mip collection to ESGVOC format."""
    # Define collection name
    collection_name = "target_mip"
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
            "full_name": "https://schema.org/name",
            "mip_era": "https://espri-mod.github.io/mip-cmor-tables/mip_era",
        }
        create_context_file(collection_name, "activity", properties)

        # Process each MIP era and its MIPs
        for mip_era, mips in source_data.items():
            for mip_id, mip_info in mips.items():
                # Use lowercase for id
                term_id = mip_id.lower()

                # Create term file
                term_data = {
                    "@context": "000_context.jsonld",
                    "id": term_id,
                    "type": "activity",
                    "mip_era": mip_era.lower(),
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
