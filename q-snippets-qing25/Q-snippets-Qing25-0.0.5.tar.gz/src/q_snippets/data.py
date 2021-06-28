import os
import torch
import json
import yaml
import numpy as np
import pandas as pd
from dataclasses import dataclass
from collections import defaultdict
from torch.utils.data import Dataset
import time
import hashlib
import multiprocessing
from p_tqdm import p_imap
from tqdm import tqdm

def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te-ts))
        return result

    return timed

def save_json(R, path):
    """ Obj, path """
    with open(path, 'w', encoding='utf8') as f:
        json.dump(R, f, indent=2, ensure_ascii=False)
    print(f"{path} loaded with {len(R)} samples!")

def load_json(path):
    with open(path, 'r', encoding='utf8') as f:
        obj = json.load(f)
    print(f"{path} loaded with {len(obj)} samples!")
    return obj

def load_yaml(path):
    with open(path) as fin:
        return yaml.safe_load(fin)


class BaseData:    
    def cpu(self):
        for k, v in self.__dict__.items():
            if type(v) is torch.Tensor:
                setattr(self, k, v.cpu())
        return self
    
    def to(self, device):
        for k,v in self.__dict__.items():
            if type(v) is torch.Tensor:
                setattr(self, k, v.to(device))
        return self
    
    def __getitem__(self,index):
        return self.__dict__[index]
    
    def todict(self):
        return self.__dict__
    
    def tolist(self):
        return [ v for k,v in self.__dict__.items()]

class BaseFeature(BaseData):
    @classmethod
    def from_tokenized(cls, td):
        return cls(
            input_ids=td['input_ids'],
            token_type_ids=td['token_type_ids'],
            attention_mask=td['attention_mask'],
            offset_mapping=td['offset_mapping'],
            overflow_to_sample_mapping=td['overflow_to_sample_mapping']
        )


@dataclass
class MRCSample(BaseData):

    qid: str = None
    title: str = None
    context: str = None
    question: str = None
    answer_texts: list = None
    answer_starts: list = None
    is_impossible: bool = None


@dataclass
class MRCBatch(BaseData):
    samples : MRCSample  = None
    input_ids: torch.Tensor =None
    attention_mask : torch.Tensor =None
    token_type_ids : torch.Tensor =None
    start_labels : torch.Tensor =None
    end_labels : torch.Tensor =None
    ans_labels : torch.Tensor =None
    offset_mappings : list = None
        
    def __len__(self):
        return self.input_ids.size(0)

def is_sample_valid(sample):
    """
    Args:
        sample (SquadSample): 读入的单条样本对象

    Returns:
        bool: 该数据的标注是否正确
    """
    if sample.answer_texts != []:
        text = sample.answer_texts[0]
        start_char = sample.answer_starts[0]
        # 标注的start_char的位置有问题
        if not sample.context[start_char:start_char+len(text)] == text:
            return False
    else:
        if sample.answer_starts != []:
            return False
    return True

def load_data(path):
    """
        从json文件中读取数据， json文件的格式为标准的Squad2.0或DuReader-checklist
    Args:
        path (str): json 文件路径

    Returns:
        list: list of loaded MRCSamples
    """
    R, invalid = [], 0
    with open(path, 'r', encoding='utf8') as f:
        obj = json.load(f)
        for entry in obj['data']:
            for sample in entry['paragraphs']:
                context = sample['context'].strip()
                title = sample.get("title", "")
                for qas in sample['qas']:
                    sample = MRCSample(
                                qid = qas['id'],
                                title=title,
                                context=context,
                                question=qas['question'],
                                answer_texts=[ a['text'].strip() for a in qas.get('answers', [])],
                                answer_starts=[ a['answer_start'] for a in qas.get('answers', [])],
                                is_impossible=qas.get('is_impossible', None)
                            )
                    if is_sample_valid(sample):
                        R.append(sample)
                    else:
                        invalid += 1
    print(f"{path} loaded with {len(R)} MRCSamples! {invalid} invalid samples dropped!")
    return R

