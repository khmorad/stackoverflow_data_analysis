import pandas as pd
import numpy as np

#reding both schema and initial stackoverflow datafram
na_vals = ['NA', 'Missing']
df = pd.read_csv("stack-overflow-developer-survey-2023/survey_results_public.csv", na_values = na_vals)
schema_df = pd.read_csv('stack-overflow-developer-survey-2023/survey_results_schema.csv',index_col='qname')

#getting basic information of data fram (mean, standard dev,min, three Quartiles, and max)
df.describe()

#table contains 89184 rows and 84 columns
df.shape

#getting info on table
df.info()

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

#display only the first 7 column of the schema data frame
schema_df.head(7)

schema_df =schema_df[['question']]

#getting the data form row language and question column
#it should be noted that schema_df tends to contain the schema for the actual data frame
schema_df.loc['Language','question']

df['Age'].value_counts()

df.loc[0:28, 'Age':'CodingActivities']

df.head()

#making the response Id the actual index of the dataframe
df = df.set_index("ResponseId")

#sorting the index in decending order
schema_df.sort_index(ascending=False).head(7)

#checking salary of individuals based on age and diplaying only age, employment, and yearly salary
filt = (df['ConvertedCompYearly'] >= 100000)
check_salary = df.loc[filt, ['Age', 'Employment', 'ConvertedCompYearly']]

#changing the column name for a better presentation
df.rename(columns={'ConvertedCompYearly':'yearlySalary'}, inplace = True)

#changing the SurveyEase column for better undrestanding of the columns
df = df.rename(columns={'SurveyEase':'survayDifficulty'})

#creating a filter which will only include the ones the mention the difficulty was easy
filt = (df['survayDifficulty'] == 'Easy')

#sorting the dataframe by yearly salary in descending order
df.sort_values(by='yearlySalary' ,ascending= False).head()


#checking the total number of people that use react
filt = df['WebframeWantToWorkWith'].str.contains('React', na=False)
filt.sum()

#locationg the United States in Country column then displaying the age column
df.loc[df['Country'] == 'United States of America']['Age']

#returning a series with multiple indexes
#if needed to grab data of certain country
#countryGroup['yearlySalary'].value_counts().loc['India']
countryGroup = df.groupby(['Country'])
countryGroup['yearlySalary'].value_counts().loc['India']

# median, and mean yearly salary for each country using aggregation (experiment)
# in order to access certain country simply add .loc['country name'] to the end of the code below
# ex: countryGroup['yearlySalary'].agg(['median', 'mean']).loc['United States of America']
# median yearly salary in America is 150000.0
countryGroup['yearlySalary'].agg(['median', 'mean'])

#how many in each country know how to use python (experiment)
countryRef = df.groupby(['Country'])

#this is no longet just a series and its a series groupby which .appy() is used in this case
countryRef['LanguageHaveWorkedWith'].apply(lambda x: x.str.contains('Python', na=False).value_counts().sum())


#finding the percentage of respondends that use python in each country (experiment)

#getting the total value of respondents for each country
country_total_responds = df['Country'].value_counts()

#getting the total value of respondents that use python in each country
country_total_python_use = countryRef['LanguageHaveWorkedWith'].apply(lambda x: x.str.contains('Python').sum())

#using concatination to concatinate the two series together (COLUMN: countries, ROW: total respondsnt, and the ones that use python)
python_df = pd.concat([country_total_responds, country_total_python_use],  axis = 'columns', sort=False)

#changing the column names for better presentation and undrestanding of the data frame
python_df.rename(columns={'count':'totalRespondents','LanguageHaveWorkedWith':'usePython'}, inplace=True)
python_df['pctKnowsPython'] = (python_df['usePython']/python_df['totalRespondents'])*100

#displaying the actual percentage
python_df['pctKnowsPython'] = python_df['pctKnowsPython'].apply(lambda x: f"{x:.2f}%")

#snippet of percentage of respondends that use python in each country
python_df.iloc[18: 24]

python_df['pctKnowsPython'].sort_values(ascending = False)

python_df.sort_values(by= 'pctKnowsPython', ascending = False).head()

#displaying the information on Japan
python_df.loc['Japan']

#seeing what data type this data frame tends to have
df.dtypes.value_counts()

#all th eunique numbers of column
df['YearsCode'].unique()

#displaye the median of years (experiment)
#the dataframe tends to include some strings which needs to be replace with a number
df['YearsCode'].replace('Less than 1 year', 0, inplace = True)
df['YearsCode'].replace('More than 50 years', 51, inplace = True)

#now changing the date type to float
df['YearsCode'] = df['YearsCode'].astype(float)
df['YearsCode'].median()

#diplaying the median
df['YearsCode'].mean()
