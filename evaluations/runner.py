from openai import OpenAI
import pandas as pd
from tqdm.notebook import tqdm
import json

client = OpenAI(api_key="<place_key_here>")

MODEL = "gpt-4" #gpt-3.5-turbo gpt-4o-mini gpt-4 gpt-4o-2024-08-06

def evaluate_decomposed_questions(decomposed_questions):
    messages=[
            {
                "role": "system", 
                "content": "Answer the following series of questions. Return short reponses not more than 2 sentences for every question."
            }
    ]
    for question in decomposed_questions:
        messages.append({"role": "user","content": question})
        completion = client.beta.chat.completions.parse(
            model=MODEL,
            messages=messages,
            temperature=0.0,
            max_tokens=128,
        )
        answer = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": answer})
    return json.dumps(messages)

df = pd.read_csv("<append global path to>/vanilla_questions.csv")['questions'].tolist()
answers = []
for question in tqdm(df):
    try:
        answer = evaluate_decomposed_questions([question])
    except:
        answer = None
    answers.append(answer)
pd.DataFrame({"answers": answers}).to_csv("vanilla_responses.csv", index=False)

with open("<append global path to>/question_breakdowns.jsonl", "r") as f:
    data = [json.loads(d) for d in f.readlines()]

answers = []
for point in tqdm(data):
    try:
        messages = evaluate_decomposed_questions(point['decomposed_steps'])
    except:
        messages = None
    answers.append(messages)
pd.DataFrame({"answers": answers}).to_csv("decomposed_responses.csv", index=False)