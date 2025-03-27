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

#### ***Project Workflow***

- We will update code in the following files in this sequence
1. constant
2. config_entity
3. artifact_entity
4. component
5. pipeline
6. app.py, demo.py


### **6. Data Ingestion**

- Before we work on "Data Ingestion" component >> Declare variables within constants. `__init__.py` file >> 
- First we have data localy. We need to put it in to the mongodb. We will do this using `notebooks/mongodb_experiments.ipynb`.
- Then we will pull this data from mongodb for our project.
    - add code to `configuration/mongo_db_connections.py` file and - define the func for mondodb connection >> 
    - Inside "data_access" folder, add code to `vehicle_data.py` that will use `mongo_db_connections.py` to connect with DB, fetch data in key-val format and transform that to df >>
    - add code to `entity/config_entity.py` file till DataIngestionConfig class >>
    - add code to entity.artifact_entity.py file till DataIngestionArtifact class >>
    - add code to components.data_ingestion.py file >> add code to training pipeline >> 
    - run demo.py (set mongodb connection url first, see next step)

    - To setup the connection url open powershell terminal and run below command:
    
    - ***For Powershell***
    ```bash
    set: $env:MONGODB_URL = "mongodb url..."
    check: echo $env:MONGODB_URL
    ```

### **7. Data Validation, Data Transformation & Model Trainer**

- Complete the work on `utils.main_utils.py` and `config.schema.yaml` file (add entire info about dataset for data validation step).
- Now work on the "Data Validation" component the way we did for Data Ingestion. (Workflow mentioned below)
- Now work on the "Data Transformation" component the way we did in above step. (add estimator.py to entity folder)
- Now work on the "Model Trainer" component the way we did in above step. (add class to estimator.py in entity folder)

### **8. Model Evaluation & Push To AWS S3 Bucket**


- Before moving to next component of Model Evaluation, some AWS services setup is needed:
    * Login to AWS console.
      * Keep region set as - us-east-1
      * Go to IAM >> Create new user (name: vehicle-proj)
      * Attach policy >> select AdministratorAccess >> next >> create user
      * Go to the user >> Security Credentials >> Access Keys >> Create access key
      * Select CLI >> agree to condition >> next >> Create Access Key >> download csv file
      * Set env variables with above csv values using below method:
      ====================================================================================
         >> Set env var from bash terminal: <<
         export AWS_ACCESS_KEY_ID="AWS_ACCESS_KEY_ID"
         export AWS_SECRET_ACCESS_KEY="AWS_SECRET_ACCESS_KEY"
         >> Check env var from bash terminal: <<
         echo $AWS_ACCESS_KEY_ID
         echo $AWS_SECRET_ACCESS_KEY

         >> Set env var from powershell terminal: <<
         $env:AWS_ACCESS_KEY_ID="AWS_ACCESS_KEY_ID downloaded in csv"
         $env:AWS_SECRET_ACCESS_KEY="AWS_SECRET_ACCESS_KEY downloaded in csv"
         >> Check env var from powershell terminal: <<
         echo $env:AWS_ACCESS_KEY_ID
         echo $env:AWS_SECRET_ACCESS_KEY
      ====================================================================================
      * Now add the access key, secret key, region name to constants.__init__.py
      * Add code to src.configuration.aws_connection.py file (To work with AWS S3 service)
      * Ensure below info in constants.__init__.py file:
            MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
            MODEL_BUCKET_NAME = "my-vehicle-mlopsproj"
            MODEL_PUSHER_S3_KEY = "model-registry"
      * Go to S3 service >> Create bucket >> Region: us-east-1 >> General purpose >>
        Bucket Name: "my-vehicle-mlopsproj" >> uncheck: "Block all public access" and acknowledge >>
        Hit Create Bucket
      * Now inside "src.aws_storage" code needs to be added for the configurations needed to pull 
        and push model from AWS S3 bucket. 
      * Inside "entity" dir we will have an "s3_estimator.py" file containing all the func to pull/push
        data from s3 bucket.

