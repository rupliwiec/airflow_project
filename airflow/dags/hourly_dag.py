from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from fetch.petrol import Petrol
from fetch.weather import Weather
from fetch.population import Population

from scrape.scrape_petrol import ScrapePetrol
from scrape.scrape_weather import ScrapeWeather
from scrape.scrape_population import ScrapePopulation

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
    python_callable=Weather('yerevan').fetch_weather
)

run_fetch_belarus_population = PythonOperator(
    dag=dag,
    task_id = 'run_fetch_belarus_population',
    python_callable=Population('Belarus').fetch_population
)

run_fetch_armenia_population = PythonOperator(
    dag=dag,
    task_id= 'run_fetch_armenia_population',
    python_callable=Population('Armenia').fetch_population
)

run_scrape_belarus_petrol = PythonOperator(
    dag=dag,
    task_id = 'run_scrape_belarus_petrol',
    python_callable=ScrapePetrol('tmp/belarus_petrol_price.html').scrape,
    op_kwargs={'country': 'BYN'},
)

run_scrape_armenia_petrol = PythonOperator(
    dag=dag,
    task_id = 'run_scrape_armenia_petrol',
    python_callable=ScrapePetrol('tmp/armenia_petrol_price.html').scrape,
    op_kwargs={'country': 'ARM'},
)

run_scrape_minsk_weather = PythonOperator(
    dag=dag,
    task_id = 'run_scrape_minsk_weather',
    python_callable=ScrapeWeather('tmp/minsk_weather.html').scrape,
    op_kwargs={'city': 'MSK'},
)

run_scrape_yerevan_weather = PythonOperator(
    dag=dag,
    task_id = 'run_scrape_armenia_weather',
    python_callable=ScrapeWeather('tmp/yerevan_weather.html').scrape,
    op_kwargs={'city': 'YRN'},
)

run_scrape_belarus_population = PythonOperator(
    dag=dag,
    task_id = 'run_scrape_belarus_population',
    python_callable=ScrapePopulation('tmp/Belarus_total_population.html').scrape,
    op_kwargs={'country': 'BYN'},
)

run_scrape_armenia_population = PythonOperator(
    dag=dag,
    task_id = 'run_scrape_armenia_population',
    python_callable=ScrapePopulation('tmp/Armenia_total_population.html').scrape,
    op_kwargs={'country': 'ARM'},
)