import logging  
import os
from typing import Type
import json
import pandas as pd
import uuid
from pandas.core.frame import DataFrame
import pyodbc
from batch import plus_batch
from helper import plus_helper


#incoming Event (filename/url)

#class Batch (input= source_filename/url, 
#                  store: batchid, start_datetime, end_datetime, Source_filename, businessobjecttype, filetype, source_path, number_of_records, number_of_files, state
#                   generate: BatchId)
    #Generate BatchId
    #check if filename is correct and file exists
    #check if file was already handled
    #report (send message to queue BatchSummary)

#class SubBatch (input = batchid,
#                   store: subbatchid, start_datetime, end_datetime, target_filename, target_folder, 
#                           target_container, number_of_records, state
#                   generate: subbatchid, destination filename (input is filter in file and objecttype) and path,  )
    #Generate Subbatchid
    #Generate target filename and path
    #Report (Query now, API later)
    
class PlusSubbatch():
    def __init__(self):        
        self.destination_filetype=None
        self.number_of_records=0
        self.number_of_records_in_table = 0
        self.database_schema=''
        self.database_table=''
        self.create_datetime=plus_helper.getcurrent_datetime()
        self.message_version=''

    def init_onramp(self, batch):
        if not isinstance(batch, plus_batch.PlusBatch):
            logging.info(f'Passed {type(batch)}, expecting object of Batch-type')
        self.cds_batchid=batch.cds_batchid
        self.source_filename=batch.source_filename
        self.source_folder=batch.source_folder
        self.business_object_type=batch.business_object_type

        self.destination_account=''
        self.destination_container=''
        self.destination_folder=''        

        self.batch=batch

        self.state = 'Init'       

        self.set_subbatchid()

    def set_subbatchid(self, subbatch=''):
        if subbatch=='':
            self.cds_subbatchid = str(uuid.uuid4())
        else:
            self.cds_subbatchid = subbatch

    def set_target_filetype(self, dest_filetype='json'):
        if isinstance(dest_filetype, str):
            self.destination_filetype=dest_filetype
        else:
            raise TypeError(f'Expected str-input for dest_filetype variable.')

    def get_filename(self, split_attributes='', split_values=''):
        if split_attributes == '' or split_values == '':
            split_zip = ''
        elif isinstance(split_attributes, (str, tuple, list)) and isinstance(split_values, (str, tuple, list)):
            split_attr_new = [item.lower() for item in split_attributes]
            split_zip = zip(split_attr_new, split_values)
        else:
            logging.info('Expected empty values or values of type string, tuple or list for "split_attributes" and "split_values" variables.')
            return False
        
        split_zip_new=''
        for item in split_zip:
            split_zip_new+="_" + "_".join(item)

        #we expect the source filename to be formatted like this:
        # YYYY_{period_letter(P(eriode),W(eek),M(aand))}{PeriodeNumber(XX)}_{BusinessObject}.{filetype}
        #ie. 2021_W20_dvo-omzet.xlsx
        if not self.destination_filetype:
            self.set_target_filetype()

        self.year = self.source_filename.split('_')[0]
        self.period = self.source_filename.split('_')[1]
        self.destination_folder=f'{self.year}/{self.period}'
        self.destination_filename = f'{self.destination_folder}/{self.year}_{self.period}{split_zip_new}_{self.business_object_type}_{self.cds_subbatchid}.{self.destination_filetype}'

        return self.destination_filename
        
    def send_batchfiles_report(self, destination_type, action):
        #destination_type valid entries: msg_queue, direct_sql
        if destination_type == 'msg_queue':
            pass
        elif destination_type == 'direct_sql':
            if action == 'insert':
                sql = f"""INSERT INTO [dbo].[BatchFiles]
                        ([BatchId]
                        ,[BatchCreateDate]
                        ,[Filename]
                        ,[NumberOfRecords]
                        ,[State]
                        ,[NumberOfRecordsInTable]
                        ,[BatchEndDate]
                        ,[SubBatchId]
                        ,[Accountname]
                        ,[Containername]
                        ,[Foldername])
                        VALUES
                        (
                        '{self.batch.cds_batchid}'
                        ,'{self.create_datetime}'
                        ,'{self.destination_filename}'
                        ,{self.number_of_records}
                        ,'{self.state}'
                        ,0
                        ,NULL
                        ,'{self.cds_subbatchid}'
                        ,'{self.destination_account}'
                        ,'{self.destination_container}'
                        ,'{self.destination_folder}'
                        )"""
                return self.batch.database.execute_insert_query(sql)
            elif action == 'update':
                
                sql = f"""UPDATE [dbo].[BatchFiles]
SET [NumberOfRecords] = {self.number_of_records}
,[State] = '{self.state}'
,[NumberOfRecordsInTable] = {self.number_of_records_in_table}
,[BatchEndDate] = {f'{self.batch.database.null_value}' if self.state not in ('Done', 'Error') else f"'{plus_helper.getcurrent_datetime()}'"}
WHERE SubBatchId = '{self.cds_subbatchid}'"""
                return self.batch.database.execute_insert_query(sql)

    def _get_onramp_msg_header(self):
        onramp_msg_header = {
                "messageType": self.batch.business_object_type,
                "creationDateTime": self.create_datetime,
                "Filename" : self.destination_filename,
                "Foldername" : self.destination_folder,
                "numberOfRecords" : self.number_of_records,
                "CDS_BatchId" : self.batch.cds_batchid, 
                "CDS_SubBatchId" : self.cds_subbatchid,
                "RapportageJaar" : self.year,
                "Rapportageperiode" : self.period[1:],
                "MessageVersion": self.message_version,
                "payload": []
            }
        return onramp_msg_header

    def _create_msg(self, df):
        self.msg = self._get_onramp_msg_header()

        records = json.loads(DataFrame(df).to_json(orient='records', date_format='iso'))
   
        for r in records:
            r['CDS_BatchId'] = self.batch.cds_batchid 
            r['CDS_SubBatchId'] = self.cds_subbatchid
            r['RapportageJaar'] = self.year
            r['Rapportageperiode'] = self.period[1:]
            record = {"record": r}
            
            payload = self.msg['payload']
            payload.append(record)
    
    def get_msg_with_data(self, df):
        if not isinstance(df, DataFrame):
            raise TypeError(f"Provided data in variable df is not a DataFrame. Can't process data.")
        
        self.number_of_records=df.shape[0]
        self.batch.number_of_records+= self.number_of_records
        self._create_msg(df=df)

        return self.msg
        
    def get_cds_notification_msg(self, action):
        self.notification_msg={
            "notification": {
                "MessageType": "cds-notificatie",
                "CDS_BatchId": self.cds_batchid,
                "CDS_SubBatchId": self.cds_subbatchid,
                "CreationDateTime": plus_helper.getcurrent_datetime(),
                "Accountname": self.destination_account,
                "Containername": self.destination_container,
                "Foldername": self.destination_folder,
                "Filename": self.destination_filename,
                "NumberOfRecords": self.number_of_records,
                "EtlRunStatus": self.state,
                "MessageVersion": self.message_version,
                "Action": action}
        }
        return json.dumps(self.notification_msg)

    def file_was_processed(self, blob):
        #a blob is expected to be a combination of folder and filename joined by a "/" ie. "2021/20/2021_P20_oos.xlsx"
        #the folder is optional.
        sql = f"SELECT COUNT(filename) as qty FROM BatchFiles WHERE filename = '{blob}' AND State IN ('Done')"
        result = self.batch.database.execute_select_query(sql)

        if result:
            if result[0] > 0:
                return True
            else:
                return False
        else:
            logging.info('Something went wrong when checking if the file was processed, see previous error messages.')
    
    def get_batchfiles_info(self):
        if self.cds_subbatchid=='':
            raise ValueError('Cds_subbatchid not set, exiting process...')
        else:
            sql = f"""SELECT [Id]
      ,[BatchId]
      ,[BatchCreateDate]
      ,[NumberOfRecords]
      ,[State]
      ,[NumberOfRecordsInTable]
      ,[BatchEndDate]
      ,[Accountname]
      ,[Containername]
      ,[Foldername]
      ,[Filename]
  FROM [dbo].[BatchFiles]
  WHERE SubBatchId = '{self.cds_subbatchid}' 
  AND state = 'ReadyForPickup'"""
            result = self.batch.database.execute_select_query(sql)

            if not result:
                logging.info(f"No result returned from select query, can't continue...")
            else:
                logging.info('Setting some variables in de subbatch...')
                self.number_of_records = result[3]
                self.destination_account = result[7]
                self.destination_container = result[8]
                self.destination_folder = result[9]
                self.destination_filename = result[10]
            