from classifier import *
#Data Link :- https://s3.console.aws.amazon.com/s3/buckets/vlifedata/Vlife_3.0/bio_lemm_data/data/?region=us-east-1&tab=overview

class BioLemmetizer:
#     def __init__(self,path):
#         self.path=path
        
    def predict():

        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                            datefmt='%m/%d/%Y %H:%M:%S',
                            level=logging.INFO)
        logger = logging.getLogger(__name__)
        
        DATA_PATH = Path('./data')

        PATH = Path('./data/tmp')
        PATH.mkdir(exist_ok=True)

        CLAS_DATA_PATH = PATH/'class'
        CLAS_DATA_PATH.mkdir(exist_ok=True)

        model_state_dict = None

        PYTORCH_PRETRAINED_BERT_CACHE = DATA_PATH
        PYTORCH_PRETRAINED_BERT_CACHE.mkdir(exist_ok=True)
        
        args = {
            "train_size": -1,
            "val_size": -1,
            "full_data_dir": DATA_PATH,
            "data_dir": PATH,
            "task_name": "toxic_multilabel",
            "no_cuda": False,
            "bert_model": 'bert-base-uncased',
            "output_dir": CLAS_DATA_PATH/'output',
            "max_seq_length": 128, #Increase to 512
            "do_train": True,
            "do_eval": True,
            "do_lower_case": True,
            "train_batch_size": 16, #Increase to 32
            "eval_batch_size": 16, #Increase to 32
            "learning_rate": 3e-5,
            "num_train_epochs": 4.0,
            "warmup_proportion": 0.1,
            "no_cuda": False,
            "local_rank": -1,
            "seed": 42,
            "gradient_accumulation_steps": 1,
            "optimize_on_cpu": False,
            "fp16": False,
            "loss_scale": 128
        }
        
        processors = {
            'toxic_multilabel':MultiLabelTextProcessor
        }
        
        task_name = args['task_name'].lower()

        if task_name not in processors:
            raise ValueError("Task not found: %s" % (task_name))
        
        processor = processors[task_name](args['data_dir'])
        label_list = processor.get_labels()
        num_labels = len(label_list)
        
        if args["local_rank"] == -1 or args["no_cuda"]:
            device = torch.device("cuda" if torch.cuda.is_available() and not args["no_cuda"] else "cpu")
            n_gpu = torch.cuda.device_count()
        else:
            torch.cuda.set_device(args['local_rank'])
            device = torch.device("cuda", args['local_rank'])
            n_gpu = 1
            # Initializes the distributed backend which will take care of sychronizing nodes/GPUs
            torch.distributed.init_process_group(backend='nccl')
        logger.info("device: {} n_gpu: {}, distributed training: {}, 16-bits training: {}".format(
                device, n_gpu, bool(args['local_rank'] != -1), args['fp16']))

        def convert_examples_to_features(examples, label_list, max_seq_length, tokenizer):

            label_map = {label : i for i, label in enumerate(label_list)}

            features = []
            for (ex_index, example) in enumerate(examples):
                tokens_a = tokenizer.tokenize(example.text_a)

                tokens_b = None
                if example.text_b:
                    tokens_b = tokenizer.tokenize(example.text_b)

                    _truncate_seq_pair(tokens_a, tokens_b, max_seq_length - 3)
                else:
                    # Account for [CLS] and [SEP] with "- 2"
                    if len(tokens_a) > max_seq_length - 2:
                        tokens_a = tokens_a[:(max_seq_length - 2)]


                tokens = ["[CLS]"] + tokens_a + ["[SEP]"]
                segment_ids = [0] * len(tokens)

                if tokens_b:
                    tokens += tokens_b + ["[SEP]"]
                    segment_ids += [1] * (len(tokens_b) + 1)

                input_ids = tokenizer.convert_tokens_to_ids(tokens)

                # The mask has 1 for real tokens and 0 for padding tokens. Only real
                # tokens are attended to.
                input_mask = [1] * len(input_ids)

                # Zero-pad up to the sequence length.
                padding = [0] * (max_seq_length - len(input_ids))
                input_ids += padding
                input_mask += padding
                segment_ids += padding

                assert len(input_ids) == max_seq_length
                assert len(input_mask) == max_seq_length
                assert len(segment_ids) == max_seq_length

                labels_ids = []
                for label in example.labels:
                    labels_ids.append(float(label))

                if ex_index < 0:
                    logger.info("*** Example ***")
                    logger.info("guid: %s" % (example.guid))
                    logger.info("tokens: %s" % " ".join(
                            [str(x) for x in tokens]))
                    logger.info("input_ids: %s" % " ".join([str(x) for x in input_ids]))
                    logger.info("input_mask: %s" % " ".join([str(x) for x in input_mask]))
                    logger.info(
                            "segment_ids: %s" % " ".join([str(x) for x in segment_ids]))
                    logger.info("label: %s (id = %s)" % (example.labels, labels_ids))

                features.append(
                        InputFeatures(input_ids=input_ids,
                                      input_mask=input_mask,
                                      segment_ids=segment_ids,
                                      label_ids=labels_ids))
            return features
        
        tokenizer = BertTokenizer.from_pretrained(args['bert_model'], do_lower_case=args['do_lower_case'])
        def accuracy(out, labels):
            outputs = np.argmax(out, axis=1)
            return np.sum(outputs == labels)

        def accuracy_thresh(y_pred:Tensor, y_true:Tensor, thresh:float=0.5, sigmoid:bool=True):
            "Compute accuracy when `y_pred` and `y_true` are the same size."
            if sigmoid: y_pred = y_pred.sigmoid()
            return np.mean(((y_pred>thresh)==y_true.bool()).float().cpu().numpy(), axis=1).sum()


        def fbeta(y_pred:Tensor, y_true:Tensor, thresh:float=0.2, beta:float=2, eps:float=1e-9, sigmoid:bool=True):
            "Computes the f_beta between `preds` and `targets`"
            beta2 = beta ** 2
            if sigmoid: y_pred = y_pred.sigmoid()
            y_pred = (y_pred>thresh).float()
            y_true = y_true.float()
            TP = (y_pred*y_true).sum(dim=1)
            prec = TP/(y_pred.sum(dim=1)+eps)
            rec = TP/(y_true.sum(dim=1)+eps)
            res = (prec*rec)/(prec*beta2+rec+eps)*(1+beta2)
            return res.mean().item()
        
        eval_examples = processor.get_dev_examples(args['data_dir'], size=args['val_size'])
        def eval():
            args['output_dir'].mkdir(exist_ok=True)


            eval_features = convert_examples_to_features(
                eval_examples, label_list, args['max_seq_length'], tokenizer)
            logger.info("***** Running evaluation *****")
            logger.info("  Num examples = %d", len(eval_examples))
            logger.info("  Batch size = %d", args['eval_batch_size'])
            all_input_ids = torch.tensor([f.input_ids for f in eval_features], dtype=torch.long)
            all_input_mask = torch.tensor([f.input_mask for f in eval_features], dtype=torch.long)
            all_segment_ids = torch.tensor([f.segment_ids for f in eval_features], dtype=torch.long)
            all_label_ids = torch.tensor([f.label_ids for f in eval_features], dtype=torch.float)
            eval_data = TensorDataset(all_input_ids, all_input_mask, all_segment_ids, all_label_ids)
            # Run prediction for full data
            eval_sampler = SequentialSampler(eval_data)
            eval_dataloader = DataLoader(eval_data, sampler=eval_sampler, batch_size=args['eval_batch_size'])

            all_logits = None
            all_labels = None

            model.eval()
            eval_loss, eval_accuracy = 0, 0
            nb_eval_steps, nb_eval_examples = 0, 0
            for input_ids, input_mask, segment_ids, label_ids in eval_dataloader:
                input_ids = input_ids.to(device)
                input_mask = input_mask.to(device)
                segment_ids = segment_ids.to(device)
                label_ids = label_ids.to(device)

                with torch.no_grad():
                    tmp_eval_loss = model(input_ids, segment_ids, input_mask, label_ids)
                    logits = model(input_ids, segment_ids, input_mask)

                tmp_eval_accuracy = accuracy_thresh(logits, label_ids)
                if all_logits is None:
                    all_logits = logits.detach().cpu().numpy()
                else:
                    all_logits = np.concatenate((all_logits, logits.detach().cpu().numpy()), axis=0)

                if all_labels is None:
                    all_labels = label_ids.detach().cpu().numpy()
                else:    
                    all_labels = np.concatenate((all_labels, label_ids.detach().cpu().numpy()), axis=0)


                eval_loss += tmp_eval_loss.mean().item()
                eval_accuracy += tmp_eval_accuracy

                nb_eval_examples += input_ids.size(0)
                nb_eval_steps += 1

            eval_loss = eval_loss / nb_eval_steps
            eval_accuracy = eval_accuracy / nb_eval_examples

        #     ROC-AUC calcualation
            # Compute ROC curve and ROC area for each class
            fpr = dict()
            tpr = dict()
            roc_auc = dict()

            for i in range(num_labels):
                fpr[i], tpr[i], _ = roc_curve(all_labels[:, i], all_logits[:, i])
                roc_auc[i] = auc(fpr[i], tpr[i])

            # Compute micro-average ROC curve and ROC area
            fpr["micro"], tpr["micro"], _ = roc_curve(all_labels.ravel(), all_logits.ravel())
            roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

            result = {'eval_loss': eval_loss,
                      'eval_accuracy': eval_accuracy,
                      'roc_auc': roc_auc  }

            output_eval_file = os.path.join(args['output_dir'], "eval_results.txt")
            with open(output_eval_file, "w") as writer:
                logger.info("***** Eval results *****")
                for key in sorted(result.keys()):
                    logger.info("  %s = %s", key, str(result[key]))
            return result
        
        output_model_file = os.path.join(PYTORCH_PRETRAINED_BERT_CACHE, "finetuned_pytorch_model.bin")
        #Load from disk
        model_state_dict = torch.load(output_model_file)
        model = BertForMultiLabelSequenceClassification.from_pretrained(args['bert_model'], num_labels = num_labels, state_dict=model_state_dict)
        model.to(device)
        eval()
        def predict(model, path, test_filename='test.csv'):
            predict_processor = MultiLabelTextProcessor(path)
            test_examples = predict_processor.get_test_examples(path, test_filename, size=-1)

