"""
Airflow DAG and airflow Task 
"""


from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from Reddit import run_reddit_etl


#Default arguments for Airflow
default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}


#Creating a DAG
dag = DAG(
    'Reddit_dag',
    default_args=default_args,
    #Can add Schedule_interval to perform the ETL daily
    # schedule_interval='@daily'
    description="ETL for Reddit data pull"
)


#This is the actual task
run_etl = PythonOperator(
    task_id = 'complete_reddit_etl',
    python_callable = run_reddit_etl,
    dag = dag
)


#Running the Task
run_etl
