'''Write a python program to create and display a data frame from a specified dictionary data which has the index labels.
Also write a program to iterate over rows in a dataframe.'''
import pandas as pd

exam_data = {'name': ['Anil', 'Divya', 'Kiran', 'James', 'Eric', 'Manoj', 'Naveen', 'Lilly', 'Keerthi', 'Jyothi'],
             'score': [12.5, 9, 16.5, 20, 9, 20, 14.5, 30, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
print("Summary of the basic information about this DataFrame and its data")
print(df.info())
print("The data frame")
print(df)
print('People who qualified with more than 2 attempts')
print(df[df['attempts'] > 2])
print('Qualified people in the examination')
print(df[df['qualify'] == 'yes'])
