import firebase_admin
from firebase_admin import credentials, firestore
from typing import List, Callable, Iterable
from streamstate_utils.k8s_utils import get_env_variables_from_config_map
from streamstate_utils.structs import FirestoreOutputStruct

# Use the application default credentials
def open_firestore_connection(project_id: str):
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(
        cred,
        {
            "projectId": project_id,
        },
    )
    return firestore.client()


def get_collection_from_org_name_and_app_name(org_name: str, app_name: str) -> str:
    return f"{org_name}_{app_name}"


def get_document_name_from_version_and_keys(key_values: list, code_version: str) -> str:
    pks = "_".join(key_values)
    return f"{pks}_{code_version}"


def apply_partition_hof(
    project_id: str,
    collection: str,
    code_version: str,
    primary_keys: List[str],
) -> Callable[[Iterable], None]:
    def apply_to_partition(rows):
        db = open_firestore_connection(project_id)
        doc_ref = db.collection(collection)
        for row in rows:
            row_dict = row.asDict()
            key_values = [row_dict[val] for val in primary_keys]
            document_name = get_document_name_from_version_and_keys(
                key_values, code_version
            )
            doc_ref.document(document_name).set(row_dict)

    return apply_to_partition


def get_firestore_inputs_from_config_map(
    app_name: str,
    code_version: str,
) -> FirestoreOutputStruct:
    env_var = get_env_variables_from_config_map()
    organization = env_var["organization"]
    project = env_var["project"]
    return FirestoreOutputStruct(
        firestore_collection_name=get_collection_from_org_name_and_app_name(
            organization, app_name
        ),
        project_id=project,
        # schema_version=schema_version,
        code_version=code_version,
    )