class MRCDataset(Dataset):

    _max_index = 99999
    def __init__(self, datas, tokenizer):
        self.datas = datas
        self.tokenizer = tokenizer
    
    def __len__(self):
        return len(self.datas)
    
    def __getitem__(self, index):
        sample = self.datas[index]
        qid, title, context, question, answer_texts, answer_starts, is_impossible = sample.tolist()
        if is_impossible == True or is_impossible is None:         # None 或 不可回答
            answer_text = ""
            # answer_start, answer_end = 0, 0    # 无答案的情况下，start和end指向[CLS] token
            answer_start, answer_end = self._max_index, self._max_index
        else:
            # ans_index = random.sample(range(len(sample.answer_texts)), 1)[0]            # 存在多个候选答案，随机选择一个作为训练目标
            ans_index = 0
            answer_text, answer_start = answer_texts[ans_index], answer_starts[ans_index]
            answer_end = answer_start + len(answer_text)    # 超出模型能处理的最大长度512也没关系，BertForQuestionAnswering在处理时会将
        
        return qid, title, context, question, answer_text, answer_start, answer_end, is_impossible, sample
    
    def _find_start_end_token_index(self, char_start, char_end, input_ids, offset_mapping):
        start_labels, end_labels, ans_labels = [], [], []
        for char_s, char_e, _input_ids, mapping in zip(char_start, char_end, input_ids, offset_mapping):
            if char_start == char_end == 0:
                start_labels.append(0)
                end_labels.append(0)
                ans_labels.append(0)
                continue
            token_s, token_e = None, None
            sep_idx = _input_ids.index(self.tokenizer.sep_token_id)
            context_mapping = mapping[sep_idx:]  # 从第一个SEP Token后开始找 
            for i, (_s, _e) in  enumerate(context_mapping):
                if _s == char_s and token_s is None:
                    token_s = i + sep_idx
                if _e == char_e and token_e is None:
                    token_e = i + sep_idx
            
            if token_e is not None and token_s is not None:
                start_labels.append(token_s)
                end_labels.append(token_e)
                ans_labels.append(1)
            elif token_s is not None:
                start_labels.append(token_s)
                end_labels.append(self._max_index)
                ans_labels.append(1)
            else:
                start_labels.append(0)
                end_labels.append(0)
                ans_labels.append(0)
        return start_labels, end_labels, ans_labels


    def collate_fn(self, batch):
        """
        这里传入的batch参数，即是batch_size条上面__getitem__返回的结果
        此函数返回的结果即为输入到模型中的一个batch
        """
        qid, title, context, question, answer_text, answer_start, answer_end, is_impossible, sample = zip(*batch)
        tokenized = self.tokenizer(list(question), list(context), max_length=512, padding=True, truncation=True, return_offsets_mapping=True)
        start_labels, end_labels, ans_labels = self._find_start_end_token_index(answer_start, answer_end, tokenized.input_ids, tokenized.offset_mapping)
        R = MRCBatch(
            samples= sample,
            input_ids= torch.tensor(tokenized.input_ids),
            attention_mask=torch.tensor(tokenized.attention_mask),
            token_type_ids=torch.tensor(tokenized.token_type_ids),
            start_labels=torch.tensor(start_labels),
            end_labels=torch.tensor(end_labels),
            ans_labels=torch.tensor(ans_labels),
            offset_mappings=tokenized.offset_mapping
        )
        return R


@dataclass
class MrcStridedBatch(BaseData):
    input_ids: torch.Tensor =None
    attention_mask : torch.Tensor =None
    token_type_ids : torch.Tensor =None
    start_positions : torch.Tensor =None
    end_positions : torch.Tensor =None
    ans_labels : torch.Tensor = None
        
    def __len__(self):
        return self.input_ids.size(0)


def load_samples_and_features_old(path, tokenizer, max_len, stride):
    """
        从json文件一次性生成 samples 和 features
    Args:
        path (str): json 文件路径
        tokenizer (transformers Tokenizer): 分词器，需是Fast版本
        max_len (int): 一条数据的最大长度
        stride (int): 步长

    Returns:
        tuple: (samples, features)
    """
    raw_samples = load_data(path)
    # questions = [examples[i]['question'] for i in range(len(examples))]
    questions_title = [raw_samples[i]['question']  + raw_samples[i]['title'] for i in range(len(raw_samples))]
    # title_contexts = [examples[i]['title'] + examples[i]['context'] for i in range(len(examples))]
    contexts = [raw_samples[i]['context'] for i in range(len(raw_samples))]
    tokenized_examples = tokenizer(questions_title,
                                    contexts,
                                    padding="max_length",
                                    max_length=max_len,
                                    truncation="only_second",
                                    stride=stride,
                                    return_offsets_mapping=True,
                                    return_overflowing_tokens=True)

    df_tmp = pd.DataFrame.from_dict(tokenized_examples, orient="index").T
    tokenized_examples = df_tmp.to_dict(orient="records")

    for i, tokenized_example in enumerate(tqdm(tokenized_examples)):
        input_ids = tokenized_example["input_ids"]
        cls_index = input_ids.index(tokenizer.cls_token_id)
        offsets = tokenized_example['offset_mapping']
        sequence_ids = tokenized_example['token_type_ids']

        # One example can give several spans, this is the index of the example containing this span of text.
        sample_index = tokenized_example['overflow_to_sample_mapping']
        answers = raw_samples[sample_index]['answer_texts']
        answer_starts = raw_samples[sample_index]['answer_starts']

        # If no answers are given, set the cls_index as answer.
        if len(answer_starts) == 0 or (answer_starts[0] == -1):
            tokenized_examples[i]["start_positions"] = cls_index
            tokenized_examples[i]["end_positions"] = cls_index
            tokenized_examples[i]['answerable_label'] = 0
        else:
            # Start/end character index of the answer in the text.
            start_char = answer_starts[0]
            end_char = start_char + len(answers[0])

            # Start token index of the current span in the text.
            token_start_index = 0
            while sequence_ids[token_start_index] != 1:
                token_start_index += 1

            # End token index of the current span in the text.
            token_end_index = len(input_ids) - 2
            while sequence_ids[token_end_index] != 1:
                token_end_index -= 1
            token_end_index -= 1

            # Detect if the answer is out of the span (in which case this feature is labeled with the CLS index).
            if not (offsets[token_start_index][0] <= start_char and
                    offsets[token_end_index][1] >= end_char):
                tokenized_examples[i]["start_positions"] = cls_index
                tokenized_examples[i]["end_positions"] = cls_index
                tokenized_examples[i]['answerable_label'] = 0
            else:
                # Otherwise move the token_start_index and token_end_index to the two ends of the answer.
                # Note: we could go after the last offset if the answer is the last word (edge case).

                while offsets[token_end_index][1] >= end_char:
                    token_end_index -= 1
                tokenized_examples[i]["end_positions"] = token_end_index + 1

                # 第二个句子长度为1 会出现mapping匹配不到的情况: (0,0)...(0,1),(0,0)...
                if start_char == 0:
                    token_start_index += 1
                else:
                    while offsets[token_start_index][0] <= start_char:
                        token_start_index += 1
                
                tokenized_examples[i]["start_positions"] = token_start_index - 1
                tokenized_examples[i]['answerable_label'] = 1

        # evaluate的时候有用
        tokenized_examples[i]["example_id"] = raw_samples[sample_index]['qid']
        tokenized_examples[i]["offset_mapping"] = [
            (o if sequence_ids[k] == 1 else None)
            for k, o in enumerate(tokenized_example["offset_mapping"])
        ]
        # tokenized_examples[i]['offset_mapping'] = tokenized_example['offset_mapping']
        # tokenized_examples[i]['sample'] = raw_samples[sample_index]

    print(f"raw_samples:{len(raw_samples)}, features:{len(tokenized_examples)}")    
    return raw_samples, tokenized_examples


