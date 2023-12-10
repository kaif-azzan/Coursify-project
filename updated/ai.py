from transformers import pipeline

summarize=pipeline("sentiment-analysis")

res=summarize("im not feeling good")
print(res)