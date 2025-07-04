from airflow import DAG
import airflow     
from airflow.operators.bash import BashOperator 


OUTPUT_DIR = "/opt/airflow/output"
dag = DAG(
    dag_id = "wiki_data" ,
    start_date = airflow.utils.dates.days_ago(4),
    schedule_interval= None
)


get_data = BashOperator (
    task_id = "get_data",
    bash_command = (
        f"curl -o {OUTPUT_DIR}/wiki/wikipageview.gz "
        "https://dumps.wikimedia.org/other/pageviews/"
        "{{ execution_date.year }}/"
        "{{ execution_date.year }}-{{ '{:02}'.format(execution_date.month) }}/"
        "pageviews-{{ execution_date.year }}"
        "{{ '{:02}'.format(execution_date.month) }}"
        "{{ '{:02}'.format(execution_date.day) }}-"
        "{{ '{:02}'.format(execution_date.hour-4) }}0000.gz" 
        # f"curl -o {OUTPUT_DIR}/wiki/wikipageview.gz "
        # "https://dumps.wikimedia.org/other/pageviews/"
        # "{{ execution_date.year }}/"
        # "{{ execution_date.year }}-{{ '{:02}'.format(execution_date.month) }}/"
        # "pageviews-{{ execution_date.year }}"
        # "{{ '{:02}'.format(execution_date.month) }}"
        # "{{ '{:02}'.format(execution_date.day) }}-"
        # "{{ '{:02}'.format(execution_date.hour-4) }}0000.gz"
        ) ,

        dag = dag
        
       
    )




get_data