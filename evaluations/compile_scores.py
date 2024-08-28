import os
import pandas as pd
import numpy as np

base_dir = '/Users/amanpriyanshu/Desktop/blog/FRACTURED-SORRY-Bench'
base_responses_dir = os.path.join(base_dir, 'responses')
for dir_name in os.listdir(base_responses_dir):
    dir_path = os.path.join(base_responses_dir, dir_name)
    if os.path.isdir(dir_path):
        print(dir_name)
        for csv_name in ['decomposed_responses.csv', 'vanilla_responses.csv']:
            csv_path = os.path.join(dir_path, csv_name)
            if os.path.exists(csv_path):
                df = pd.read_csv(csv_path)
                labels_array = df['llm-eval'].tolist()
                labels, counts = np.unique(labels_array, return_counts=True)
                print('\t', csv_name)
                print('\t\t', labels, counts)