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
    "notebooks/mongodb_experiments.ipynb",  # notebook to data ingestion with mongodb
    "notebooks/experiments.ipynb",  # notebook to perform experiments with data
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