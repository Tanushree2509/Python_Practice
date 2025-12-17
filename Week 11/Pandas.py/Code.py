import pandas as pd
scores = pd.read_csv('scores.csv')
print(scores[scores['Gender'] =='M']['Total'].max())
print(scores[scores['Gender'] =='F']['Total'].min())
print(scores)