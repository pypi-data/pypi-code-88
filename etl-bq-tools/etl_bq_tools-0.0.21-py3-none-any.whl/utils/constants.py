"""This file of constants"""

# bq.py
txt_set_project_success = "Project update: {0}"
txt_set_project_errors = "Project Not Found: {0}"

txt_execute_sql_success = "Success file: {0}"
txt_execute_sql_errors = "Error file: {0}"

# bigquery.py
txt_create_dt_success = "Created dataset: {0}"
txt_create_dt_error = "Already Exists or ProjectID Not Found: {0}"

txt_delete_dt_success = "Deleted dataset: {0}"
txt_delete_dt_error = "Dataset Not Found: {0}"

txt_create_tb_success = "Created table: {0}"
txt_create_tb_error = "Already Exists or TableID Not Found: {0}"

txt_delete_tb_success = "Deleted table: {0}"
txt_delete_tb_error = "Not exists Table or TableID Not Found: {0}"

txt_query_to_df_success = "Success query to dataframe"
txt_query_to_df_errors = "Error query to dataframe"

txt_query_to_rows_success = "Success query to rows"
txt_query_to_rows_errors = "Error query to rows"

txt_truncate_success = "Success truncate query"
txt_truncate_errors = "Error truncate query"

txt_delete_partition_success = "Success delete range partition {0} to {1}"
txt_delete_partition_errors = "Error delete range partition {0} to {1}"

txt_restore_table_success = "Success restore table name {0}_RESTORE"
txt_restore_table_errors = "Error restore table name {0}_RESTORE"

# dataframe
txt_upload_df_to_bq_success = "Load Table {0} from dataframe"
txt_upload_df_to_bq_errors = "Provided Schema does not match table {0}"

# cloudstorage
txt_gs_bucket_list_objects_success = "list_blobs from  bucket {0}"
txt_gs_bucket_list_objects_errors = "BucketName Not Found {0}"

txt_gs_bucket_list_patterns_success = "list_blobs from  bucket {0}"
txt_gs_bucket_list_patterns_errors = "BucketName Not Found {0}"

txt_gs_bucket_list_to_df_success = "blobs from dataframe {0}/{1}"
txt_gs_bucket_list_to_df_errors = "BucketName Not Found {0} "

txt_bucket_download_file_success = "Download file: {0}"
txt_bucket_download_file_errors = "File Not Found {0}"

txt_bucket_upload_file_success = "Upload file: {0}"
txt_bucket_upload_file_errors = "File Not Found {0}"

txt_storage_delete_file_success = "Delete file: {0}"
txt_storage_delete_file_errors = "File Not Found {0}"

txt_storage_delete_folder_success = "Delete folder: {0}"
txt_storage_delete_folder_errors = "Folder Not Found {0}"

# dataset
txt_show_describe_table_success = "Success describe table {0}"
txt_show_describe_table_errors = "Error describe table {0}"
