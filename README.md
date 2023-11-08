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
│   │   ├── ingest_bundle_to_s3/       # IngestBundleToS3 microservice
│   │   │   ├── Dockerfile             # Dockerfile for IngestBundleToS3
│   │   │   ├── main.py                # Main script for IngestBundleToS3
│   │   │   ├── requirements.txt       # Dependencies for IngestBundleToS3
│   │   │   └── ...                    # Other source files for IngestBundleToS3
│   │   ├── transform_bundle_json_to_tabular/           # TransformBundleJsonToTabular microservice
│   │   │   ├── Dockerfile             # Dockerfile for TransformBundleJsonToTabular
│   │   │   ├── main.py                # Main script for TransformBundleJsonToTabular
│   │   │   ├── requirements.txt       # Dependencies for TransformBundleJsonToTabular
│   │   │   └── ...                    # Other source files for TransformBundleJsonToTabular
│   ├── tests/
│   │   ├── ingest_bundle_to_s3/
│   │   │   ├── test_main.py           # Tests for IngestBundleToS3
│   │   │   └── ...                    # Other test files for IngestBundleToS3
│   │   ├── transform_bundle_json_to_tabular/
│   │   │   ├── test_main.py           # Tests for TransformBundleJsonToTabular
│   │   │   └── ...                    # Other test files for TransformBundleJsonToTabular
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
