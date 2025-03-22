# Vehicle-Insurance-Domain-Mlops-Project

- This repository will contain source code related to Vehicle Insurance Domain Mlops Project.



### **1. Create a `template.py` file:**

- We will create a template.py file that will contain this code:
    
    ```python
    import os  # Importing the os module for operating system dependent functionality
    from pathlib import Path  # Importing Path for handling filesystem paths

    project_name = "src"  # Defining the main project directory name

    # List of file paths to be created within the project structure
    list_of_files = [
        f"{project_name}/__init__.py",  # Package initialization file
        f"{project_name}/components/__init__.py",  # Initialization for components package
        f"{project_name}/components/data_ingestion.py",  # Data ingestion module
        f"{project_name}/components/data_validation.py",  # Data validation module
        f"{project_name}/components/data_transformation.py",  # Data transformation module
        f"{project_name}/components/model_trainer.py",  # Model training module
        f"{project_name}/components/model_evaluation.py",  # Model evaluation module
        f"{project_name}/components/model_pusher.py",  # Model deployment module
        f"{project_name}/configuration/__init__.py",  # Initialization for configuration package
        f"{project_name}/configuration/mongo_db_connection.py",  # MongoDB connection module
        f"{project_name}/configuration/aws_connection.py",  # AWS connection module
        f"{project_name}/cloud_storage/__init__.py",  # Initialization for cloud storage package
        f"{project_name}/cloud_storage/aws_storage.py",  # AWS cloud storage module
        f"{project_name}/data_access/__init__.py",  # Initialization for data access package
        f"{project_name}/data_access/proj1_data.py",  # Data access module for project 1
        f"{project_name}/constants/__init__.py",  # Initialization for constants package
        f"{project_name}/entity/__init__.py",  # Initialization for entity package
        f"{project_name}/entity/config_entity.py",  # Configuration entity module
        f"{project_name}/entity/artifact_entity.py",  # Artifact entity module
        f"{project_name}/entity/estimator.py",  # Estimator module
        f"{project_name}/entity/s3_estimator.py",  # S3 estimator module
        f"{project_name}/exception/__init__.py",  # Initialization for exception handling package
        f"{project_name}/logger/__init__.py",  # Initialization for logging package
        f"{project_name}/pipline/__init__.py",  # Initialization for pipeline package
        f"{project_name}/pipline/training_pipeline.py",  # Training pipeline module
        f"{project_name}/pipline/prediction_pipeline.py",  # Prediction pipeline module
        f"{project_name}/utils/__init__.py",  # Initialization for utilities package
        f"{project_name}/utils/main_utils.py",  # Main utility functions module
        "app.py",  # Main application file
        "requirements.txt",  # File listing project dependencies
        "Dockerfile",  # Dockerfile for containerization
        ".dockerignore",  # File specifying files to ignore in Docker builds
        "demo.py",  # Demo script for the project
        "setup.py",  # Setup script for packaging the project
        "pyproject.toml",  # Configuration file for the project
        "config/model.yaml",  # YAML file for model configuration
        "config/schema.yaml",  # YAML file for data schema
    ]

    # Creating the file structure and files as specified in list_of_files
    for filepath in list_of_files:
        filepath = Path(filepath)  # Convert string path to a Path object
        filedir, filename = os.path.split(filepath)  # Split into directory and filename
        if filedir != "":  # Check if directory is not empty
            os.makedirs(filedir, exist_ok=True)  # Create directories if they don't exist
        # Create the file if it doesn't exist or is empty
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:  # Open file in write mode
                pass  # Create an empty file
        else:
            print(f"file is already present at: {filepath}")  # Notify if file already exists
    ``` 
    - This file will help us create the projects files with single command instead of manually creating it. Here is how to create project structure:
    ```python
    python template.py
    ```
