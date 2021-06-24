import os
import json
import base64
import boto3
import botocore


class ApiKeyNotDefinied(Exception):
    pass


class Not200Error(Exception):
    pass


class ParameterError(Exception):
    pass


class SigmindTools():

    def __init__(self):
        config = botocore.config.Config(
            read_timeout=9000,
            connect_timeout=9000,
            retries={"max_attempts": 0}
        )
        self.client = boto3.client(
            'lambda', region_name='us-east-1', config=config)

    def _call(self, entry, jdata):
        res = self.client.invoke(FunctionName=entry,
                                 InvocationType='RequestResponse',
                                 Payload=json.dumps(jdata).encode('utf-8'))

        if res['ResponseMetadata']['HTTPStatusCode'] == 200:
            res_content = res['Payload'].read()
            res_content_parsed = json.loads(res_content.decode('utf-8'))
            if 'body' in res_content_parsed:
                return res_content_parsed['body']
            else:
                raise Exception(res_content_parsed)

        else:
            raise Not200Error(str(res.status_code) +
                              res.content.decode('utf-8'))

    def _parse_arguments(self, **kargv):
        args_s3 = set(['bucket', 'key'])
        args_file = set(['fn'])
        args_url = set(['url'])

        args_received = set(kargv.keys())

        if args_received == args_s3:
            key = kargv['key']
            bucket = kargv['bucket']
            jdata = {'type': 's3', 'name': key, 'bucket': bucket}
        elif args_received == args_file:
            fn = kargv['fn']
            file = base64.b64encode(open(fn, 'rb').read()).decode('utf-8')
            jdata = {'type': 'file', 'file': file}

        elif args_received == args_url:
            url = kargv['url']
            jdata = {'type': 'url', 'url': url}

        else:
            raise ParameterError

        return jdata

    def _generic_call_audio_file(self, entry, **kargv):
        jdata = self._parse_arguments(**kargv)
        res = self._call(entry, jdata)
        return json.loads(res)

    def speech_to_text(self, **kargv):
        """
        Returns the output of the function use the Google speech-2-text api.
        Supports 3 types of parameters, each method is exclusive

            Parameters for public url audio method:
                - url: An public url with a audio

            Parameters for S3 audio method:
                - bucket (string): the name of the bucket
                - key (string): object key

            Parameters for file method:
                - fn (string): local file name 
        """
        return self._generic_call_audio_file('sigmind_lab__speech-2-text', **kargv)

    def speech_intervals(self, **kargv):
        return self._generic_call_audio_file('sigmind_lab__compute-talking-intervals', **kargv)

    def pitch_analysis(self, **kargv):
        return self._generic_call_audio_file('sigmind_lab__pitch-analysis', **kargv)

    def sentiment_analysis(self, text):
        entry = 'sigmind_lab__sentiment-google'
        jdata = {'text': text}
        res = self._call(entry, jdata)
        return json.loads(res)

    def text_indexes(self, text):
        entry = 'sigmind_lab__text-indexes'
        jdata = {'text': text}
        res = self._call(entry, jdata)
        return json.loads(res)