@dataclass
class Feature(BaseData):
    # returns of tokenizer()
    input_ids : list
    token_type_ids : list
    attention_mask : list
    offset_mapping : list
    overflow_to_sample_mapping:list
    # additions
    start_positions : int  = None
    end_positions : int = None
    answerable_label : int = None
    sample_id : str = None


    @classmethod
    def from_tokenized(cls, td):
        """ 直接从tokenizer返回的结果生成一个Feature对象

        Args:
            td (dict): tokenizer返回的结果

        Returns:
            Feature : Feature的实例
        """
        return cls(
            input_ids=td['input_ids'],
            token_type_ids=td['token_type_ids'],
            attention_mask=td['attention_mask'],
            offset_mapping=td['offset_mapping'],
            overflow_to_sample_mapping=td['overflow_to_sample_mapping']
        )

def load_feature(datas, tokenizer, max_len=384, stride=128):
    questions = [sample.question for sample in datas]
    title_contexts = [sample.title + sample.context for sample in datas]
    td_samples = tokenizer(
        questions,
        title_contexts,
        padding="max_length",
        max_length=max_len,
        truncation="only_second",
        stride=stride,
        return_offsets_mapping=True,
        return_overflowing_tokens=True
    )
    
    df_tmp = pd.DataFrame.from_dict(td_samples, orient="index").T
    td_samples = df_tmp.to_dict(orient="records")
    # print(td_samples)

    R = []
    for i, td_sample in enumerate(tqdm(td_samples)):
        feature = Feature.from_tokenized(td_sample)

        input_ids = td_sample["input_ids"]
        cls_index = input_ids.index(tokenizer.cls_token_id)
        offsets = td_sample['offset_mapping']
        sequence_ids = td_sample['token_type_ids']

        # One example can give several spans, this is the index of the example containing this span of text.
        sample_index = td_sample['overflow_to_sample_mapping']

        answers = datas[sample_index].answer_texts
        answer_starts = datas[sample_index].answer_starts

        # If no answers are given, set the cls_index as answer.
        if len(answer_starts) == 0 or (answer_starts[0] == -1):
            feature.start_positions = cls_index
            feature.end_positions = cls_index
            feature.answerable_label = 0
        else:
            # Start/end character index of the answer in the text.
            start_char = answer_starts[0]
            end_char = start_char + len(answers[0])

            # Start token index of the current span in the text.
            token_start_index = sequence_ids.index(1)

            # End token index of the current span in the text.
            token_end_index = len(input_ids) - sequence_ids[::-1].index(1) - 2  # 不是SEP的最后一个

            # Detect if the answer is out of the span (in which case this feature is labeled with the CLS index).
            if not (offsets[token_start_index][0] <= start_char and offsets[token_end_index][1] >= end_char):
                feature.start_positions = cls_index
                feature.end_positions = cls_index
                feature.answerable_label = 0
            else:
                try:
                    while True:
                        if offsets[token_start_index][0] == start_char:
                            break
                        token_start_index += 1
                    
                    while True:
                        if offsets[token_end_index][1] == end_char:
                            break
                        token_end_index -= 1

                    assert token_start_index <= token_end_index
                except:
                    continue
                if token_end_index < token_start_index:
                    print(td_sample)
                feature.start_positions = token_start_index
                feature.end_positions = token_end_index
                feature.answerable_label = 1
            
        # evaluate的时候有用
        feature.sample_id = datas[sample_index].qid

        feature.offset_mapping = [
            (o if sequence_ids[k] == 1 else None)
            for k, o in enumerate(td_sample["offset_mapping"])
        ]
        # 校验生成的标注是否有问题
        context = datas[sample_index].context
        if feature.answerable_label == 0 and len(answers) == 0: # 本条数据无答案
            pass
        elif feature.answerable_label == 0 and len(answers)!=0: 
            pass # 本段文本没找到答案;如果这条数据有答案，但所有的分段都没找到标注答案，待处理！
        else:
            decoded = context[offsets[token_start_index][0]:offsets[token_end_index][1]]
            if decoded != answers[0]:
                print(decoded, answers)

        R.append(feature)
    return R

