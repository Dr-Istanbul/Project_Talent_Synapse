# skills_pipeline_dag.py
from airflow import DAG
from airflow.providers.amazon.aws.operators.s3 import S3ListOperator

with DAG('skills_etl', schedule_interval='@daily') as dag:
    extract_profiles = PythonOperator(
        task_id='extract_profiles',
        python_callable=extract_user_profiles
    )
    
    process_skills = PythonOperator(
        task_id='process_skills',
        python_callable=run_skill_extraction
    )