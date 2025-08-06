
import pandas as pd


df = pd.read_csv('task\\stackoverflow_qa.csv', parse_dates=['creationdate'])


questions_before_2014 = df[df['creationdate'] < '2014-01-01']
print("1. Questions before 2014:\n", questions_before_2014)


score_above_50 = df[df['score'] > 50]
print("\n2. Score > 50:\n", score_above_50)


score_50_100 = df[(df['score'] >= 50) & (df['score'] <= 100)]
print("\n3. Score between 50 and 100:\n", score_50_100)

answered_by_scott = df[df['ans_name'] == 'Scott Boston']
print("\n4. Answered by Scott Boston:\n", answered_by_scott)


users = ['Scott Boston', 'unutbu', 'Mike Pennington', 'jezrael', 'DSM']
answered_by_5_users = df[df['ans_name'].isin(users)]
print("\n5. Answered by 5 users:\n", answered_by_5_users)

filtered = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'unutbu') &
    (df['score'] < 5)
]
print("\n6. Questions March–October 2014 by Unutbu with score < 5:\n", filtered)


score_or_views = df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]
print("\n7. Score 5-10 or views > 10000:\n", score_or_views)


not_answered_by_scott = df[df['ans_name'] != 'Scott Boston']
print("\n8. Not answered by Scott Boston:\n", not_answered_by_scott)


titanic_df = pd.read_csv("task\\titanic.csv")


female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]
print("1. Female Class 1, Age 20-30:\n", female_class1_20_30)

fare_over_100 = titanic_df[titanic_df['Fare'] > 100]
print("\n2. Fare > 100:\n", fare_over_100)


survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]
print("\n3. Survived and alone:\n", survived_alone)


embarked_C_fare_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]
print("\n4. Embarked C & Fare > 50:\n", embarked_C_fare_50)


has_family = titanic_df[
    (titanic_df['SibSp'] > 0) & (titanic_df['Parch'] > 0)
]
print("\n5. Has siblings/spouses and parents/children:\n", has_family)

under_15_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) & (titanic_df['Survived'] == 0)
]
print("\n6. Age ≤ 15 and not survived:\n", under_15_not_survived)


cabin_and_high_fare = titanic_df[
    titanic_df['Cabin'].notna() & (titanic_df['Fare'] > 200)
]
print("\n7. Cabin known and Fare > 200:\n", cabin_and_high_fare)


odd_passenger_ids = titanic_df[titanic_df['PassengerId'] % 2 == 1]
print("\n8. Odd Passenger IDs:\n", odd_passenger_ids)

ticket_counts = titanic_df['Ticket'].value_counts()
unique_tickets = ticket_counts[ticket_counts == 1].index
unique_ticket_df = titanic_df[titanic_df['Ticket'].isin(unique_tickets)]
print("\n9. Unique tickets:\n", unique_ticket_df)

# 10. 'Miss' в имени и класс 1
miss_in_class1 = titanic_df[
    (titanic_df['Name'].str.contains('Miss')) & (titanic_df['Pclass'] == 1)
]
print("\n10. 'Miss' in name and Class 1:\n", miss_in_class1)