def load_samples_and_features(path, tokenizer, max_len, stride):
    datas = load_data(path)
    features = load_feature(datas, tokenizer, max_len, stride)
    return datas, features

class MrcStridedDataset(Dataset):
    def __init__(self, path, data_dir, tokenizer, max_len=384, stride=128):
        self.path = path
        self.data_dir = data_dir
        if not os.path.exists(self.data_dir):
            os.mkdir(self.data_dir)
        self.samples, self.features = self.load_cache(tokenizer, max_len, stride)

    def load_cache(self, tokenizer, max_len, stride):
        filename = os.path.basename(self.path)
        cachefile = os.path.join(self.data_dir, filename.split(".")[0]+".pt")
        cache_version = os.path.join(self.data_dir, "cache_version.pt")
        if os.path.exists(cachefile):
            _max_len, _stride = torch.load(cache_version)
            if not (_max_len, _stride) == (max_len, stride):
                print(f"cached version has max_len={_max_len}, stride={_stride}, recaching...")
            else:
                print(f"Using cached dataset in '{cachefile}' ~")
                samples, features = torch.load(cachefile)
                return samples, features
        
        # 重新加载数据，并缓存
        samples, features = load_samples_and_features(self.path, tokenizer, max_len, stride)
        torch.save((samples, features), cachefile)
        torch.save((max_len, stride), cache_version)
        return samples, features

    def __len__(self):
        return len(self.features)

    def __getitem__(self, index):
        return self.features[index]

    def collate_fn(self, batch):
        max_len = max([sum(x['attention_mask']) for x in batch])
        R = MrcStridedBatch(
            input_ids=torch.tensor([x['input_ids'][:max_len] for x in batch]),
            attention_mask=torch.tensor([x['attention_mask'][:max_len] for x in batch]),
            token_type_ids=torch.tensor([x['token_type_ids'][:max_len] for x in batch]),
            start_positions=torch.tensor([x["start_positions"] for x in batch]),
            end_positions=torch.tensor([x["end_positions"] for x in batch]),
            ans_labels=torch.tensor([x["answerable_label"] for x in batch])
        )
        return R


def span_decode(start_logits, end_logits, cls_logits=None, max_a_len=512, samples=None, offset_mappings=None, use_cls=True, no_answer=""):
    """

    Args:
        start_logits  (torch.Tensor) :  (bsz,seqlen)
        end_logits (torch.Tensor) :   (bsz,seqlen)
        cls_logits (torch.Tensor) :  (bsz, num_classes)
        max_a_len ( int ): 限制答案文本的最大长度
        samples (MRCSample ): 该条数据的所有信息
        offset_mappings ([type]): tokenizer返回的
        use_cls (bool, optional): 是否使用预测的有无答案的概率，False则一定会返回预测的span文本. Defaults to True.
        no_answer (str, optional): Squad和DuReader要求的无答案形式不同，. Defaults to "".

    Returns:
        Dict : {qid: pred_text, ...}
    """
    se_sum = end_logits[:,None,:] + start_logits[:,:,None]
    # 限制值的范围是s<e, 最大长度为 max_a_len        
    mask = torch.tril(torch.triu(torch.ones_like(se_sum), 0), max_a_len)   
    r = (mask * se_sum).masked_fill_((1-mask).bool(), float('-inf'))    # score值全是负的，导致0 > score，选出来s>e了
    start_max, end_max = r.max(2)[0].max(1)[1], r.max(1)[0].max(1)[1]
    answerable = cls_logits.argmax(-1) if cls_logits is not None else torch.zeros(start_logits.size(0),)
    R = {}
    for s, e, a, sample, mapping in zip(start_max, end_max, answerable, samples, offset_mappings):
        if a == 1 and use_cls:
            R[sample.qid] = no_answer
        else:
            s_char, e_char = mapping[s][0], mapping[e][-1]
            pred_text = sample.context[s_char:e_char]
            pred_text = no_answer if pred_text == "" else pred_text
            R[sample.qid] = pred_text
    return R


