import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG, macros

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator

DAG_RUN_DATE = '{{ dag_run.start_date.strftime("%Y-%m-%d") }}'

# load environment variables
load_dotenv()

# gcp bucket
BUCKET = os.getenv('GCP_BUCKET')

# download location
DATA_PATH =  os.getenv('DOWN_PATH')

# check whether file storage is a bucket or a NFS path
DOWNLOAD_COMMAND = 'gsutil cp -r gs://{}/{}* {}'.format(BUCKET, DATA_PATH, DAG_RUN_DATE)

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'CLOUDACTIVEWEB',
    'depends_on_past': False,
    'email': [],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
with DAG(
    'down_data',
    default_args=default_args,
    description='download data from GCP bucket',
    schedule_interval='59 23 * * *',
    start_date=datetime(2021, 12, 1, 23, 59, 0),
    catchup=False,
    tags=['download'],
) as dag:

    t1 = BashOperator(
        task_id='download',
        depends_on_past=False,
        bash_command=DOWNLOAD_COMMAND,
    )

    t1.doc_md = dedent(
        """\
    #### Task Documentation
        Download data from GCP bucket.
    """
    )

    dag.doc_md = __doc__  # providing that you have a docstring at the beginning of the DAG