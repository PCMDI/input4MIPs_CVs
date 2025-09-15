#!/usr/bin/env python3
"""
Master script for converting input4MIPs Controlled Vocabulary (CV) to ESGVOC format.
This script coordinates the conversion of all collections.
"""

import os
import logging
import importlib
import json
from pathlib import Path
from typing import Dict, List, Optional

# Import CV fetcher
from scripts.fetch_cv_files import fetch_all_cv_files

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define collections to convert
COLLECTIONS = [
    "activity_id",
    "target_mip",
    "source_id",
    "dataset_category",
    "license",
    "mip_era",
    "product",
    "publication_status",
    "tracking_id",
    "required_global_attributes",
    "institution_id"
]

# Source and destination paths
CV_SOURCE_DIR = Path("CVs")
OUTPUT_BASE_DIR = Path(".")


def create_collection_directory(collection_name: str) -> Path:
    """
    Create directory for collection if it doesn't exist.
    
    Args:
        collection_name: Name of the collection
        
    Returns:
        Path: Path to the created directory
    """
    dir_name = f"input4MIPs_{collection_name}"
    dir_path = OUTPUT_BASE_DIR / dir_name
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def convert_collection(collection_name: str) -> bool:
    """
    Convert a specific collection.
    
    Args:
        collection_name: Name of the collection to convert
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    logger.info(f"Converting collection: {collection_name}")
    
    try:
        # Try to import the converter module
        try:
            # Dynamic import of converter module
            module_name = f"create_{collection_name}"
            module_path = f"scripts.{module_name}"
            converter = importlib.import_module(module_path)
        except ImportError:
            logger.error(f"Could not import converter module for {collection_name}")
            return False
        
        # Call the conversion function
        converter.convert()
        logger.info(f"Successfully converted {collection_name}")
        return True
    except Exception as e:
        logger.error(f"Error converting {collection_name}: {str(e)}")
        return False


def main():
    """Main function to convert all collections."""
    logger.info("Starting CV collection conversion")
    
    # Step 1: Fetch all CV files from GitHub
    logger.info("Fetching CV files from GitHub...")
    cv_files = fetch_all_cv_files()
    if not cv_files:
        logger.error("Failed to fetch any CV files. Cannot proceed with conversion.")
        return
    
    # Step 2: Convert all collections
    results = {}
    for collection in COLLECTIONS:
        success = convert_collection(collection)
        results[collection] = "Success" if success else "Failed"
    
    # Output summary
    logger.info("\nConversion Summary:")
    for collection, status in results.items():
        logger.info(f"{collection}: {status}")


if __name__ == "__main__":
    main()
