import pandas as pd
scores = pd.read_csv('scores.csv')
print(scores['Total'].max())
print(scores['Total'].min())
print(scores)
print(scores.shape)
print(scores.count())
print(scores['Total'].mean())
print(scores['Total'].sum())
print(scores['Total'].sort_values()) #Ascending order
print(scores['Total'].sort_values(ascending=False)) #Descending order




'''import pandas as pd

# Example usage to verify
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
'''