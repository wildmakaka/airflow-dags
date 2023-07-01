from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello_world-0701100710",
}

dag = DAG(
    "hello_world-0701100710",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello_world.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_d7a05a9c_d628_4e33_a89b_5034d5acddf6 = NotebookOp(
    name="hello",
    namespace="ml-workshop",
    task_id="hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/hello.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="hello_world-0701100710",
    cos_dependencies_archive="hello-d7a05a9c-d628-4e33-a89b-5034d5acddf6.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_d7a05a9c_d628_4e33_a89b_5034d5acddf6.image_pull_policy = "IfNotPresent"


notebook_op_696b8b6f_4ca9_4353_b066_bc2ec9a2a4f7 = NotebookOp(
    name="world",
    namespace="ml-workshop",
    task_id="world",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/world.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="hello_world-0701100710",
    cos_dependencies_archive="world-696b8b6f-4ca9-4353-b066-bc2ec9a2a4f7.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_696b8b6f_4ca9_4353_b066_bc2ec9a2a4f7.image_pull_policy = "IfNotPresent"

(
    notebook_op_696b8b6f_4ca9_4353_b066_bc2ec9a2a4f7
    << notebook_op_d7a05a9c_d628_4e33_a89b_5034d5acddf6
)
