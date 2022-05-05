from http.client import ImproperConnectionState
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import pickle 
import random
kml = pickle.load(open('k_means_movies.pkl','rb'))
print(15*"20")

print("Pick the genres You want to watch :")
print()
genres =['Adventure',
        'Animation',
        'Children',
        'Comedy',   
        'Fantasy',
        'Romance',
        'Drama',
        'Action',
        'Crime',
        'Thriller',
        'Horror',
        'Mystery',
        'Sci-Fi',
        'War',
        'Musical',
        'Documentary',
        'IMAX',
        'Western',
        'Film-Noir',
        '(no genres listed)']
j = 1 
for i in genres:
    print(f'({j})  {i}')
    j+=1

Choice = list(map(int,input("Enter Your Choices :").split(",")))

if max(Choice)>len(genres):
    print("Wrong Choice (Out of Bound index), Restart the program")
else  :
    choice = np.zeros(len(genres),int)
    choice = list(choice)
    for i in (1,len(genres)+1):
        if i in Choice:
            choice.insert(1,i-1)
    choice = np.array(choice)
    choice = choice.reshape(1,-1)
    cluster = kml.predict(choice)

    data = pd.read_csv('Movie_recommendatioin.csv')
    data = data[data.classes==cluster[0]]
    data = data.reset_index()
    rand_var = random.randint(0,len(data))
    print("----Try Watching ---- ")
    print()
    print(data.iloc[rand_var].title)
    print("Rerun the program for other recommendation")