#            print(test_examples)


            label_map = {i : label for i, label in enumerate(label_list)}

            labels_set = []

            for ex in test_examples:
                #print(ex)
                tmp = []
                for j, label in enumerate(ex.labels):
                    if label == 1:
                        tmp.append(label_map[j])
                labels_set.append(tmp)

            input_data = [{'id': input_example.guid, 'text': input_example.text_a, 'labels': input_example.labels, 'label_set': label_set}
                         for (input_example, label_set) in zip(test_examples, labels_set)]

            test_features = convert_examples_to_features(
                test_examples, label_list, args['max_seq_length'], tokenizer)

            logger.info("***** Running prediction *****")
            logger.info("  Num examples = %d", len(test_examples))
            logger.info("  Batch size = %d", args['eval_batch_size'])

            all_input_ids = torch.tensor([f.input_ids for f in test_features], dtype=torch.long)
            all_input_mask = torch.tensor([f.input_mask for f in test_features], dtype=torch.long)
            all_segment_ids = torch.tensor([f.segment_ids for f in test_features], dtype=torch.long)

            test_data = TensorDataset(all_input_ids, all_input_mask, all_segment_ids)

            # Run prediction for full data
            test_sampler = SequentialSampler(test_data)
            test_dataloader = DataLoader(test_data, sampler=test_sampler, batch_size=args['eval_batch_size'])

            all_logits = None
            all_logits_sig = None
            all_logits_bin = None

            model.eval()
            eval_loss, eval_accuracy = 0, 0
            nb_eval_steps, nb_eval_examples = 0, 0
            for step, batch in enumerate(tqdm(test_dataloader, desc="Prediction Iteration")):
                input_ids, input_mask, segment_ids = batch
                input_ids = input_ids.to(device)
                input_mask = input_mask.to(device)
                segment_ids = segment_ids.to(device)

                with torch.no_grad():
                    logits = model(input_ids, segment_ids, input_mask)
                    logits_sig = logits.sigmoid()
                    t = torch.Tensor([0.5]).to(device)  # threshold
                    logits_bin = (logits_sig > t).int() * 1

                if all_logits is None:
                    all_logits = logits.detach().cpu().numpy()
                else:
                    all_logits = np.concatenate((all_logits, logits.detach().cpu().numpy()), axis=0)

                if all_logits_sig is None:
                    all_logits_sig = logits_sig.detach().cpu().numpy()
                else:
                    all_logits_sig = np.concatenate((all_logits_sig, logits_sig.detach().cpu().numpy()), axis=0)

                if all_logits_bin is None:
                    all_logits_bin = logits_bin.detach().cpu().numpy()
                else:
                    all_logits_bin = np.concatenate((all_logits_bin, logits_bin.detach().cpu().numpy()), axis=0)


                nb_eval_examples += input_ids.size(0)
                nb_eval_steps += 1


            preds = []
            for ex in all_logits_bin:
                tmp = []
                for j, label in enumerate(ex):
                    if label == 1:
                        tmp.append(label_map[j])
                preds.append(tmp)

            out = [{'predictions': pred} for pred in preds]

            merge1 = pd.merge(pd.DataFrame(input_data), pd.DataFrame(out), left_index=True, right_index=True)

            pred_sig = [{'predictions_sigmoid': sig} for sig in all_logits_sig]

            df2 = pd.merge(merge1, pd.DataFrame(pred_sig), left_index=True, right_index=True)

            pred_binary = [{'predictions_binary': sig} for sig in all_logits_bin]

            df3 = pd.merge(df2, pd.DataFrame(pred_binary), left_index=True, right_index=True)

            pred_scores = [{'predictions_raw': pred} for pred in all_logits]

            return pd.merge(df3, pd.DataFrame(pred_scores), left_index=True, right_index=True)
        def clean_text(text):
            df1=text.lower()
            result1=re.sub(r'\d+','',df1)       #remove numbers
            result2=result1.translate(str.maketrans('', '', string.punctuation)) #remove punctuation
            result3=result2.strip() # remove whitespaces
            stop_words=set(stopwords.words('english'))
            tokens=word_tokenize(result3)
            result4=[i for i in tokens if not i in stop_words] # remove stopwords
            result5=' '.join(result4)
            result6=re.sub(r'\b\w{1,3}\b','',result5)
            return result6
        result = predict(model, DATA_PATH)
        result['labels'] = result['labels'].apply(lambda x: x.tolist())
        result['predictions_sigmoid'] = result['predictions_sigmoid'].apply(lambda x: x.tolist())
        result['predictions_binary'] = result['predictions_binary'].apply(lambda x: x.tolist())
        result['predictions_raw'] = result['predictions_raw'].apply(lambda x: x.tolist())
        result_1 = result[['id','label_set','labels','text','predictions','predictions_binary']]
        result_1[['250.0', '428.0', '518.81', '584.9']] = pd.DataFrame(result_1.predictions_binary.values.tolist(), index= result_1.index)
        result_1['cost_250.0']=[12.42*i for i in result_1['250.0']]
        result_1['cost_428.0']=[13.21*i for i in result_1['428.0']]
        result_1['cost_518.81']=[14.64*i for i in result_1['518.81']]
        result_1['cost_584.9']=[14.24*i for i in result_1['584.9']]
        result_1['Total_medication_cost']=result_1['cost_250.0']+result_1['cost_428.0']+result_1['cost_518.81']+result_1['cost_584.9']
        result_1.to_csv('test_data_output.csv',index=False)
        return "Prediction done in 'test_data_output.csv' file"