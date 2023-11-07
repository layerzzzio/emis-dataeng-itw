Welcome to EMIS x Analytics

# Objective

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
│   │   ├── json_to_tabular.py         # Top-level ETL script for JSON to tabular
│   │   ├── extract_patient_ids.py     # Top-level ELT script for extracting patient IDs
│   │   ├── json_to_tabular/           # Directory for functions related to JSON to tabular use case
│   │   │   ├── __init__.py
│   │   │   └── some_function.py
│   │   ├── extract_patient_ids/       # Directory for functions related to extract patient IDs use case
│   │   │   ├── __init__.py
│   │   │   └── another_function.py
│   │   └── lib/
│   │       ├── __init__.py
│   │       └── api_client.py          # Code to interact with APIs
│   ├── tests/
│   │   ├── json_to_tabular/
│   │   │   ├── __init__.py
│   │   │   └── test_some_function.py
│   │   ├── extract_patient_ids/
│   │   │   ├── __init__.py
│   │   │   └── test_another_function.py
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
