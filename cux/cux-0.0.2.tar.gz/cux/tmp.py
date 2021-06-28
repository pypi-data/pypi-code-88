#!/usr/bin/env python
import codefast as cf

red = cf.format.red
green = cf.format.green


class ASRJsonParser:
    def __init__(self,
                 file_name: str,
                 speaker_one: str = 'User',
                 speaker_two: str = 'User'):
        self.js = jsn.read(file_name)
        self.left = speaker_one
        self.right = speaker_two

    @property
    def _channel_number(self):
        return len(self.js['flash_result'])

    def _merge_continual(self, lst: list) -> list:
        ''' Merge time continual fractions of ASR result'''
        ans = []
        for x in lst:
            if ans and ans[-1]['end_time'] == x['start_time']:
                ans[-1]['text'] = ans[-1]['text'].rstrip('。').rstrip(
                    '？') + x['text']
                ans[-1]['end_time'] = x['end_time']
            else:
                ans.append(x)
        return ans

    def parse_result(self):
        if self._channel_number == 1:
            for s in self.js['flash_result'][0]['sentence_list']:
                sid = green(self.left) if s['speaker_id'] == 1 else red(
                    self.right)
                print(sid, s['text'], sep=': ')

        else:
            res = []
            for i, lst in enumerate(self.js['flash_result']):
                x = lst['sentence_list']
                for e in x:
                    e['speaker_id'] = i
                res += self._merge_continual(x)

            res.sort(key=lambda e: e['start_time'])
            for x in res:
                sid = green(self.left) if x['speaker_id'] == 1 else red(
                    self.right)
                print(sid, x['text'], sep=': ')


if __name__ == '__main__':
    ajp = ASRJsonParser('/tmp/flash_asr.json', '客户', '销售')
    ajp.parse_result()
