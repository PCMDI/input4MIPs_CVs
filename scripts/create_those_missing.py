#!/usr/bin/env python3
"""
Converter for the mip_era collection.
Converts input4MIPs_mip_era.json to ESGVOC format.
"""

import json
import logging
import os
from pathlib import Path
from typing import List

import esgvoc.api as ea

from scripts.create_context_file import create_context_file

wanted_DDs_collection = {
    "realm": "realm",
    "frequency": "frequency",
    "variable": "variable_id",
    "grid": "grid_label",
    "directory_date": "version",
    "time_range": "time_range",
}

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def convert(dd_name: str, collection_name: str, terms_ids: list) -> None:
    """Convert mip_era collection to ESGVOC format."""
    # Define collection name
    dir_name = f"input4MIPs_{collection_name}"

    # Ensure directory exists
    os.makedirs(dir_name, exist_ok=True)

    try:
        # Create context file
        create_context_file(collection_name, dd_name)

        # Create term files for each MIP era
        for term_id in terms_ids:
            # Use lowercase for id

            # Create term file
            term_data = {
                "@context": "000_context.jsonld",
                "id": term_id,
                "type": dd_name,
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
    for dd, col in wanted_DDs_collection.items():
        # fetch the list of all terms available in universe for this dd:
        terms = ea.get_all_terms_in_data_descriptor(dd, [])
        ids = [term.id for term in terms]

        convert(dd, col, ids)
    # terms = ea.get_all_terms_in_data_descriptor("realm", [])
    # ids = [term.id for term in terms]
    # convert("realm", "realm", ids)
