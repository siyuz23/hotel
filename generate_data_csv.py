import os
import pandas as pd

DATA_ROOT = 'C:/Users/siyuz/PycharmProjects/hotel/data'

review_text = []    # str
is_spam = []        # 0, 1
is_positive = []    # 0, 1
hotel_name = []     # str

for polarity in os.listdir(DATA_ROOT):
    for source in os.listdir(f'{DATA_ROOT}/{polarity}'):
        for fold in os.listdir(f'{DATA_ROOT}/{polarity}/{source}'):
            for filename in os.listdir(f'{DATA_ROOT}/{polarity}/{source}/{fold}'):
                if filename.split('.')[0].split('_')[0] == 'd':
                    is_spam.append(1)
                else:
                    is_spam.append(0)
                hotel_name.append(filename.split('.')[0].split('_')[1])
                if polarity.split('_')[0] == 'negative':
                    is_positive.append(0)
                else:
                    is_positive.append(1)
                with open(f'{DATA_ROOT}/{polarity}/{source}/{fold}/{filename}', 'r') as file:
                    review_text.append(file.read().rstrip())

df = pd.DataFrame()
df['hotel_name'] = hotel_name
df['is_positive'] = is_positive
df['is_spam'] = is_spam
df['review_text'] = review_text

df.to_csv(f'{DATA_ROOT}/data.csv', index=False)


