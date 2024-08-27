import json
import pandas as pd

def clean_file(file_path:str):
    data = pd.read_json(file_path, lines=True).to_dict()
    keys = list(data.keys())
    list_of_points = []
    for i in range(len(data[keys[0]])):
        result = {key_:data[key_][i] if 'question' not in key_ else 'question_id_'+str(i) for key_ in keys}
        list_of_points.append(result)
    for i,r in enumerate(list_of_points):
        if i==0:
            a = 'w'
        else:
            a = 'a'
        with open(file_path, a) as f:
            f.write(json.dumps(r) + "\n")

if __name__=='__main__':
    clean_file("benign_questions_decomposed.jsonl")
    clean_file("evaluations.jsonl")
    clean_file("question_breakdowns.jsonl")