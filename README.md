# Getting Started

## 1. Create a Project Folder
- Choose a location on your computer (e.g., C:\Users\YourName\Documents).
- Create a new folder named python_project.
- Save the Python script inside this folder.
- This will keep everything organized when running the script.

## 2. Install Virtual Environment & Dependencies
- Open Command Prompt (cmd).
- Navigate to the python_project folder:
```
cd path\to\python_project
```
- Run the following commands to set up a virtual environment and install required packages:
```
pip install virtualenv
python -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process   # (For PowerShell users)
venv/Scripts/Activate.ps1  # (For Windows, use `venv\Scripts\activate` in cmd)
```
  
