# CV Build Test for a New Project  

## Objective  
This project aims to build the CV for a new project.  

### **Input & Output**  
- **Input CV:** [PCMDI/input4MIPs_CVs](https://github.com/PCMDI/input4MIPs_CVs/tree/main/CVs)  
- **Output:** A repository compatible with the ESGVOC library: [ESGF Vocabulary](https://esgf.github.io/esgf-vocab/)  

---

## **Project Steps & Progress**  

### **1. Repository Setup**  
- Create a new repository or a branch within an existing one to store the new project CV format (this repository).  

### **2. Define the DRS (Directory, Filename, Dataset Name)**  
- Most projects have a **DRS** linked to the CV.  
- Define the DRS in the correct format.  
- Example: [CMIP6Plus Project Specs](https://github.com/WCRP-CMIP/CMIP6Plus_CVs/blob/esgvoc/project_specs.json).  

**Tracking history:**  
- A simple script (`scripts/build_drs.py`) will be used to track the history of each file.  
- This script is project-specific (not reusable) and was written for efficiency.  
- **Output:** `project_spec.json` is created!  

---

### **3. Create Directories for Each Collection**  
Each collection requires a directory containing **terms** and **context** files.  

#### **Example: "activity" Collection**  
- Source: [input4MIPs_activity_id.json](https://github.com/PCMDI/input4MIPs_CVs/blob/main/CVs/input4MIPs_activity_id.json).  
- It contains only one term: **input4MIPs**.  

#### **Checking CMIP Universe Compatibility**  
- Verify if the term exists in the **CMIP Universe**:  
  [WCRP-Universe Activity](https://github.com/WCRP-CMIP/WCRP-universe/tree/esgvoc/activity)  
- **Result:** **Not found**.  

#### **Two Solutions**  
1. **Request Addition:** Open an issue in the **WCRP-Universe repository**.  
2. **Create a New Term** (not covered here).  

Once the term is added to the WCRP-Universe repository, proceed with the following steps:  

#### **Steps to Integrate in This Repository**  
1. **Create a directory** → `input4MIPs_activity_id/`  
2. **Add a context file** → `000_context.jsonld`  
   - Use an existing template:  
     [Example Context File](https://github.com/WCRP-CMIP/CMIP6Plus_CVs/blob/esgvoc/activity_id/000_context.jsonld).  
3. **Add the term definition** → `input4MIPs.json`  
   - Fetch relevant data from the **CMIP Universe**.  
   - Use an existing example:  
     [Example Term File](https://github.com/WCRP-CMIP/CMIP6Plus_CVs/blob/esgvoc/activity_id/cmip.json).  
   - Modify the ID to match the universe's ID.  

---

### **Repeat for Each Collection & Required Terms**  
Follow the above steps for all necessary collections and terms. 


#### institution_id 

institution is a known datadescriptor in the universe. 
##### Create context

lets take the institution context and copy/paste it in a input4MIPs_institution_id directory  

##### Create terms

then, for each term, check if it exists in universe, if not : ask for it the be registered 

for now those are missing : 
CR not found in universe
DRES not found in universe
UCLA not found in universe
uoexeter not found in universe
+ 
CNRM-Cerfacs is CNRM-CERFACS in universe 


#### source_id 
this one is interesting ! 

this collection is exactly the same as the datadescriptor source in the universe. 
BUT not every term here are part of the universe. Go to issues in universe to add it 
and then the term in this repo, in this collection will be a link to these future one. 

#### dataset_category

this one is interesting too ! 
this collection does not have an equivalent in the universe. But looking at existaing one, it seems that it could be the same meaning as "realm". so the idea is to add these term in universe in realm ? go to issues in universe to add it. Or even ask if realm is the good datadescriptor to put those term in 

here we have added those one in realm (for example purposes, but seems OK for now)  

when this is done, we can then create terms here witch are only link to those in univere realm 


#### license 
this is also an interesting one
this one is pretty easy, there is already the term "CC BY 4.0" in the universe, therefore we just have to create a collection input4MIPs_license with a term in json file that point to universe term. 
but, there is a key, value that is not the same in the universe "conditions", we will add it here. 

#### mip_era 

this one exists in universe and all input4MIPs terms are all present, lets use them 

#### product 

this one exists in universe, it only misses "reanalyses", ==> issue in universe. Then we can create input4MIPs terms

#### publication status
this one is interesting as well ! 
it doesnt exist in universe, and nothing that already exist have the same meaning  ==> issues on universe in order to add this new datadesciptors and terms  
Then we will create those term 

#### target_mip
this one is also intersting 
the collection in input4MIPs is called target_mip but there the "activity" datadescriptor in universe that seems do be exactly what it described. But this a nested dict with "mip_era" as key for the first level. this kind of link is not CV (cf CV-TaskTeam work). what we can do is specified the "mip_era" in each terms here but the activity is picked from universe. 
in addition, there is no "prototype" term in activity in universe ==> issues in universe


### Esgvoc
the basic access to input4MIPs CV is now possible
lets try the DRS app with all this new defined CV !



That’s all, folks! 🚀
