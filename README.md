# Welcome to EMIS x Analytics 👋

This repository contains all the code EMIS uses to extract, transform, load, analyze medical, patient data etc.

# Getting started
You should locally have:
- Docker
- Python 3.8 with the following libraries
- PyCharm

# Stack
The stack we use is:
- Amazon S3
- Databricks
- Docker

# Project structure

The following project structure is designed to be scalable, containerizable and simple.

```
emis-dataeng-itw/
├── .azuredevops/                      # Azure DevOps CI/CD pipeline definitions for all projects
│   ├── ci-pipeline.yml                # Continuous Integration pipeline
│   └── cd-pipeline.yml                # Continuous Deployment pipeline
├── terraform/                         # Terraform infrastructure as code for all projects
│   ├── main.tf                        # Main Terraform configuration
│   ├── variables.tf                   # Terraform variables definition
│   └── outputs.tf                     # Terraform outputs definition
├── common/
│   ├── etl/
│   │   ├── abstract_etl.py            # Abstract ETL class
│   │   └── abstract_elt.py            # Abstract ELT class (if needed)
│   └── utils/
│       ├── __init__.py
│       └── s3_handler.py              # S3 interaction utility
├── fhir/
│   ├── src/
│   │   ├── lib/                        # Shared code for the fhir project
│   │   │   ├── __init__.py
│   │   │   ├── api_client.py           # Code to interact with APIs
│   │   │   └── ...                     # Other shared utilities
│   │   ├── json_to_tabular/            # Module for JSON to tabular ETL process
│   │   │   ├── __init__.py
│   │   │   ├── main.py                 # Main ETL script for JSON to tabular
│   │   │   ├── extract.py              # Extraction logic for JSON to tabular
│   │   │   ├── transform.py            # Transformation logic for JSON to tabular
│   │   │   └── load.py                 # Loading logic for JSON to tabular
│   │   └── extract_patient_ids/        # Module for extracting patient IDs
│   │       ├── __init__.py
│   │       ├── main.py                 # Main script for extracting patient IDs
│   │       └── ...                     # Other scripts specific to this use case
│   ├── tests/
│   │   ├── json_to_tabular/
│   │   │   ├── __init__.py
│   │   │   ├── test_extract.py
│   │   │   ├── test_transform.py
│   │   │   └── test_load.py
│   │   ├── extract_patient_ids/
│   │   │   ├── __init__.py
│   │   │   └── test_extract.py
│   │   └── lib/
│   │       └── test_api_client.py
│   ├── airflow/
│   │   ├── dags/
│   │   │   └── fhir_dag.py            # Airflow DAG for FHIR project
│   │   └── plugins/
│   │       └── custom_operator.py     # Custom Airflow operators for FHIR
│   ├── docker/
│   │   ├── Dockerfile
│   │   └── docker-compose.yml         # Docker configuration for FHIR project
│   └── env/
│       ├── .env.development           # Environment variables for development
│       ├── .env.staging               # Environment variables for staging
│       └── .env.production            # Environment variables for production
├── xxbc/
│   (similar structure for the XXBC project)
├── docker-compose.override.yml        # Overrides for local development for all projects
├── docker-compose.dev.yml             # Docker Compose for development environment for all projects
├── docker-compose.staging.yml         # Docker Compose for staging environment for all projects
├── docker-compose.prod.yml            # Docker Compose for production environment for all projects
└── README.md                          # Repository documentation
```
