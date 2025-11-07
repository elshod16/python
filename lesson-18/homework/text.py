##########1st task
df = pd.read_csv('tackoverflow_qa.csv')
df.head()
#1
df['creationdate'] = pd.to_datetime(df['creationdate'])
date_before_2024=df['creationdate']<'2024-01-01'
df[date_before_2024]
#2
quest_over_50=df['quest_rep']>50
df[quest_over_50]
#3
quest_between=df['quest_rep'].between(50,100)
df[quest_between]
#4
quest_ans=df['ans_name']=='Scott Boston'
df[quest_ans]
#5
ans_over_5=df['answercount']>5
df[ans_over_5]
#6
filtered = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'Unutbu') &
    (df['score'] < 5)
]
filtered
#7
filter=df[(df['ans_rep'].between(5,10))|
          (df['viewcount']>10000)]
filter
#8
quest_ans=df['ans_name']!='Scott Boston'
df[quest_ans]




#########2nd task

dt=pd.read_csv('titanic.csv')
dt.head()


#1
female_f=dt[
    (dt['Sex'] == 'female') &
    (dt['Pclass'] == 1) &
    (dt['Age'].between(20, 30))
]
female_f
#2
over_100=dt['Fare']>100
dt[over_100]
#3
survived_alone = dt[
    (dt['Survived'] == 1) &
    (dt['SibSp'] == 0) &
    (dt['Parch'] == 0)
]
survived_alone
#4
embarked_c_over_50 = dt[(dt['Embarked'] == 'C') & (dt['Fare'] > 50)]

#5
family_onboard = dt[(dt['SibSp'] > 0) & (dt['Parch'] > 0)]

#6
young_not_survived = dt[(dt['Age'] <= 15) & (dt['Survived'] == 0)]

#7
cabin_over_200 = dt[(dt['Cabin'].notnull()) & (dt['Fare'] > 200)]

#8
odd_passenger_id = dt[dt['PassengerId'] % 2 != 0]

#9
unique_tickets = dt[dt['Ticket'].duplicated(keep=False) == False]

#10
miss_class1 = dt[(dt['Name'].str.contains('Miss')) & (dt['Pclass'] == 1) & (dt['Sex'] == 'female')]
