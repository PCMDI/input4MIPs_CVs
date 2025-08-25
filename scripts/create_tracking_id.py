#!/usr/bin/env python3
"""
Converter for the tracking_id collection.
Converts input4MIPs_tracking_id.json to ESGVOC format.
"""

import json
import os
import logging
from pathlib import Path
from typing import List

from scripts.create_context_file import create_context_file

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def convert() -> None:
    """Convert tracking_id collection to ESGVOC format."""
    # Define collection name
    collection_name = "tracking_id"
    dir_name = f"input4MIPs_{collection_name}"
    
    # Ensure directory exists
    os.makedirs(dir_name, exist_ok=True)
    
    try:
        # Read source file
        source_path = Path("CVs") / f"input4MIPs_{collection_name}.json"
        with open(source_path, "r", encoding="utf-8") as f:
            patterns = json.load(f)
        
        # Create context file with properties
        properties = {
            "pattern": "https://schema.org/pattern"
        }
        create_context_file(collection_name, properties)
        
        # Create term files for each pattern
        for i, pattern in enumerate(patterns):
            term_id = f"pattern_{i+1}"
            
            # Create term file
            term_data = {
                "@context": "000_context.jsonld",
                "id": term_id,
                "type": "tracking_id_pattern",
                "pattern": pattern
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
