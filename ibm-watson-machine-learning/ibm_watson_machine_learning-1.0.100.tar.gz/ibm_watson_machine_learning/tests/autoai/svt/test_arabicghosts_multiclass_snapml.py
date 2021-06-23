import unittest
from sklearn.metrics import roc_auc_score

from sklearn.linear_model import LogisticRegression as LR
from sklearn.tree import DecisionTreeClassifier as Tree
from sklearn.neighbors import KNeighborsClassifier as KNN

# from lale.lib.lale import Hyperopt
from lale import wrap_imported_operators

from pprint import pprint
import pandas as pd
from os import environ
import traceback

from ibm_watson_machine_learning import APIClient

from ibm_watson_machine_learning.experiment import AutoAI
from ibm_watson_machine_learning.deployment import WebService, Batch
from ibm_watson_machine_learning.workspace import WorkSpace

from ibm_watson_machine_learning.helpers.connections import S3Connection, S3Location, DataConnection, FSLocation, \
    DeploymentOutputAssetLocation

from ibm_watson_machine_learning.tests.utils.utils import (get_wml_credentials, get_cos_credentials, bucket_exists,
                                                           create_bucket, get_space_id, is_cp4d)
from ibm_watson_machine_learning.tests.utils.cleanup import space_cleanup
from ibm_watson_machine_learning.utils.autoai.enums import ClassificationAlgorithms

from ibm_watson_machine_learning.utils.autoai.errors import InvalidSequenceValue

from ibm_watson_machine_learning.helpers import pipeline_to_script


