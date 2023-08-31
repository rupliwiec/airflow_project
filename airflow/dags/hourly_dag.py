from airflow import DAG
from datetime import datetime

from fetch.petrol import Petrol
from fetch.weather import Weather
from fetch.population import Population