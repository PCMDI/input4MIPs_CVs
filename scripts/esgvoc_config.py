from esgvoc.core import service
from esgvoc.core.service.state import ProjectSettings

##### Create context
if service.config_manager is not None : 
    service.config_manager.switch_config("default")
    m_config = service.config_manager.get_active_config()
    print(m_config)
    m_config.projects["input4mips"] = ProjectSettings(project_name= "input4mips",
                                                     github_repo="https://github.com/ltroussellier/test_new_CV",
                                                     branch="main",
                                                     local_path="repos/test_new_CV",
                                                     db_path="dbs/input4mips"
                                                     ) 
    
    service.config_manager.save_config(m_config.dump(),"test_input4mips")
   
    service.config_manager.switch_config("test_input4mips")
    current_state = service.get_state()
    # print(current_state)
    current_state.synchronize_all()