### **2. Create a `setup.py` and `pyproject.toml`**
- We need to create a `setup.py` and `pyproject.toml` in order to import local packages for out project.

  - `setup.py` code will look like this:
    ```python
    from setuptools import setup, find_packages

    setup(
        name="src",
        version="0.0.1",
        author="Adil Naeem",
        author_email="madilnaeem0@gmail.com",
        packages=find_packages()
    )
    ```
    - `pyproject.toml` code will look like this:
    ```python
    [project]
    name = "src"
    version = "0.0.1"
    description = "An MLOps project for productionizing models"
    authors = [{name = "Adil Naeem", email = "madilnaeem0@gmail.com"}]

    [tool.setuptools]
    packages = {find = {}}

    [tool.setuptools.dynamic]
    dependencies = {file = "requirements.txt"}
    ```     

    - `requirements.txt` code will look like this
    ```bash
    ipykernel
    pandas
    numpy
    matplotlib
    plotly
    seaborn
    scikit-learn
    pymongo
    from_root
    dill
    certifi
    PyYAML
    boto3
    mypy-boto3-s3
    botocore
    fastapi
    python-multipart
    uvicorn
    jinja2
    imblearn
    -e .
    ```


### **3. Create a Conda Environment**

- To Create a conda environment:
    ```python
    conda create -p venv python=3.11 -y
    ```
- To actvate this environment:
    ```python
    conda activate venv\
    ```
- To Install `requirements.txt`:
    ```python
    pip install -r requirements.txt
    ```
- To remove this environment after use:
    ```python
    conda remove --name your_env_name --all -y
    ```

### **4. MongoDB Setup For Data Ingestion**

- Sign up to MongoDB Atlas and create a new project by just providing it a name then next next create.

- From "Create a cluster" screen, hit "create", Select M0 service keeping other services as default, hit "create deployment"

-  Setup the username and password and then create DB user.

- Go to "network access" and add ip address - "0.0.0.0/0" so that we can access it from anywhere.

- Go back to project >> "Get Connection String" >> "Drivers" >> {Driver:Python, Version:3.6 or later} 
   >> copy and save the connection string with you(replace password). >> Done.

   - Install it in terminal.
        ```python
        python -m pip install "pymongo[srv]"
        ``` 
    - Then you will copy a connection string which may look like this. We need to edit it for our use case.
        ```python
        mongodb+srv://madilnaeem0:<db_password>@cluster0.kra1i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
        ```   
    
- Dataset added to notebook folder
- Push your data to mongoDB database from your python notebook.
- Go to mongoDB Atlas >> Database >> browse collection >> see your data in key value format.

### **5. Set Up Logging and Exception**

- Go to `src/logger/__init__.py` and write logging code in it:
    ```python
    import logging
    import os
    from logging.handlers import RotatingFileHandler
    from from_root import from_root
    from datetime import datetime

    # Constants for log configuration
    LOG_DIR = 'logs'
    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
    BACKUP_COUNT = 3  # Number of backup log files to keep

    # Construct log file path
    log_dir_path = os.path.join(from_root(), LOG_DIR)
    os.makedirs(log_dir_path, exist_ok=True)
    log_file_path = os.path.join(log_dir_path, LOG_FILE)

    def configure_logger():
        """
        Configures logging with a rotating file handler and a console handler.
        """
        # Create a custom logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        
        # Define formatter
        formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

        # File handler with rotation
        file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.INFO)
        
        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    # Configure the logger
    configure_logger()
    ```
- Go to `src/exception/__init__.py` and write logging code in it:

    ```python
    import sys
    import logging

    def error_message_detail(error: Exception, error_detail: sys) -> str:
        """
        Extracts detailed error information including file name, line number, and the error message.

        :param error: The exception that occurred.
        :param error_detail: The sys module to access traceback details.
        :return: A formatted error message string.
        """
        # Extract traceback details (exception information)
        _, _, exc_tb = error_detail.exc_info()

        # Get the file name where the exception occurred
        file_name = exc_tb.tb_frame.f_code.co_filename

        # Create a formatted error message string with file name, line number, and the actual error
        line_number = exc_tb.tb_lineno
        error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"
        
        # Log the error for better tracking
        logging.error(error_message)
        
        return error_message

    class MyException(Exception):
        """
        Custom exception class for handling errors in the US visa application.
        """
        def __init__(self, error_message: str, error_detail: sys):
            """
            Initializes the USvisaException with a detailed error message.

            :param error_message: A string describing the error.
            :param error_detail: The sys module to access traceback details.
            """
            # Call the base class constructor with the error message
            super().__init__(error_message)

            # Format the detailed error message using the error_message_detail function
            self.error_message = error_message_detail(error_message, error_detail)

        def __str__(self) -> str:
            """
            Returns the string representation of the error message.
            """
            return self.error_message
    ```


