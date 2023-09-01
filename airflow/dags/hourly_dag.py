from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from fetch.petrol import Petrol
from fetch.weather import Weather
from fetch.population import Population

dag = DAG(
    dag_id= 'hourly_tasks_dag',
    start_date= datetime(2023, 9, 1),
    schedule_interval= "@hourly"
)

run_fetch_belarus_petrol = PythonOperator(
    dag=dag,
    task_id = 'run_fetch_belarus_petrol',
    python_callable=Petrol('Belarus').fetch_petrol
)

run_fetch_armenia_petrol = PythonOperator(
    dag=dag,
    task_id= 'run_fetch_armenia_petrol',
    python_callable=Petrol('Armenia').fetch_petrol
)

run_fetch_minsk_weather = PythonOperator(
    dag=dag,
    task_id = 'run_fetch_belarus_weather',
    python_callable=Weather('minsk').fetch_weather
)

run_fetch_erevan_weather = PythonOperator(
    dag=dag,
    task_id= 'run_fetch_erevan_weather',
    python_callable=Weather('erevan').fetch_weather
)

run_fetch_belarus_population = PythonOperator(
    dag=dag,
    task_id = 'run_fetch_belarus_population',
    python_callable=Population('belarus').fetch_population
)

run_fetch_armenia_population = PythonOperator(
    dag=dag,
    task_id= 'run_fetch_armenia_population',
    python_callable=Population('armenia').fetch_population
)