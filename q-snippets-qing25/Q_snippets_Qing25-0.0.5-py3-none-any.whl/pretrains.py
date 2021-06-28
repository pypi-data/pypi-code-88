import os
import time
from dataclasses import dataclass
from transformers import AutoModel, AutoTokenizer, PreTrainedModel
from transformers import AutoModelForCausalLM, AutoModelForMaskedLM, AutoModelForTokenClassification
from transformers import BertTokenizer, BertModel, BertForMaskedLM, BertForQuestionAnswering
from transformers import T5ForConditionalGeneration, MT5ForConditionalGeneration, PegasusForConditionalGeneration, PegasusTokenizer
from transformers import GPT2LMHeadModel
try:
    from roformer import RoFormerPreTrainedModel, RoFormerTokenizer
except:
    print("To use roformer, run `pip install roformer` first")

ROOT = "/pretrains/pt"

@dataclass
class ModelInfo:
    web_dirname : str                        # hfl/bert-base-wwm
    model : object = AutoModel
    tokenizer : object = AutoTokenizer
    save_dir : str = None                    # example: /pretrians/pt/hfl-bert-base-wwm

    @property
    def local_dirname(self):
        return self.web_dirname.replace("/", "-", 1)     # hfl-bert-base-wwm
    
    @property
    def web_url(self):
        return "https://huggingface.co/"+self.web_dirname

    @property
    def local_url(self):
        if self.save_dir is None:
            return os.path.join(ROOT, self.local_dirname)
        else:
            return self.save_dir

    def save(self):
        t1 = time.time()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t1)))
        self.m = self.model.from_pretrained(self.web_dirname)
        self.t = self.tokenizer.from_pretrained(self.web_dirname)
        t2 = time.time()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t2)), f"---- Downloading finished in {(t2-t1):.2f} seconds.")
        self.m.save_pretrained(self.local_url)
        self.t.save_pretrained(self.local_url)
        print(f"saved to {self.local_url}; please check if warning info exists \n "
                "Or you'd better re-save the model with correct model head ! {self.web_url}")

    def is_saved(self):
        return os.path.exists(self.local_url)

