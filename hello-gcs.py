from airflow import DAG
from airflow.operators import PythonOperator
dag = DAG(
    'add_gcp_connection',
    default_args=default_args,
    schedule_interval="@once")

# Task to add a connection
t1 = PythonOperator(
    dag=dag,
    task_id='add_gcp_connection_python',
    python_callable=add_gcp_connection,
    provide_context=True,
)