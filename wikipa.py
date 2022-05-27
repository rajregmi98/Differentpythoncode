import warnings
warnings.filterwarnings("ignore")

import wikipedia
import random


value=input("Enter the words: ")
try:
    m=wikipedia.search(value,3)
    print(wikipedia.summary(m[0],sentences=2))
    # print(p)
except wikipedia.exceptions.DisambiguationError as e:
    s=random.choice(e.options)
    p=wikipedia.summary(s,sentences=2)
    print(p)