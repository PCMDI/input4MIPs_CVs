#!/usr/bin/env python3
"""
Utility script to generate standardized context files for CV collections.
"""

import json
import os
from pathlib import Path
from typing import Dict, Optional


def create_context_file(
    collection_name: str,
    DDtype: str,
    properties: Optional[Dict[str, str]] = None,
    base_url_path: Optional[str] = None,
) -> Path:
    """
    Create a context file for a collection.

    Args:
        collection_name: Name of the collection (e.g., 'target_mip')
        properties: Dictionary of additional properties to include in the context
        base_url_path: Override for the base URL path (defaults to collection_name)

    Returns:
        Path: Path to the created context file
    """
    # Create directory if it doesn't exist
    dir_name = f"input4MIPs_{collection_name}"
    os.makedirs(dir_name, exist_ok=True)

    # Use provided base_url_path or default to collection_name
    url_path = base_url_path if base_url_path else collection_name

    # Base context structure
    context = {
        "@context": {
            "@base": f"https://espri-mod.github.io/mip-cmor-tables/{DDtype}/",
            "@vocab": "http://schema.org/",
            "id": "@id",
            "type": "@type",
        }
    }

    # Add additional properties if provided
    if properties:
        for prop_name, prop_uri in properties.items():
            context["@context"][prop_name] = {"@id": prop_uri}

    # Write context file
    context_path = Path(dir_name) / "000_context.jsonld"
    with open(context_path, "w", encoding="utf-8") as f:
        json.dump(context, f, indent=4)

    return context_path
