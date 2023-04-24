from google_play_scraper import app
import pandas as pd
import numpy as np

from google_play_scraper import Sort, reviews_all


my11circle = reviews_all(
    'com.games24x7.my11circle.fantasycricket',
    sleep_milliseconds=0, 
    lang='en', 
    country='us', 
    sort=Sort.NEWEST,
)

df_my11 = pd.DataFrame(np.array(my11circle),columns=['review'])
df_my11 = df_my11.join(pd.DataFrame(df_my11.pop('review').tolist()))
df_my11.head()