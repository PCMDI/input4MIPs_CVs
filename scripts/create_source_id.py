#!/usr/bin/env python3
"""
Converter for the source_id collection.
Converts input4MIPs_source_id.json to ESGVOC format.
"""

import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, List

from scripts.create_context_file import create_context_file
from scripts.fetch_cv_files import fetch_cv_file, get_cv_path

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def convert() -> None:
    """Convert source_id collection to ESGVOC format."""
    # Define collection name
    collection_name = "source_id"
    dir_name = f"input4MIPs_{collection_name}"

    # Ensure directory exists
    os.makedirs(dir_name, exist_ok=True)

    try:
        # Ensure the CV file is available locally
        filename = f"input4MIPs_{collection_name}.json"
        source_path = get_cv_path(collection_name)
        if not source_path or not source_path.exists():
            logger.info(f"Fetching {filename} from GitHub...")
            source_path = fetch_cv_file(filename)

        # Read source file
        with open(source_path, "r", encoding="utf-8") as f:
            source_data = json.load(f)

        # Extract all properties from the first entry to create context
        sample_entry = next(iter(source_data.values()))
        properties = {}

        # Map each property to an appropriate URI
        property_mappings = {
            "activity_id": "https://espri-mod.github.io/mip-cmor-tables/activity",
            "institution_id": "https://espri-mod.github.io/mip-cmor-tables/institution",
            "contact": "https://schema.org/email",
            "license_id": "https://schema.org/license",
            "mip_era": "https://espri-mod.github.io/mip-cmor-tables/mip_era",
            "source_version": "https://schema.org/version",
            "further_info_url": "https://schema.org/url",
            "dataset_category": "https://espri-mod.github.io/mip-cmor-tables/dataset_category",
            "target_mip": "https://espri-mod.github.io/mip-cmor-tables/target_mip",
            "authors": "https://schema.org/author",
        }

        # Add all properties found in the sample entry
        for key in sample_entry.keys():
            if key in property_mappings:
                properties[key] = property_mappings[key]
            else:
                # Default to schema.org namespace for unknown properties
                properties[key] = f"https://schema.org/{key}"

        # Create context file
        create_context_file(collection_name, "source", properties)

        # Create term files for each source ID
        for source_id, details in source_data.items():
            # Use lowercase for id
            term_id = source_id.lower()

            # Create term file
            term_data = {
                "@context": "000_context.jsonld",
                "id": term_id,
                "type": "source",  # here we have to tell the type from Universe DD to get the pydantic in esgvoc
            }

            # Add all properties
            for key, value in details.items():
                term_data[key] = value

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