class TestAutoAIRemote(unittest.TestCase):
    """
    The test covers:
    - AutoAI experiment with SNAP ML estimators
    - lale pretty print check
    """
    wml_client: 'APIClient' = None
    experiment: 'AutoAI' = None
    remote_auto_pipelines = None
    hyperopt_pipelines = None
    prefix = None
    new_pipeline = None
    wml_credentials = None
    cos_credentials = None
    pipeline_opt = None
    service: 'WebService' = None
    service_batch: 'Batch' = None
    lale_pipeline = None

    data_location = './autoai/data/arabicghosts_train.csv'
    target_column = 'لون'

    trained_pipeline_details = None
    run_id = None

    data_connection = None
    results_connection = None

    train_data = None

    cos_endpoint = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
    if "BUCKET_NAME" in environ:
        bucket_name = environ['BUCKET_NAME']
    else:
        bucket_name = "wml-autoaitests-qa"

    pod_version = environ.get('KB_VERSION', None)

    data_cos_path = 'data/arabicghosts_train.csv'
    cos_resource_instance_id = None

    results_cos_path = 'results_wml_autoai'

    batch_cos_filename = "batch_payload_arabicghosts.csv"

    best_pipeline: 'Pipeline' = None
    deployed_pipeline = None

    OPTIMIZER_NAME = 'arabicghosts_train binary as sample notebook test'
    DEPLOYMENT_NAME = "arabicghosts_train AutoAI test Deployment "

    space_name = 'autoai_tests_sdk_space'

    space_id = None
    project_id = None

    asset_id = None

    @classmethod
    def setUpClass(cls) -> None:
        """
        Load WML credentials from config.ini file based on ENV variable.
        """
        cls.data = pd.read_csv(cls.data_location)
        cls.X = cls.data.drop([cls.target_column], axis=1)
        cls.y = cls.data[cls.target_column]

        wrap_imported_operators()

        cls.wml_credentials = get_wml_credentials()
        cls.wml_client = APIClient(wml_credentials=cls.wml_credentials)
        if not cls.wml_client.ICP:
            cls.cos_credentials = get_cos_credentials()
            cls.cos_endpoint = cls.cos_credentials.get('endpoint_url')
            cls.cos_resource_instance_id = cls.cos_credentials.get('resource_instance_id')

        cls.project_id = cls.wml_credentials.get('project_id')

    def test_00a_space_cleanup(self):
        space_cleanup(self.wml_client,
                      get_space_id(self.wml_client, self.space_name,
                                   cos_resource_instance_id=self.cos_resource_instance_id),
                      days_old=7)
        TestAutoAIRemote.space_id = get_space_id(self.wml_client, self.space_name,
                                                 cos_resource_instance_id=self.cos_resource_instance_id)

        if self.wml_client.ICP:
            self.wml_client.set.default_project(self.project_id)
        else:
            self.wml_client.set.default_space(self.space_id)

    def test_00b_prepare_COS_instance(self):
        if self.wml_client.ICP or self.wml_client.WSD:
            self.skipTest("Prepare COS is available only for Cloud")

        import ibm_boto3
        cos_resource = ibm_boto3.resource(
            service_name="s3",
            endpoint_url=self.cos_endpoint,
            aws_access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
            aws_secret_access_key=self.cos_credentials['cos_hmac_keys']['secret_access_key']
        )
        # Prepare bucket
        if not bucket_exists(cos_resource, self.bucket_name):
            TestAutoAIRemote.bucket_name = create_bucket(cos_resource, self.bucket_name)

            self.assertIsNotNone(TestAutoAIRemote.bucket_name)
            self.assertTrue(bucket_exists(cos_resource, TestAutoAIRemote.bucket_name))

        print(f"Using COS bucket: {TestAutoAIRemote.bucket_name}")

    def test_01_initialize_AutoAI_experiment__pass_credentials__object_initialized(self):
        TestAutoAIRemote.experiment = AutoAI(wml_credentials=self.wml_credentials.copy(),
                                             project_id=self.project_id)

        self.assertIsInstance(self.experiment, AutoAI, msg="Experiment is not of type AutoAI.")

    def test_02_save_remote_data_and_DataConnection_setup(self):
        if self.wml_client.ICP:
            TestAutoAIRemote.data_connection = DataConnection(
                location=FSLocation(path=self.data_location))
            TestAutoAIRemote.results_connection = None

        else:  # for cloud and COS
            connection_details = self.wml_client.connections.create({
                'datasource_type': 'bluemixcloudobjectstorage',
                'name': 'Connection to COS for tests',
                'properties': {
                    'bucket': self.bucket_name,
                    'access_key': self.cos_credentials['cos_hmac_keys']['access_key_id'],
                    'secret_key': self.cos_credentials['cos_hmac_keys']['secret_access_key'],
                    # 'iam_url': self.cos_credentials['iam_url'],
                    'url': self.cos_endpoint
                }
            })
            TestAutoAIRemote.data_connection = DataConnection(
                connection=S3Connection(endpoint_url=self.cos_endpoint,
                                        access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
                                        secret_access_key=self.cos_credentials['cos_hmac_keys']['secret_access_key']),
                location=S3Location(bucket=self.bucket_name,
                                    path=self.data_cos_path)
            )
            TestAutoAIRemote.results_connection = DataConnection(
                connection=S3Connection(endpoint_url=self.cos_endpoint,
                                        access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
                                        secret_access_key=self.cos_credentials['cos_hmac_keys']['secret_access_key']),
                location=S3Location(bucket=self.bucket_name,
                                    path=self.results_cos_path)
            )
            TestAutoAIRemote.data_connection.write(data=self.data, remote_name=self.data_cos_path)

        self.assertIsNotNone(obj=TestAutoAIRemote.data_connection)

    def test_03_initialize_optimizer(self):
        from ibm_watson_machine_learning.experiment.autoai.optimizers import RemoteAutoPipelines

        if self.wml_client.ICP:
            with self.assertRaises(AttributeError):
                TestAutoAIRemote.remote_auto_pipelines = self.experiment.optimizer(
                    name=self.OPTIMIZER_NAME,
                    prediction_type=AutoAI.PredictionType.MULTICLASS,
                    prediction_column=self.target_column,
                    include_only_estimators=[self.experiment.ClassificationAlgorithms.SnapRF,
                                             self.experiment.ClassificationAlgorithms.SnapDT,
                                             self.experiment.ClassificationAlgorithms.SnapSVM]
                )

            with self.assertRaises(InvalidSequenceValue):
                TestAutoAIRemote.remote_auto_pipelines = self.experiment.optimizer(
                    name=self.OPTIMIZER_NAME,
                    prediction_type=AutoAI.PredictionType.MULTICLASS,
                    prediction_column=self.target_column,
                    include_only_estimators=[ClassificationAlgorithms.SnapRF,
                                             ClassificationAlgorithms.SnapDT,
                                             ClassificationAlgorithms.SnapSVM],
                    max_number_of_estimators=3
                )
            self.assertIsNone(self.remote_auto_pipelines, msg="experiment.optimizer was initialized with snap on CPD")
        else:
            TestAutoAIRemote.remote_auto_pipelines = self.experiment.optimizer(
                name=self.OPTIMIZER_NAME,
                prediction_type=AutoAI.PredictionType.MULTICLASS,
                prediction_column=self.target_column,
                scoring=AutoAI.Metrics.ACCURACY_SCORE,
                include_only_estimators=[self.experiment.ClassificationAlgorithms.SnapDT,
                                         self.experiment.ClassificationAlgorithms.SnapRF,
                                         self.experiment.ClassificationAlgorithms.SnapSVM,
                                         self.experiment.ClassificationAlgorithms.SnapLR],
                max_number_of_estimators=3,
                autoai_pod_version=self.pod_version
            )

            self.assertIsInstance(self.remote_auto_pipelines, RemoteAutoPipelines,
                                  msg="experiment.optimizer did not return RemoteAutoPipelines object")

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_04_get_configuration_parameters_of_remote_auto_pipeline(self):
        parameters = self.remote_auto_pipelines.get_params()
        # print(parameters)
        self.assertIsInstance(parameters, dict, msg='Config parameters are not a dictionary instance.')

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_05_fit_run_training_of_auto_ai_in_wml(self):
        TestAutoAIRemote.trained_pipeline_details = self.remote_auto_pipelines.fit(
            training_data_reference=[self.data_connection],
            training_results_reference=self.results_connection,
            background_mode=False)

        TestAutoAIRemote.run_id = self.trained_pipeline_details['metadata']['id']

        # TestAutoAIRemote.run_id = ''
        # TestAutoAIRemote.remote_auto_pipelines = self.experiment.runs.get_optimizer(TestAutoAIRemote.run_id)
        #
        # TestAutoAIRemote.data_connection = self.remote_auto_pipelines.get_data_connections()

        self.assertIsNotNone(self.data_connection.auto_pipeline_params,
                             msg='DataConnection auto_pipeline_params was not updated.')
        TestAutoAIRemote.train_data = self.remote_auto_pipelines.get_data_connections()[0].read()

        print("train data sample:")
        print(self.train_data.head())
        self.assertGreater(len(self.train_data), 0)

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_06_get_run_status(self):
        status = self.remote_auto_pipelines.get_run_status()
        self.assertEqual(status, "completed", msg="AutoAI run didn't finished successfully. Status: {}".format(status))

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_07_get_run_details(self):
        parameters = self.remote_auto_pipelines.get_run_details()
        print(parameters)
        self.assertIsNotNone(parameters)

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_08_summary_listing_all_pipelines_from_wml(self):
        pipelines_details = self.remote_auto_pipelines.summary()
        print(pipelines_details)

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_09_get_pipeline__load_lale_pipeline__pipeline_loaded(self):
        from lale.operators import TrainablePipeline

        TestAutoAIRemote.best_pipeline = self.remote_auto_pipelines.get_pipeline(pipeline_name="Pipeline_8",
                                                                                 persist=True)
        print(f"Fetched pipeline type: {type(self.best_pipeline)}")

        self.assertIsInstance(self.best_pipeline, TrainablePipeline,
                              msg="Fetched pipeline is not of TrainablePipeline instance.")
        predictions = self.best_pipeline.predict(
            X=self.train_data.drop([self.target_column], axis=1).values[:5])
        print(predictions)

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_10__pipeline_to_script__lale__pretty_print(self):
        pipeline_to_script(self.best_pipeline)
        pipeline_code = self.best_pipeline.pretty_print()
        exception = None
        try:
            exec(pipeline_code)

        except Exception as exception:
            self.assertIsNone(exception, msg="Pretty print from lale pipeline was not successful")

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_11__predict__do_the_predict_on_lale_pipeline__results_computed(self):
        y_true = self.train_data[self.target_column].values[:10]
        predictions = self.best_pipeline.predict(self.train_data.drop([self.target_column], axis=1).values[:10])
        print(predictions)

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_12__remove_last_freeze_trainable__prefix_returned(self):
        from lale.operators import TrainablePipeline

        TestAutoAIRemote.prefix = self.best_pipeline.remove_last().freeze_trainable()
        self.assertIsInstance(TestAutoAIRemote.prefix, TrainablePipeline,
                              msg="Prefix pipeline is not of TrainablePipeline instance.")

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_13_add_estimator(self):
        TestAutoAIRemote.new_pipeline = TestAutoAIRemote.prefix >> (LR | Tree | KNN)

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_14_hyperopt_fit_new_pipepiline(self):
        from lale.lib.lale import Hyperopt
        train_X = self.train_data.drop([self.target_column], axis=1).values
        train_y = self.train_data[self.target_column].values

        hyperopt = Hyperopt(estimator=TestAutoAIRemote.new_pipeline, cv=3, max_evals=5)
        TestAutoAIRemote.hyperopt_pipelines = hyperopt.fit(train_X, train_y)

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_15_get_pipeline_from_hyperopt(self):
        from sklearn.pipeline import Pipeline
        new_pipeline_model = TestAutoAIRemote.hyperopt_pipelines.get_pipeline()
        print(f"Hyperopt_pipeline_model is type: {type(new_pipeline_model)}")
        TestAutoAIRemote.new_pipeline = new_pipeline_model.export_to_sklearn_pipeline()
        self.assertIsInstance(TestAutoAIRemote.new_pipeline, Pipeline,
                              msg=f"Incorect Sklearn Pipeline type after conversion. Current: {type(TestAutoAIRemote.new_pipeline)}")

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_16__predict__do_the_predict_on_sklearn_pipeline__results_computed(self):
        y_true = self.train_data[self.target_column].values[:10]
        predictions = TestAutoAIRemote.new_pipeline.predict(
            self.train_data.drop([self.target_column], axis=1).values[:10])
        print(predictions)

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_17_get_all_pipelines_as_lale(self):
        from lale.operators import TrainablePipeline
        summary = self.remote_auto_pipelines.summary()
        print(summary)
        failed_pipelines_loading = []
        failed_pipelines_pretty_print = []
        for pipeline_name in summary.reset_index()['Pipeline Name']:
            print(f"Getting pipeline: {pipeline_name}")
            lale_pipeline = None
            try:
                lale_pipeline = self.remote_auto_pipelines.get_pipeline(pipeline_name=pipeline_name)
                self.assertIsInstance(lale_pipeline, TrainablePipeline)
                predictions = lale_pipeline.predict(
                    X=self.train_data.values[:1])
                print(predictions)
                self.assertGreater(len(predictions), 0, msg=f"Returned prediction for {pipeline_name} are empty")
            except:
                print(f"Failure: {pipeline_name}")
                failed_pipelines_loading.append(pipeline_name)
                traceback.print_exc()

            # check lale pretty print code for every pipeline
            try:
                if not lale_pipeline:
                    lale_pipeline = self.remote_auto_pipelines.get_pipeline(pipeline_name=pipeline_name)

                self.assertIsInstance(lale_pipeline, TrainablePipeline)

                pipeline_to_script(lale_pipeline)
                pipeline_code = lale_pipeline.pretty_print()
                exception = None
                try:
                    exec(pipeline_code)

                except Exception as exception:
                    if exception is not None:
                        # import joblib
                        # with open(f"{pipeline_name}.pickle", 'wb') as f:
                        #     joblib.dump(lale_pipeline, f)
                        failed_pipelines_pretty_print.append(pipeline_name)
                        print(f"Pretty print from lale pipeline was not successful for {pipeline_name}")
                        traceback.print_exc()
                        print(exception)
                        print("\n\n pipeline code:\n\n")
                        print(pipeline_code)
            except:
                print(f"Failure: {pipeline_name}")
                traceback.print_exc()

            if not TestAutoAIRemote.lale_pipeline:
                TestAutoAIRemote.lale_pipeline = lale_pipeline
                print(f"{pipeline_name} loaded for next test cases")

        self.assertEqual(len(failed_pipelines_loading), 0,
                         msg=f"Some pipelines failed. Full list: {failed_pipelines_loading}")
        self.assertEqual(len(failed_pipelines_pretty_print), 0,
                         msg=f"Some pipeline codes failed. Full list: {failed_pipelines_pretty_print}")

    #################################
    #      DEPLOYMENT SECTION       #
    #################################

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_21_deployment_setup_and_preparation(self):
        TestAutoAIRemote.service = WebService(source_wml_credentials=self.wml_credentials.copy(),
                                              source_project_id=self.project_id,
                                              target_wml_credentials=self.wml_credentials,
                                              target_space_id=self.space_id)
        self.wml_client.set.default_space(self.space_id)
        self.assertIsNone(self.service.name)
        self.assertIsNone(self.service.id)
        self.assertIsNone(self.service.scoring_url)

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_22__deploy__deploy_best_computed_pipeline_from_autoai_on_wml(self):
        self.service.create(
            experiment_run_id=self.run_id,
            model="Pipeline_3",
            deployment_name=self.DEPLOYMENT_NAME)

        self.assertIsNotNone(self.service.name)
        self.assertIsNotNone(self.service.id)
        self.assertIsNotNone(self.service.asset_id)

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_24_score_deployed_model(self):
        nb_records = 10
        predictions = self.service.score(payload=self.train_data.drop([self.target_column], axis=1)[:nb_records])
        print(predictions)
        self.assertIsNotNone(predictions)
        self.assertEqual(len(predictions['predictions'][0]['values']), nb_records)

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_25_delete_deployment(self):
        print("Delete current deployment: {}".format(self.service.deployment_id))
        self.service.delete()
        self.wml_client.set.default_space(self.space_id) if not self.wml_client.default_space_id else None
        self.wml_client.repository.delete(self.service.asset_id)
        self.wml_client.set.default_project(self.project_id) if is_cp4d() else None

        #########################
        #  Batch deployment
        #########################

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_30_batch_deployment_setup_and_preparation(self):
        TestAutoAIRemote.service_batch = Batch(source_wml_credentials=self.wml_credentials.copy(),
                                               source_project_id=self.project_id,
                                               target_wml_credentials=self.wml_credentials,
                                               target_space_id=self.space_id)

        self.assertIsInstance(self.service_batch, Batch, msg="Deployment is not of Batch type.")
        self.assertIsInstance(self.service_batch._source_workspace, WorkSpace, msg="Workspace set incorrectly.")
        self.assertEqual(self.service_batch.id, None, msg="Deployment ID initialized incorrectly")
        self.assertEqual(self.service_batch.name, None, msg="Deployment name initialized incorrectly")

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_32__deploy__batch_deploy_pipeline_from_autoai_on_wml(self):
        self.service_batch.create(
            experiment_run_id=self.run_id,
            model="Pipeline_1",
            deployment_name=self.DEPLOYMENT_NAME + ' BATCH')

        self.assertIsNotNone(self.service_batch.id, msg="Batch Deployment creation - missing id")
        self.assertIsNotNone(self.service_batch.name, msg="Batch Deployment creation - name not set")
        self.assertIsNotNone(self.service_batch.asset_id,
                             msg="Batch Deployment creation - model (asset) id missing, incorrect model storing")

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_33a_run_job_batch_deployed_model_with_data_connection_data_asset(self):
        self.wml_client.set.default_space(self.space_id) if self.wml_client.ICP else None
        asset_details = self.wml_client.data_assets.create(
            name=self.data_location.split('/')[-1],
            file_path=self.data_location)
        asset_id = asset_details['metadata']['guid']
        asset_href = self.wml_client.data_assets.get_href(asset_details)

        payload_reference = DataConnection(data_asset_id=asset_id)
        results_reference = DataConnection(
            location=DeploymentOutputAssetLocation(name="batch_output.csv"))

        scoring_params = self.service_batch.run_job(
            payload=[payload_reference],
            output_data_reference=results_reference,
            background_mode=False)

        self.wml_client.set.default_project(self.project_id) if self.wml_client.ICP else None

        print(scoring_params)
        self.assertIsNotNone(scoring_params)
        self.wml_client.data_assets.list()

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_33b_run_job_batch_deployed_model_with_data_connection_s3(self):
        if self.wml_client.ICP or self.wml_client.WSD:
            self.skipTest("Batch Deployment with s3 data connection is available only for Cloud")
        else:
            payload_reference = DataConnection(
                connection=S3Connection(endpoint_url=self.cos_endpoint,
                                        access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
                                        secret_access_key=self.cos_credentials['cos_hmac_keys']['secret_access_key']),
                location=S3Location(bucket=self.bucket_name,
                                    path=self.batch_cos_filename)
            )
            results_reference = DataConnection(
                connection=S3Connection(endpoint_url=self.cos_endpoint,
                                        access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
                                        secret_access_key=self.cos_credentials['cos_hmac_keys']['secret_access_key']),
                location=S3Location(bucket=self.bucket_name,
                                    path='batch_output_car-price.csv')
            )
            payload_reference.write(data=self.X,
                                    remote_name=self.batch_cos_filename)

        scoring_params = self.service_batch.run_job(
            payload=[payload_reference],
            output_data_reference=results_reference,
            background_mode=False)
        print(scoring_params)
        self.assertIsNotNone(scoring_params)
        self.wml_client.data_assets.list()

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_34_list_batch_deployments(self):
        deployments = self.service_batch.list()
        print(deployments)
        params = self.service_batch.get_params()
        print(params)
        self.assertIsNotNone(params)

    @unittest.skipIf(is_cp4d(), "SnapML is not supported on CPD")
    def test_35_delete_deployment_batch(self):
        print("Delete current deployment: {}".format(self.service_batch.deployment_id))
        self.service_batch.delete()
        self.wml_client.set.default_space(self.space_id) if not self.wml_client.default_space_id else None
        self.wml_client.repository.delete(self.service_batch.asset_id)
        self.wml_client.set.default_project(self.project_id) if is_cp4d() else None
        self.assertEqual(self.service_batch.id, None, msg="Deployment ID deleted incorrectly")
        self.assertEqual(self.service_batch.name, None, msg="Deployment name deleted incorrectly")
        self.assertEqual(self.service_batch.scoring_url, None,
                         msg="Deployment scoring_url deleted incorrectly")


if __name__ == '__main__':
    unittest.main()
