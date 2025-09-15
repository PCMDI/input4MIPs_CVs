#!/usr/bin/env python3
"""
Script to set up ESGVOC configuration for the input4MIPs project.
"""

import logging
import os
from pathlib import Path

from esgvoc.core import service
from esgvoc.core.service.state import ProjectSettings

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def setup_esgvoc_config(
    github_repo: str = "https://github.com/ltroussellier/test_new_CV",
    branch: str = "devel",
    local_path: str = "repos/test_new_CV",
    db_path: str = "dbs/input4mips.sqlite"
) -> None:
    """
    Set up ESGVOC configuration for the input4MIPs project.
    
    Args:
        github_repo: URL of the GitHub repository
        branch: Branch name to use
        local_path: Local path for the repository
        db_path: Path to store the database
    """
    try:
        # Check if config manager is available
        if service.config_manager is None:
            logger.error("ESGVOC config manager is not available")
            return
        
        # Switch to default config first
        service.config_manager.switch_config("default")
        m_config = service.config_manager.get_active_config()
        logger.info(f"Using base configuration: {m_config}")
        
        # Add input4mips project to the configuration
        m_config.projects["input4mips"] = ProjectSettings(
            project_name="input4mips",
            github_repo=github_repo,
            branch=branch,
            local_path=local_path,
            db_path=db_path
        )
        
        # Save the configuration with a new name
        config_name = "input4mips_config"
        service.config_manager.save_config(m_config.dump(), config_name)
        logger.info(f"Saved configuration as '{config_name}'")
        
        # Switch to the new configuration
        service.config_manager.switch_config(config_name)
        logger.info(f"Switched to configuration: {config_name}")
        
        # Synchronize the configuration
        current_state = service.get_state()
        logger.info("Synchronizing project state...")
        current_state.synchronize_all()
        logger.info("Synchronization complete")
        
    except Exception as e:
        logger.error(f"Error setting up ESGVOC configuration: {str(e)}")
        raise


if __name__ == "__main__":
    
    # Set up the configuration
    setup_esgvoc_config()
