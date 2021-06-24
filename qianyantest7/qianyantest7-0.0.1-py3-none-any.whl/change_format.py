#coding=utf8
import json

preds={}
with open('rocket_test_predictions.json', 'r') as f:
    for line in f:
        line=json.loads(line.strip())
        preds[line['query_id']]=line['answer_text']
with open('preds.json', 'w') as f:
    json.dump(preds, f, ensure_ascii=False, indent=4)