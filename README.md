# Welcome to EMIS x Analytics 👋

This repository contains all the code EMIS uses to extract, transform, load, analyze medical and patient data.

# Getting started

Download the following locally:
- Docker
- Python 3.8 with the following libraries ...
- PyCharm

# Stack

The stack we use is:
- Amazon S3
- Databricks
- Docker

# Project structure

The following project structure is designed to be scalable, containerized and simple.

```
emis-dataeng-itw/
├── .azuredevops/                      # Azure DevOps CI/CD pipeline definitions
│   ├── ci-pipeline.yml                # Continuous Integration pipeline
│   └── cd-pipeline.yml                # Continuous Deployment pipeline
├── terraform/                         # Terraform infrastructure as code
│   ├── main.tf                        # Main Terraform configuration
│   ├── variables.tf                   # Terraform variables definition
│   └── outputs.tf                     # Terraform outputs definition
├── common/                            # Shared code across projects
│   ├── etl/
│   │   ├── abstract_etl.py            # Abstract ETL class
│   │   └── abstract_elt.py            # Abstract ELT class
│   └── utils/
│       ├── __init__.py
│       └── s3_handler.py              # S3 interaction utility
├── fhir/                              # FHIR project
│   ├── src/
│   │   ├── fetch_patient_bundle/      # FetchPatientBundle microservice
│   │   │   ├── Dockerfile             # Dockerfile for FetchPatientBundle
│   │   │   ├── main.py                # Main script for FetchPatientBundle
│   │   │   ├── requirements.txt       # Dependencies for FetchPatientBundle
│   │   │   └── ...                    # Other source files for FetchPatientBundle
│   │   ├── json_to_tabular/           # JsonToTabular microservice
│   │   │   ├── Dockerfile             # Dockerfile for JsonToTabular
│   │   │   ├── main.py                # Main script for JsonToTabular
│   │   │   ├── requirements.txt       # Dependencies for JsonToTabular
│   │   │   └── ...                    # Other source files for JsonToTabular
│   │   └── extract_patient_ids/       # ExtractPatientIds microservice
│   │       ├── Dockerfile             # Dockerfile for ExtractPatientIds
│   │       ├── main.py                # Main script for ExtractPatientIds
│   │       ├── requirements.txt       # Dependencies for ExtractPatientIds
│   │       └── ...                    # Other source files for ExtractPatientIds
│   ├── tests/
│   │   ├── fetch_patient_bundle/
│   │   │   ├── test_main.py           # Tests for FetchPatientBundle
│   │   │   └── ...                    # Other test files for FetchPatientBundle
│   │   ├── json_to_tabular/
│   │   │   ├── test_main.py           # Tests for JsonToTabular
│   │   │   └── ...                    # Other test files for JsonToTabular
│   │   └── extract_patient_ids/
│   │       ├── test_main.py           # Tests for ExtractPatientIds
│   │       └── ...                    # Other test files for ExtractPatientIds
│   ├── airflow/
│   │   ├── dags/
│   │   │   └── fhir_dag.py            # Airflow DAG for FHIR project
│   │   └── plugins/
│   │       └── custom_operator.py     # Custom Airflow operators for FHIR
│   ├── env/
│   │   ├── .env.development           # Environment variables for development
│   │   ├── .env.staging               # Environment variables for staging
│   │   └── .env.production            # Environment variables for production
│   └── docker-compose.yml             # Docker Compose for FHIR project (for local development)
├── xxbc/                              # XXBC project (structured similarly to FHIR project)
├── docker-compose.override.yml        # Overrides for local development for all projects
├── docker-compose.dev.yml             # Docker Compose for development environment
├── docker-compose.staging.yml         # Docker Compose for staging environment
├── docker-compose.prod.yml            # Docker Compose for production environment
└── README.md                          # Repository documentation
```
