'''
A virtual environment (venv) is an isolated Python environment for a project.

Meaning:

    separate Python packages
    separate dependencies
    separate versions

One project's packages won't affect another project.

    Project A requires Django 4.0 (say)
    Project B requires Django 5.0 (say)

Globally installing pip install django - causes version conflicts. Only one version can be active globally.

Solution - create a virtual environment for each project

How to create a virtual environment?

    python -m venv venv_name_you_want_to_give
    creates folders 
        
    venv/
        Scripts/
        Lib/
        Include/
        pyvenv.cfg
    
    Activate virtual environment

       venv\Scripts\activate

    Now if you install anything it will be installed in Lib folder - installed locally to the virtual environment

    Deactivate virtual environment

        deactivate
    
Install Requirements

    pip freeze > requirements.txt (creates a file called requirements.txt) - saves the list of installed packages in the virtual environment

    pip install -r requirements.txt (installs the packages in the requirements.txt file) 

Virtual environment (venv) is an isolated Python environment
used to manage project-specific packages and dependencies
without affecting global Python installation or other projects.

'''