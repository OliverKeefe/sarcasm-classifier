import os
import json
import tensorflow as tf
import numpy as np
import pandas as pd
import string
import zipfile
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from bs4 import BeautifulSoup

def get_data(filename, extract_path):
    if not os.path.exists(extract_path):
        try:
             with zipfile.ZipFile(filename, 'r') as file:
                file.extractall(extract_path)
                print(f"[+] Success, the dataset '{filename}' has been extracted to '{extract_path}'.")
        except FileNotFoundError:
            print("[!] Error, dataset not found!")
            exit(1)
    else:
        print(f"[*] The dataset '{extract_path}/Sarcasm_Headlines_Dataset.json' already exists.")

def format_data(data, stopwords):
    sentences = []
    labels = []
    urls = []
    with open(data) as file:
        for line in file:
            item = json.loads(line)
            sentence = item['headline'].lower()
            sentence = sentence.replace(",", " , ")
            sentence = sentence.replace(".", " . ")
            sentence = sentence.replace("-", " - ")
            sentence = sentence.replace("/", " / ")
            soup = BeautifulSoup(sentence)
            sentence = soup.get_text()
            words = sentence.split()
            filtered_sentence = ""
            for word in words:
                if word not in stopwords:
                    filtered_sentence += word + " "
            sentences.append(filtered_sentence)
            labels.append(item['is_sarcastic'])
            urls.append(item['article_link'])

    return sentences, labels, urls
# %%
def main():
    stopwords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at",
             "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do",
             "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having",
             "he", "hed", "hes", "her", "here", "heres", "hers", "herself", "him", "himself", "his", "how",
             "hows", "i", "id", "ill", "im", "ive", "if", "in", "into", "is", "it", "its", "itself",
             "lets", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought",
             "our", "ours", "ourselves", "out", "over", "own", "same", "she", "shed", "shell", "shes", "should",
             "so", "some", "such", "than", "that", "thats", "the", "their", "theirs", "them", "themselves", "then",
             "there", "theres", "these", "they", "theyd", "theyll", "theyre", "theyve", "this", "those", "through",
             "to", "too", "under", "until", "up", "very", "was", "we", "wed", "well", "were", "weve", "were",
             "what", "whats", "when", "whens", "where", "wheres", "which", "while", "who", "whos", "whom", "why",
             "whys", "with", "would", "you", "youd", "youll", "youre", "youve", "your", "yours", "yourself",
             "yourselves"]

    dataset_path = "Sarcasm_Headlines_Dataset.json.zip"
    extract_path = "dataset"
    get_data(dataset_path, extract_path)
    dataset = extract_path + "/Sarcasm_Headlines_Dataset.json"
    sentences, labels, urls = format_data(dataset, stopwords)
    print(sentences, labels, urls)

    xs=[]
    ys=[]
    current_item=1
    for item in sentences:
      xs.append(current_item)
      current_item=current_item+1
      ys.append(len(item))
    newys = sorted(ys)
    

if __name__ == "__main__":
    main()