### **9. Making Prediction With Best ML Model Using FastApi**

- Create the code structure of "Prediction Pipeline" and setup your app.py. For this we will use `fastapi` framework.
-  Add "static" and folder in such a way that `static/css/style.css`. 
- "templates" dir to the project in such a way that `templates/vehicledata.html`.
- Once you do this add code in app.py. 
  - Run `app.py` with this command:
    ```python
    python app.py
    ```

  - Open this address on your browser to experiment with UI.
    ```python
    http://localhost:5000/
    ```

    - Use Following values as input:    
        `
        1  25  1  15  0 28711  152 239  1  0  1
        `  
### **9. Implementing CICD**


Getting started with CI-CD process:
  * Setup the dockerfile (mention files that needs to be dockerized) and .dockerignore (mention files that needs to be ignored by docker) files.
  * Setup the .github\workflows dir and aws.yaml file within as `.github/workflows/`
  * Go to AWS console and create a new IAM user exactly the way we did earlier or use the same

  * Now create one `ECR repo to store/save docker image`:
        AWS console >> Go to ECR >> Region: us-east-1 >> Hit create repository >>
        repo name: `vehicleproj` >> hit create repository >> copy and keep uri
  * Now create EC2 Ubuntu server >> AWS console >> EC2 >> Launch Instance >> name: `vehicledata-machine`
    >> Image: Ubuntu >> AMI: Ubuntu Server 24.04 (free tier) >> Instance: T2 Medium (~chargeable-3.5rs/hr)
        
    >> create new key pair (name: proj1key) >> allow for https and http traffic >> storage: 30gb >> Launch
    
    >> Go to instance >> click on "Connect" >> Connect using EC2 Instance Connect 
    
    >> Connect (Terminal will be launched) 

- Open EC2 and Install docker in EC2 Machine:
    ### **Optinal**

    ```python
    sudo apt-get update -y
    sudo apt-get upgrade -y
    ```
      
    ### **Required (Because Docker is'nt there in our EC2 server - [docker --version])**

    ```python
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
    ```

    - In order to verify if docker installed:
    ```python
    docker ps
    ```  



- Next step is to connect Github with EC2(Self hosted runner):

  * select your project on Github >> go to settings >> Actions >> Runner >> New self hosted runner
        
     >> Select OS (Linux) >> Now step by step run all "Download" related commands on EC2 server 
        
    >> run first "Configure" command (hit enter instead of setting a runner group, runner name: self-hosted)
        
    >> enter any additional label (hit enter to skip) >> name of work folder (again hit enter)
        
    >> Now run second "Configure" command (./run.sh) and runner will get connected to Github
        
    >> To crosscheck, go back to Github and click on Runner and you will see runner state as "idle"
        
    >> If you do ctrl+c on EC2 server then runner will shut then restart with "./run.sh"

1.  Setup your Github secrets: (Github project>Settings>SecretandVariable>Actions>NewRepoSecret)
    
    AWS_ACCESS_KEY_ID
    
    AWS_SECRET_ACCESS_KEY
    
    AWS_DEFAULT_REGION
    
    ECR_REPO

2.  CI-CD pipeline will be triggered at next commit and push.
3.  Now we need to activate the 5000 port of our EC2 instance:
      * Go to the instance > Security > Go to Security Groups > Edit inbound rules > add rule
        > type: Custom TCP > Port range: 5080 > 0.0.0.0/0 > Save rules
4.  Now paste the public ip address on the address bar +:5080 and your app will be launched.
5.  You can also do model training on /training route
6.  (Optional) Now if you want your machine keep running 
    ```python
    cd ~/actions-runner
    ```
    - Set up the runner as a service:
    ```python
    sudo ./svc.sh install
    ``` 

    - Again start the service:
    ```python
    sudo ./svc.sh start
    ``` 
    
    - To check status of the service:
    ```python
    sudo ./svc.sh status
    ``` 

- Now in order to stop the services first comment of content in `cicd.yaml`.

- Then delete rest of the aws credentials as `IAM`, `ECR`, `EC2`.