#!/usr/bin/env python3
"""
Utility to fetch input4MIPs CV files from GitHub.
"""

import json
import os
import logging
import requests
from pathlib import Path
from typing import Dict, Any, List, Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# GitHub repository information
GITHUB_BASE_URL = 'https://raw.githubusercontent.com/PCMDI/input4MIPs_CVs'
GITHUB_BRANCH = 'main'
GITHUB_CV_PATH = 'CVs'

# List of CV files to fetch
CV_FILES = [
    'input4MIPs_activity_id.json',
    'input4MIPs_target_mip.json',
    'input4MIPs_source_id.json',
    'input4MIPs_dataset_category.json',
    'input4MIPs_license.json',
    'input4MIPs_mip_era.json',
    'input4MIPs_product.json',
    'input4MIPs_publication_status.json',
    'input4MIPs_tracking_id.json',
    'input4MIPs_required_global_attributes.json',
    'input4MIPs_institution_id.json',
    'input4MIPs_DRS.json'
]

# Local directory to store fetched files
LOCAL_CV_DIR = Path("CVs")


def fetch_json(url: str) -> Any:
    """
    Fetch and parse JSON data from a URL.
    
    Args:
        url: URL to fetch JSON from
        
    Returns:
        Parsed JSON data
        
    Raises:
        Exception: If there's an issue fetching or parsing the data
    """
    try:
        logger.debug(f"Fetching JSON from {url}")
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Failed to fetch data from {url}: {str(e)}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON from {url}: {str(e)}")
        raise


def fetch_cv_file(filename: str, branch: str = GITHUB_BRANCH) -> Path:
    """
    Fetch a CV file from GitHub and save it locally.
    
    Args:
        filename: Name of the CV file to fetch
        branch: GitHub branch to fetch from
        
    Returns:
        Path to the locally saved file
        
    Raises:
        Exception: If there's an issue fetching or saving the file
    """
    # Create local directory if it doesn't exist
    os.makedirs(LOCAL_CV_DIR, exist_ok=True)
    
    # Construct GitHub URL
    github_url = f"{GITHUB_BASE_URL}/{branch}/{GITHUB_CV_PATH}/{filename}"
    
    # Local file path
    local_file_path = LOCAL_CV_DIR / filename
    
    try:
        # Fetch the JSON data
        logger.info(f"Fetching {filename} from GitHub...")
        data = fetch_json(github_url)
        
        # Save to local file
        with open(local_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        
        logger.info(f"Saved {filename} to {local_file_path}")
        return local_file_path
    
    except Exception as e:
        logger.error(f"Failed to fetch and save {filename}: {str(e)}")
        raise


def fetch_all_cv_files(branch: str = GITHUB_BRANCH) -> Dict[str, Path]:
    """
    Fetch all CV files from GitHub and save them locally.
    
    Args:
        branch: GitHub branch to fetch from
        
    Returns:
        Dictionary mapping filenames to local file paths
    """
    results = {}
    
    for filename in CV_FILES:
        try:
            local_path = fetch_cv_file(filename, branch)
            results[filename] = local_path
        except Exception as e:
            logger.error(f"Skipping {filename} due to error: {str(e)}")
    
    # Print summary
    success_count = len(results)
    logger.info(f"Successfully fetched {success_count}/{len(CV_FILES)} CV files")
    
    return results


def get_cv_path(collection_name: str) -> Optional[Path]:
    """
    Get the local path to a CV file.
    
    Args:
        collection_name: Name of the collection (e.g., 'activity_id')
        
    Returns:
        Path to the local CV file, or None if the file doesn't exist
    """
    filename = f"input4MIPs_{collection_name}.json"
    file_path = LOCAL_CV_DIR / filename
    
    if not file_path.exists():
        logger.warning(f"CV file not found: {file_path}")
        return None
    
    return file_path


if __name__ == "__main__":
    # Fetch all CV files when run directly
    fetch_all_cv_files()
