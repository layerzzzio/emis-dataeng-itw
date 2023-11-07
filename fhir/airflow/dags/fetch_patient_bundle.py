from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from fhir.src.fetch_patient_bundle.main import FetchPatientBundle

# Constants for the DAG
DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

SOURCE_API_URL = "http://api.fhir.org/v1/bundles"
S3_BUCKET = "your-s3-bucket-name"

# Initialize the ETL process outside the tasks to use across multiple tasks
etl_process = FetchPatientBundle(SOURCE_API_URL, S3_BUCKET)


def extract_task():
    etl_process.extract()


def transform_task(**kwargs):
    ti = kwargs['ti']
    extracted_data = ti.xcom_pull(task_ids='extract_task')
    etl_process.transform(extracted_data)


def load_task(**kwargs):
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(task_ids='transform_task')
    etl_process.load(transformed_data)


# Define the DAG
dag = DAG(
    'fetch_patient_bundle_dag',
    default_args=DEFAULT_ARGS,
    description='DAG for fetching FHIR patient bundles and loading to S3',
    schedule_interval=timedelta(days=1),
)

# Define the tasks
extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract_task,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_task',
    python_callable=transform_task,
    provide_context=True,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_task',
    python_callable=load_task,
    provide_context=True,
    dag=dag,
)

# Set the order of execution
extract_task >> transform_task >> load_task