models = [
    
    ModelInfo('hfl/chinese-roberta-wwm-ext-large'),
    ModelInfo('hfl/chinese-bert-wwm-ext'),
    ModelInfo('hfl/chinese-bert-wwm'),
    ModelInfo('hfl/chinese-macbert-base'),
    ModelInfo('hfl/chinese-macbert-large'),
    ModelInfo('hfl/chinese-electra-180g-large-discriminator'),
    ModelInfo('hfl/chinese-legal-electra-large-discriminator'),
    ModelInfo('hfl/chinese-xlnet-mid'),
    ModelInfo('hfl/chinese-xlnet-base'),
    ModelInfo('hfl/rbt3'),           # re-trained 3-layer RoBERTa-wwm-ext model
    # QA
    ModelInfo('luhua/chinese_pretrain_mrc_roberta_wwm_ext_large', model=BertForQuestionAnswering, tokenizer=BertTokenizer),
    ModelInfo('luhua/chinese_pretrain_mrc_macbert_large', model=BertForQuestionAnswering, tokenizer=BertTokenizer),
    ModelInfo('uer/roberta-base-chinese-extractive-qa', model=BertForQuestionAnswering, tokenizer=BertTokenizer),
    ModelInfo('mrm8488/spanbert-large-finetuned-squadv2', model=BertForQuestionAnswering, tokenizer=BertTokenizer),
    ModelInfo('schen/longformer-chinese-base-4096'),
    # https://github.com/CLUEbenchmark/CLUEPretrainedModels
    ModelInfo('clue/roberta_chinese_clue_tiny' ),
    ModelInfo('clue/roberta_chinese_pair_tiny'),
    ModelInfo('clue/roberta_chinese_3L768_clue_tiny'),
    ModelInfo('clue/roberta_chinese_3L312_clue_tiny' ),
    ModelInfo('clue/roberta_chinese_clue_large' ),
    ModelInfo('clue/roberta_chinese_pair_large'),
    ModelInfo('clue/xlnet_chinese_large'),
    # https://github.com/renmada/t5-pegasus-pytorch
    ModelInfo('imxly/t5-pegasus',  model=MT5ForConditionalGeneration, tokenizer=BertTokenizer),
    ModelInfo('imxly/t5-pegasus-small',  model=MT5ForConditionalGeneration, tokenizer=BertTokenizer),
    # https://huggingface.co/uer
    ModelInfo('uer/chinese_roberta_L-2_H-128', model=BertForMaskedLM, tokenizer=BertTokenizer),
    ModelInfo('uer/chinese_roberta_L-2_H-768', model=BertForMaskedLM, tokenizer=BertTokenizer),
    ModelInfo('uer/t5-base-chinese-cluecorpussmall',  model=T5ForConditionalGeneration, tokenizer=BertTokenizer),
    ModelInfo('uer/t5-small-chinese-cluecorpussmall',  model=T5ForConditionalGeneration, tokenizer=BertTokenizer),
    ModelInfo('uer/gpt2-chinese-poem', model=GPT2LMHeadModel, tokenizer=BertTokenizer),
    ModelInfo('uer/gpt2-base-chinese-cluecorpussmall', model=GPT2LMHeadModel, tokenizer=BertTokenizer),
    ModelInfo('uer/gpt2-distil-chinese-cluecorpussmall', model=GPT2LMHeadModel, tokenizer=BertTokenizer),
    ModelInfo('uer/pegasus-base-chinese-cluecorpussmall', model=GPT2LMHeadModel, tokenizer=BertTokenizer),

    ModelInfo('voidful/albert_chinese_xxlarge'),
    ModelInfo('wptoux/albert-chinese-large-qa'),
    ModelInfo("junnyu/roformer_chinese_small", model=RoFormerPreTrainedModel, tokenizer=RoFormerTokenizer),
    ModelInfo("junnyu/roformer_chinese_base", model=RoFormerPreTrainedModel, tokenizer=RoFormerTokenizer),
    ModelInfo("junnyu/roformer_chinese_char_base", model=RoFormerPreTrainedModel, tokenizer=RoFormerTokenizer),
    ModelInfo("ckiplab/gpt2-base-chinese", model=AutoModelForMaskedLM, tokenizer=BertTokenizer),     # https://huggingface.co/ckiplab/gpt2-base-chinese
    # 古文
    ModelInfo('ethanyt/guwenbert-base'),         # https://huggingface.co/ethanyt/guwenbert-base
    ModelInfo('ethanyt/guwenbert-large'),
    ModelInfo('SIKU-BERT/sikubert'),
    ModelInfo('SIKU-BERT/sikuroberta'),
    ModelInfo('uer/gpt2-chinese-ancient', model=GPT2LMHeadModel, tokenizer=BertTokenizer),
    # English
    ModelInfo('prajjwal1/bert-tiny'),
    ModelInfo('bert-base-uncased'),
    ModelInfo('bert-large-uncased'),
    ModelInfo('xlm-roberta-large'),
    ModelInfo('distilroberta-base'),
    ModelInfo('gpt2-large'),
    ModelInfo('gpt2'),
    ModelInfo('distilgpt2'),
    ModelInfo('microsoft/DialoGPT-large'),
    ModelInfo('facebook/bart-base'),
    ModelInfo('allenai/longformer-base-4096'),
    ModelInfo('allenai/t5-small-squad11'),
    ModelInfo('allenai/longformer-large-4096-finetuned-triviaqa'),
    ModelInfo('allenai/unifiedqa-t5-small'),
    ModelInfo('allenai/unifiedqa-t5-11b'),
    ModelInfo('allenai/unifiedqa-t5-large'),
    ModelInfo('allenai/t5-small-squad2-question-generation'),
    ModelInfo('SpanBERT/spanbert-base-cased'),
    ModelInfo('SpanBERT/spanbert-large-cased'),
    ModelInfo('tuner007/pegasus_paraphrase', model=PegasusForConditionalGeneration, tokenizer=PegasusTokenizer),    #https://huggingface.co/tuner007/pegasus_paraphrase
    ModelInfo('t5-large'),
    ModelInfo('t5-small'),
    ModelInfo('t5-base'),
    ModelInfo('facebook/bart-large'),
    ModelInfo('google/bigbird-roberta-base'),
    ModelInfo('google/bigbird-roberta-large'),
    ModelInfo('google/byt5-small'),
    ModelInfo('google/byt5-base'),
    ModelInfo('google/byt5-large'),
    ModelInfo('google/byt5-xl'),
    ModelInfo('google/byt5-xxl'),
    ModelInfo('google/mt5-small'),
    ModelInfo('google/mt5-base'),
    ModelInfo('google/mt5-large'),
    ModelInfo('google/mt5-xxl'),
    ModelInfo('google/roberta2roberta_L-24_cnn_daily_mail'),
    ModelInfo('google/bigbird-pegasus-large-arxiv'),
    # ModelInfo(''),
] 


def get_model_url(string):
    """
    如果该预训练模型已经被保存到本地了，则返回本地路径
    否则，如果在本文件的模型集合中，则下载后保存，如果不在，则直接保存到本地； 最后返回本地路径
    Args:
        string (str): 预训练模型的huggingface标识， 如 hfl/roberta_chinese_wwm

    Returns:
        str : 本地路径
    """
    tmp_model = ModelInfo(string)
    if tmp_model.is_saved():
        return tmp_model.local_url
    else:
        for model in models:
            if model.web_dirname == string:
                model.save()
                return model.local_url
            else:
                tmp_model.save()
                return tmp_model.local_url

def saved_pretrains():
    print("\n".join(sorted([ f"{_.is_saved()}\t{i}\t{_.local_url}"  for i, _ in enumerate(models)])))

if __name__ == '__main__':
    # for _ in models:
        # print(_.local_url)
    saved_pretrains()
    