def nbest_span_decode(start_scores, end_scores, batch, max_a_len=512, nbest=5):
    # se_sum = end_scores[:,None,:] + start_scores[:,:,None]
    # r = torch.tril(torch.triu(torch.ones_like(se_sum), 0), max_a_len) * se_sum   # (0,0) is necessary !!!!!!!!!!!!
    se_sum = end_scores[:,None,:] + start_scores[:,:,None]
    # 限制值的范围是s<e, 最大长度为 max_a_len        
    mask = torch.tril(torch.triu(torch.ones_like(se_sum), 0), max_a_len)   
    r = (mask * se_sum).masked_fill_((1-mask).bool(), float('-inf'))

    pred_answers = defaultdict(dict)
    for mat, c, m, qid, a in zip(r, batch['context'], batch['offset_mapping'], batch['qids'], batch['gold']):
        pred_answers[qid]['gold'] = a
        pred_answers[qid]['nbest'] = []
        v, i = torch.topk(mat.flatten(), int(nbest))
        v, i = v.cpu(), i.cpu()
        for (s,e), p in zip(np.array(np.unravel_index(i.numpy(), mat.shape)).T, v):
            s_char, e_char =  m[s][0], m[e][-1]
            pred_text = c[s_char:e_char]
            pred_text = "no answer" if pred_text == "" else pred_text
            pred_answers[qid]['nbest'].append({"prob":f"{p.item():.3f}", "text": pred_text})
    return pred_answers


class DataProcessor():
    """用于多进程执行同一个函数
    """
    def __init__(self, num_workers):
        self.num_workers = num_workers

    def __call__(self, f, data):
        """
        对data中的每条数据用f单独处理， 自动使用num_workers个进程
        ```
        >>> datas = [s1,s2,...]
        >>> dp = DataProcessor(4)(datas, lambda x: ProcessedSample(x))
        >>> dp
            [ProcessedSample(s1), ProcessedSample(s2),...]
        ``` 
        Args:
            f (function): 输入为单条数据， 返回单条数据处理后的对象
            data (list):  数据的列表

        Returns:
            List : 处理后的数据对象的列表， eg: [Sample1, Sample2,...]
        """
        iterator = p_imap(f, data, num_cpus=self.num_workers)
        results = [ _ for _ in iterator]
        return results



def gen_uid(string):
    """
    根据字符串生成对应的Md5码
    Args:
        string (str): 需要是能标识该对象的独特字符串

    Returns:
        str: 十六进制字符串
    """
    return hashlib.md5(string.encode("utf8")).hexdigest()


def sequence_padding(inputs, length=None, force=False, padding=0):
    """Numpy函数，将序列padding到同一长度
    Args:
        inputs (list of lists): [description]
        length (int, optional): 指定最大长度. Defaults to None.
        force (bool, optional): 如果为True则一定Padding到length长度，否则padding到最长的list的长度. Defaults to False.
        padding (int, optional): Padding的值. Defaults to 0.

    Returns:
        np.array: padding后的序列
    """
    _length = max([len(x) for x in inputs])
    if length is None:
        length = _length
    else:
        length = min(length, _length) if not force else length

    outputs = np.array([
        np.concatenate([x, [padding] * (length - len(x))]) if len(x) < length else x[:length]
        for x in inputs
    ])
    return outputs  


