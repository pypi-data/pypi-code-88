import os
import base64

from ml_metadata.proto import Artifact
from mlmd.dataset_manager_scheme import ArtifactType, ExecutionType, ContextType
from mlmd.dataset_manager_dao import *
from dataset_management.utils import generate_version_id
from dataset_management.blob import _upload_blob, get_bucket_name, list_blob, _download_blob
import datetime
from multiprocessing import Array, cpu_count, Pool

from mlmd.metadata_dao import get_annotation_stats, get_image_metadata, get_model_info_by_dataset, get_tenant_id, get_training_history, insert_image_log_bulk, insert_image_metadata_bulk, get_image_executions_by_version
from .triggers import ApiTrigger

class Dataset():
    def __init__(self, datasetname, version="latest", username="Anomymous") -> None:        
        dataset = get_artifact_by_type_and_name(ArtifactType.DATASET, datasetname)
        if dataset is None:
            raise Exception("Dataset {} not found".format(datasetname))
        self.metadata = dataset.properties
        self.datasetname = dataset.name
        self.created_at = datetime.datetime.fromtimestamp(dataset.create_time_since_epoch//1000.0)
        self.id = dataset.id
        self.username = username
        self.version = version
        if self.version == "latest":
            self.version = self.metadata["latest_version"].string_value
        self.uncommitted_version = self.metadata["uncommitted_version"].string_value
        self.filelist = self.get_filelist()
        self.trigger = ApiTrigger.from_json_string(self.metadata["trigger"].string_value)

    def __str__(self) -> str:
        return str({
            "name": self.datasetname,
            "version": self.version,
            "tags": self.metadata["tags"].string_value,
            "created_by": self.metadata["created_by"].string_value,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        })

    def list_staged_executions(self):
        tobe_committed_ctx = get_context(ContextType.COMMIT_DATASET_VERSION, self.uncommitted_version)
        return [{
            "execution": get_type_name_from_id(exe.type_id),
            "file_location": exe.properties["file_location"].string_value,
            "tenant": exe.properties["tenant"].string_value,
            "annotation": exe.properties["annotation"].string_value,
            "executed_by": exe.properties["executed_by"].string_value,
            "executed_at": datetime.datetime.fromtimestamp(exe.create_time_since_epoch//1000.0).strftime("%Y-%m-%d %H:%M:%S")
        } for exe in get_executions_by_context(tobe_committed_ctx.id)]


    def list_versions(self, short=False):
        if short:
            return [ctx.name for ctx in get_contexts_by_artifact(ContextType.COMMIT_DATASET_VERSION, self.id) if ctx.properties["committed_by"].string_value != ""]            
        return [
            {"version": ctx.name,
             "committed_by": ctx.properties["committed_by"].string_value,
             "commit_message": ctx.properties["commit_message"].string_value,
             "prev_version": ctx.properties["prev_ref"].string_value,
             "created_at": datetime.datetime.fromtimestamp(ctx.create_time_since_epoch//1000.0).strftime("%Y-%m-%d %H:%M:%S")
            } for ctx in get_contexts_by_artifact(ContextType.COMMIT_DATASET_VERSION, self.id) if ctx.properties["committed_by"].string_value != ""]

    def add_files_from_dir(self, _dir, override=False, annotation=None, tenant="unknown"):
        if _dir is None or os.path.isdir(_dir) == False:
            raise Exception("Data dir {} not valid".format(_dir))

        tenant_id = get_tenant_id(tenant)
        if tenant_id is None:
            raise Exception("Tenant {} is invalid".format(tenant))

        blobnamelist = {blob.name for blob in list_blob(get_bucket_name(self.datasetname))}

        files_in_dir = [ f for f in os.listdir(_dir) if os.path.isfile(os.path.join(_dir, f))]
        if override == True:
            filelist = files_in_dir
        else:
            filelist = [f for f in files_in_dir if f not in blobnamelist]

        arglist = [(_file, self.datasetname, _dir, {"annotation": annotation, "tenant": tenant}) for _file in filelist]
        if len(arglist) > 0:
            proc_count = cpu_count()
            if len(arglist) < cpu_count():
                proc_count = len(arglist)
            print("{}/{} is being uploaded by {} processes...".format(len(filelist), len(files_in_dir),proc_count))
            p = Pool(proc_count)
            r = p.map(_upload_blob, arglist)
            p.close()
            p.join()
            success_list = []
            for i,_ in enumerate(r):
                if r[i] == False:
                    print("Failed to update {} in changelist".format(self.changelist[i][0]))
                else:
                    success_list.append(r[i])
            print("Successfully uploaded {} files".format(len(success_list)))
        else:
            print("No file to upload. Override option is being set to {}".format(override))

        print("Creating image metadata...")
        exe_id = create_execution(ExecutionType.ADD_FILES_TO_DATASET, {"executed_by": self.username,"file_location": os.uname()[1] + ":" + os.path.abspath(_dir), "tenant": tenant, "annotation": annotation})
        #insert image metadata
        image_metadata = [(image_name, tenant_id, self.id, annotation) for image_name in files_in_dir]
        if len(image_metadata) > 0:
            image_metadata_ids = insert_image_metadata_bulk(image_metadata, return_ids=True)
            # execution and image artifacts link
            log_metadata = [(image_id, exe_id, self.uncommitted_version, self.id) for image_id in image_metadata_ids]
            if len(log_metadata) > 0:
                insert_image_log_bulk(log_metadata)

        # version and execution link
        if exe_id is None:
            print("No new image metadata. No execution created")
            return 
        ctx = get_context(ContextType.COMMIT_DATASET_VERSION, self.uncommitted_version)
        create_association_attribution(ctx.id, exe_id, None)
        print("Execution [{}] created".format(exe_id))
        return True

    def remove_files(self, filelist):
        if filelist is None or len(filelist) <= 0:
            return None
        exe_id = create_execution(ExecutionType.REMOVE_FILES_FROM_DATASET, {"executed_by": self.username})
        #insert image metadata
        image_names = [(image_name,) for image_name in filelist]
        image_metadata = get_image_metadata(image_names, self.id)
        image_metadata_ids = [item[0] for item in image_metadata]
        if len(image_metadata) > 0:
            log_metadata = [(image_id, exe_id, self.uncommitted_version, self.id) for image_id in image_metadata_ids]
            if len(log_metadata) > 0:
                insert_image_log_bulk(log_metadata)

        ctx = get_context(ContextType.COMMIT_DATASET_VERSION, self.uncommitted_version)
        return create_association_attribution(ctx.id, exe_id, None)

    def commit_version(self, commit_message="", trigger=None, ref_version=None):
        # update uncommited version to become official version
        tobe_committed_ctx = get_context(ContextType.COMMIT_DATASET_VERSION, self.uncommitted_version)

        if len(get_executions_by_context(tobe_committed_ctx.id)) <= 0:
            print("Nothing to commit")
            return False

        tobe_committed_ctx.properties["committed_by"].string_value = self.username
        tobe_committed_ctx.properties["prev_ref"].string_value = self.version if ref_version is None else ref_version
        tobe_committed_ctx.properties["commit_message"].string_value = commit_message
        update_context(tobe_committed_ctx)
        committed_version_id = tobe_committed_ctx.name
        # new uncommited version ref to committed version and its link
        new_uncommitted_version_id = generate_version_id()
        context_id = create_context(ContextType.COMMIT_DATASET_VERSION, new_uncommitted_version_id, None, self.version)
        create_association_attribution(context_id, None, self.id)

        update_artifact(ArtifactType.DATASET, self.datasetname, None, committed_version_id, new_uncommitted_version_id)
        self.uncommitted_version = new_uncommitted_version_id
        self.version = committed_version_id
        self.filelist = self.get_filelist()

        # execute trigger if have
        # if trigger is not None:
        #     trigger.execute()
        # elif self.trigger is not None:
        #     self.trigger.execute()
        return committed_version_id

    # def get_trigger(self):
    #     return ApiTrigger.from_json_string(self.metadata.get("trigger"))

    # def set_trigger(self, trigger: ApiTrigger):
    #     self.metadata["trigger"].string_value = str(trigger)
    #     self.trigger = trigger
    #     return update_artifact(ArtifactType.DATASET, self.datasetname, None, None, None, self.metadata["trigger"].string_value)

    def trigger_retrain(self, models=None, metadata_filter=None):
        url = os.environ.get("DATASET_MANAGEMENT_RETRAIN_URL")
        username = os.environ.get("DATASET_MANAGEMENT_USERNAME")
        password = os.environ.get("DATASET_MANAGEMENT_PASSWORD")
        if url is None or username is None or password is None:
            print("Missing required environment variables: DATASET_MANAGEMENT_RETRAIN_URL, DATASET_MANAGEMENT_USERNAME, DATASET_MANAGEMENT_PASSWORD")
            return
        authorization = base64.b64encode("{}:{}".format(username, password).encode()).decode()
        data = {"dataset":self.datasetname, "version":self.version}
        if metadata_filter:
            data["metadata_filter"] = metadata_filter
        if models is not None and isinstance(models, list):
            data["models"] = models
        t = ApiTrigger("POST", url, data, authorization)
        return t.execute()

    def get_tags(self):
        return self.metadata["tags"].string_value

    def add_tag(self, tag):
        tag_str = self.metadata["tags"].string_value
        if tag_str is None or tag_str == '':
            tag_arr = [tag]
        else:
            tag_arr = tag_str.split(",")
            if tag not in tag_arr:
                tag_arr.append(tag)
            else:
                print("Tag existed")
                return False
        tag_str = ",".join(tag_arr)
        self.metadata["tags"].string_value = tag_str
        return update_artifact(ArtifactType.DATASET, self.datasetname, None, None, None, None, tag_str)

    def set_tags(self, tags: Array):
        tags_str = ",".join(tags)
        self.metadata["tags"].string_value = tags_str
        return update_artifact(ArtifactType.DATASET, self.datasetname, None, None, None, None, tags_str)

    def get_connected_models(self):
        return get_model_info_by_dataset(self.datasetname)

    def __collect_changelist(self, version, global_changelist, metadata_filter=None):
        ctx = get_context(ContextType.COMMIT_DATASET_VERSION, version)
        if ctx is None:
            raise Exception("Version {} not exists in this dataset".format(self.version))

        image_log_arr = get_image_executions_by_version(version, metadata_filter)
        for item in image_log_arr:
            if global_changelist.get(item.get("image_name")) is None:
                global_changelist[item.get("image_name")] = [item.get("execution_id")]
            else:
                global_changelist[item.get("image_name")].append(item.get("execution_id"))

        prev_version = ctx.properties["prev_ref"].string_value
        if prev_version is not None and prev_version != '':
            return self.__collect_changelist(prev_version, global_changelist)
        return global_changelist

    def get_filelist(self, metadata_filter=None):
        if self.version is None or self.version == "":
            return None
        addtype = get_execution_type_by_name(ExecutionType.ADD_FILES_TO_DATASET)
        filelist = []
        global_changelist = self.__collect_changelist(self.version, {}, metadata_filter)
        for key,value in global_changelist.items():
            if value[0] == addtype.id:
                filelist.append(key)
        return filelist

    def get_current_version(self):
        return self.version

    def checkout(self, version, metadata_filter=None):
        if version == "latest":
            version = self.metadata["latest_version"].string_value
        if version not in self.list_versions(short=True):
            raise Exception("Version is not valid")
        self.version = version
        self.filelist = self.get_filelist(metadata_filter)

    def download_to_dir(self, _dir, overriding=False):
        if not os.path.exists(_dir):
            os.makedirs(_dir)
        if self.filelist is None:
            self.filelist = self.get_filelist()
        if self.filelist is None or len(self.filelist) == 0:
            print("Nothing to download")
            return False

        existing_files = os.listdir(_dir)
        arglist = []
        for _f in self.filelist:
            if not overriding and _f in existing_files:
                print("Skipping existing file {}".format(_f))
            else:
                arglist.append((_f, self.datasetname, _dir))

        proc_count = cpu_count()
        if len(arglist) < cpu_count():
            proc_count = len(arglist)
        print("Downloading {} files by {} processes...".format(len(self.filelist), proc_count))
        p = Pool(proc_count)
        r = p.map(_download_blob, arglist)
        p.close()
        p.join()
        success_list = []
        for i,_ in enumerate(r):
            if r[i] == False:
                print("Failed to download {}".format(self.changelist[i][0]))
            else:
                success_list.append(r[i])
        print("{}/{} files downloaded".format(len(success_list), len(self.filelist)))

    def load_filelist(splitter=None):
        """
        Load the images specified in self.filelist to memory variables. A logic of how to split can be defined by input splitter
        """
        print("Not yet implemented")
        pass

    def update_filelist_metadata():
        """
        Update metadata of images specified in self.filelist
        """
        print("Not yet implemented")
        pass

    def get_annotation_stats(self):
        """
        Return all annotations of the images of the current version

        """
        return get_annotation_stats(self.id)

    def get_training_history(self):
        return get_training_history(self.datasetname)
