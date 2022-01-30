from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator

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
    'run_terraform',
    default_args=default_args,
    description='run terraform to init gcp vm instances, run script and send data to bucket',
    schedule_interval='*59 23 * * *',
    start_date=datetime(2021, 12, 1, 23, 59, 0),
    catchup=False,
    tags=['terraform'],
) as dag:

    t1 = BashOperator(
        task_id='init',
        depends_on_past=False,
        bash_command='terraform init',
    )
    t1.doc_md = dedent(
        """\
    #### Task Documentation
        Run terraform init
    """
    )
    t2 = BashOperator(
        task_id='apply',
        depends_on_past=False,
        bash_command='terraform -auto-approve apply',
    )
    t2.doc_md = dedent(
        """\
    #### Task Documentation
        Run terraform apply
    """
    )
    t3 = BashOperator(
        task_id='destroy',
        depends_on_past=False,
        bash_command='terraform -auto-approve destroy',
    )
    t3.doc_md = dedent(
        """\
    #### Task Documentation
        Run terraform destroy
    """
    )
    
    t1 >> t2 >> t3

    dag.doc_md = __doc__  # providing that you have a docstring at the beginning of the DAG