def dict2list(td):
    """
        输入的是tokenizer一次处理多条数据的结果， 返回list, 其中每个dict是每条数据的结果
    Args:
        td (dict): {'input_ids': [[...],[...],...], 'attention_mask':...}

    Returns:
        [list]: [{'input_ids':[], 'attention_mask':[]},{},...]
    """
    df = pd.DataFrame.from_dict(td, orient='index').T
    return df.to_dict(orient='records')



class SegmentUtility():
    def __init__(self, seg_func) -> None:
        """

        Args:
            seg_func (function):  eg: lambda s: seg.cut(s) || jieba.lcut(s)
        """
        self.seg = seg_func

    def seg_start_end(self, sentence):
        """
            返回句子分词的结果，以及每个词对应的字符start end
        """
        words = self.seg(sentence)
        s,e = 0,0
        R = [[(s:=e, e:=s+len(word))] for word in words]
        return words, sum(R, [])

    @staticmethod
    def generate_seg_ids(tokenizer, input_ids, offset_mapping, se):
        """对于一个句子的input_ids， 根据该句子的中文分词结果，对于每个词的tokens给一个id
        从[CLS]是0开始，第一个词是1,...
        Args:
            input_ids (list): Tokenizer 返回的input_ids
            offset_mapping (list): Tokenizer 返回的 offset_mapping
            se (list): [(0,2),(2,6),...,(s,e)]

        Returns:
            list : [0,1,1,2,2,2,2,...]
        """
        R, ptr, word_ptr = [], 0, 0
        for token_id, (s,e) in zip(input_ids, offset_mapping):
            if (s,e) == (0,0) and token_id != tokenizer.pad_token_id:
                R.append(ptr)
                ptr += 1
            elif token_id == 0:  # padding
                R.append(ptr)
            elif se[word_ptr][0] <= s and e < se[word_ptr][1]:
                R.append(ptr)
            elif e == se[word_ptr][1]:
                R.append(ptr)
                word_ptr += 1
                ptr += 1
        assert len(R) == len(input_ids), f"{(len(R), R)},{(len(input_ids), input_ids)}"
        return R

    def prepare_inputs(self, tokenizer, first, second=None):
        """[summary]

        Args:
            tokenizer ([type]): [description]
            first (str): 第一个句子
            second (str, optional): 第二个句子 Defaults to None.

        Returns:
            [type]: [description]
        """
        words_1 = self.seg(first)
        s,e = 0,0
        se_1 = [[(s:=e, e:=s+len(word))] for word in words_1]
        
        if second is not None:
            words_2 = self.seg(second)
            s,e = 0,0
            se_2 = [[(s:=e, e:=s+len(word))] for word in words_2]
            
        td = tokenizer(first, second, return_offsets_mapping=True)
        td['se'] =  sum(se_1 if second is None else se_1 + se_2, [])
        return td

    def prepare_batch_inputs(self, tokenizer, first, second=None):
        """[summary]

        Args:
            tokenizer ([type]): [description]
            first (list):  字符串的列表
            second (list, optional): 字符串的list. Defaults to None.

        Returns:
            dict: 分词器分词后的结果，增加了words = [], se = []
        """
        td = tokenizer(first, second, return_offsets_mapping=True, padding=True)
        SE = []
        Seg = []
        if second is not None:
            for ids, mapping, a, b in zip(td.input_ids, td.offset_mapping, first, second):
                words_1 = self.seg(a)
                s,e = 0,0
                se_1 = [[(s:=e, e:=s+len(word))] for word in words_1]

                words_2 = self.seg(b)
                s,e = 0,0
                se_2 = [[(s:=e, e:=s+len(word))] for word in words_2]

                se = sum(se_1 + se_2, [])
                SE.append(se)
                Seg.append((words_1, words_2))
        else:
            for ids, mapping, a in zip(td.input_ids, td.offset_mapping, first):
                words_1 = self.seg(a)
                s,e = 0,0
                se_1 = [[(s:=e, e:=s+len(word))] for word in words_1]
                se = sum(se_1, [])
                SE.append(se)
                Seg.append(words_1)
        td.se = SE
        td.words = Seg
        return td