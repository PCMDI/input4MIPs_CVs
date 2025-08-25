#!/usr/bin/env python3
"""
Script to check if terms in the input4MIPs CV already exist in the WCRP Universe.
This helps ensure compatibility and identify terms that need to be added to the Universe.
"""

import json
import os
import logging
from pathlib import Path
from typing import Dict, List, Any, Set, Optional

import esgvoc.api as ev

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_cv_terms(collection_name: str) -> List[str]:
    """
    Load terms from a CV file.
    
    Args:
        collection_name: Name of the collection
        
    Returns:
        List of term IDs
    """
    cv_path = Path("CVs") / f"input4MIPs_{collection_name}.json"
    
    if not cv_path.exists():
        logger.warning(f"CV file not found: {cv_path}")
        return []
    
    with open(cv_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Extract terms based on file structure
    terms = []
    if isinstance(data, list):
        # Simple list format
        terms = data
    elif isinstance(data, dict):
        if collection_name == "target_mip":
            # Special handling for nested target_mip structure
            for mip_era in data.values():
                terms.extend(mip_era.keys())
        else:
            # Dictionary with key-value pairs
            terms = list(data.keys())
    
    return terms


def check_collection_compatibility(collection_name: str, terms: List[str]) -> Dict[str, List]:
    """
    Check if terms in a collection exist in the Universe.
    
    Args:
        collection_name: Name of the collection (e.g., 'target_mip')
        terms: List of term IDs to check
        
    Returns:
        Dictionary with found and missing terms
    """
    found_terms = []
    missing_terms = []
    
    # Try to get terms from the Universe
    universe_terms = []
    try:
        # Use appropriate data descriptor name based on collection_name
        data_descriptor = collection_name
        if collection_name == "target_mip":
            data_descriptor = "mip"
        elif collection_name == "source_id":
            data_descriptor = "source"
        
        universe_terms = ev.get_all_terms_in_data_descriptor(data_descriptor)
        logger.info(f"Found {len(universe_terms)} {data_descriptor} terms in Universe")
    except Exception as e:
        logger.warning(f"Could not retrieve {collection_name} terms from Universe: {str(e)}")
        missing_terms = terms
        return {"found": found_terms, "missing": missing_terms}
    
    # Check each term against universe terms
    for term in terms:
        found = False
        for universe_term in universe_terms:
            # Try to match by ID or DRS name (case-insensitive)
            if (universe_term.id.lower() == term.lower() or
                    (hasattr(universe_term, 'drs_name') and 
                     universe_term.drs_name.lower() == term.lower())):
                found = True
                found_terms.append({
                    "id": term,
                    "universe_id": universe_term.id,
                    "type": universe_term.type
                })
                break
        
        if not found:
            missing_terms.append(term)
    
    return {
        "found": found_terms,
        "missing": missing_terms
    }


def main() -> None:
    """Main function to check all collections for Universe compatibility."""
    # Define collections to check
    collections_to_check = [
        "activity_id",
        "target_mip",
        "dataset_category",
        "institution_id",
        "mip_era"
    ]
    
    results = {}
    
    for collection_name in collections_to_check:
        try:
            logger.info(f"Checking {collection_name} compatibility...")
            
            # Load terms from CV file
            terms = load_cv_terms(collection_name)
            if not terms:
                logger.warning(f"No terms found for {collection_name}")
                continue
            
            # Check compatibility
            compatibility = check_collection_compatibility(collection_name, terms)
            results[collection_name] = compatibility
            
            # Log results
            logger.info(f"{collection_name} compatibility:")
            logger.info(f"  Found in Universe: {len(compatibility['found'])}")
            logger.info(f"  Missing from Universe: {len(compatibility['missing'])}")
            
            # Output missing terms to a file
            if compatibility["missing"]:
                missing_file = f"missing_{collection_name}_terms.json"
                with open(missing_file, "w", encoding="utf-8") as f:
                    json.dump(compatibility["missing"], f, indent=4)
                logger.info(f"  Missing terms written to {missing_file}")
            
        except Exception as e:
            logger.error(f"Error checking {collection_name}: {str(e)}")
    
    # Output overall summary
    logger.info("\nOverall Compatibility Summary:")
    for collection_name, compatibility in results.items():
        found_count = len(compatibility["found"])
        missing_count = len(compatibility["missing"])
        total_count = found_count + missing_count
        percentage = (found_count / total_count * 100) if total_count > 0 else 0
        
        logger.info(f"{collection_name}: {found_count}/{total_count} terms found ({percentage:.1f}%)")


if __name__ == "__main__":
    main()
