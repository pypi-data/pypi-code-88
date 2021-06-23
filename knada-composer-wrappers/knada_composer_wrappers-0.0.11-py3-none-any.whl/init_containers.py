import kubernetes.client as k8s
import os


def create_read_bucket_init_container(bucket_path: str):
    return k8s.V1Container(
        name="read-bucket",
        image="navikt/knada-dbt:4",
        volume_mounts=[
            k8s.V1VolumeMount(
                name="data", mount_path="data", sub_path=None, read_only=False
            )
        ],
        command=["/bin/sh", "-c"],
        args=[
            f"gsutil cp -r gs://{os.environ['GCS_BUCKET']}/{bucket_path}/* data/"
        ],
    )
