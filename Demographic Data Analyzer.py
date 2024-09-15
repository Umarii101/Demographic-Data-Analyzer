#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

# Load the dataset
df = pd.read_csv('demographic_data.csv')

# 1. How many people of each race are represented in this dataset?
race_counts = df['race'].value_counts()

# 2. What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()

# 3. What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

# 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_advanced_education_high_income = (df[advanced_education]['salary'] == '>50K').mean() * 100

# 5. What percentage of people without advanced education make more than 50K?
non_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_non_advanced_education_high_income = (df[non_advanced_education]['salary'] == '>50K').mean() * 100

# 6. What is the minimum number of hours a person works per week?
min_hours_per_week = df['hours-per-week'].min()

# 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_salary_percentage = (df[df['hours-per-week'] == min_hours_per_week]['salary'] == '>50K').mean() * 100

# 8. What country has the highest percentage of people that earn >50K and what is that percentage?
country_percentage_high_income = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100

if not country_percentage_high_income.empty:
    highest_percentage_country = country_percentage_high_income.idxmax()
    highest_percentage = country_percentage_high_income.max()
else:
    highest_percentage_country = 'None'
    highest_percentage = 0

# 9. Identify the most popular occupation for those who earn >50K in India.
india_high_income_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

if not india_high_income_occupation.empty:
    most_popular_occupation_india = india_high_income_occupation['occupation'].mode()[0]
else:
    most_popular_occupation_india = 'None'

# Print results
print("People of each race:\n", race_counts)
print("Average age of men:", round(average_age_men, 1))
print("Percentage with a Bachelor's degree: {:.1f}%".format(percentage_bachelors))
print("Percentage of people with advanced education earning >50K: {:.1f}%".format(percentage_advanced_education_high_income))
print("Percentage of people without advanced education earning >50K: {:.1f}%".format(percentage_non_advanced_education_high_income))
print("Minimum number of hours worked per week:", min_hours_per_week)
print("Percentage of people who work the minimum number of hours and earn >50K: {:.1f}%".format(min_hours_salary_percentage))
print("Country with the highest percentage earning >50K:", highest_percentage_country)
print("Highest percentage earning >50K in that country: {:.1f}%".format(highest_percentage))
print("Most popular occupation for those earning >50K in India:", most_popular_occupation_india)


# In[ ]:




