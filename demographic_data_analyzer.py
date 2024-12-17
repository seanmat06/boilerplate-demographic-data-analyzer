import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    ###
    # -- How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    ###
    # -- What is the average age of men?
    # Populate variable with all Males
    men_data = df[df['sex'] == 'Male']
    #Calculate average age of men
    average_age_men = round(men_data['age'].mean(),1)

    ###
    # -- What is the percentage of people who have a Bachelor's degree?
    # Find total people in dataset
    total_people = len(df)
    # Populate variable with bachelors owners
    bachelors_owners = df[df['education'] == 'Bachelors']
    # Count bachelors owners
    bachelors_index = len(bachelors_owners)
    # Find the percentage of bachelors owners
    percentage_bachelors = round((bachelors_index/total_people) * 100,1)

    ###
    #  -- What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # Populate variable with Advanced Education Types
    advanced_education = ['Bachelors','Masters','Doctorate']
    # Fill var with all users who have advaced Education
    advanced_education_data = df[df['education'].isin(advanced_education)]
    # Calculate the total number of people with advanced edication
    total_advanced_education = len(advanced_education_data)
    # Figure out how many of the advanced education people make over 50K
    advanced_high_income_data = advanced_education_data[advanced_education_data['salary'] == '>50K']
    # Calculate the length of advanced education users making over 50K
    advanced_over_50k = len(advanced_high_income_data)

    ###
    # -- What percentage of people without advanced education make more than 50K?
    # Fill var with all users who do not have higher education
    low_education_data = df[~df['education'].isin(advanced_education)]
    # Calculate length of all users with low education
    total_low_education = len(low_education_data)
    # Calculate users with lower education that make over 50K
    low_high_income_data = low_education_data[low_education_data['salary'] == '>50K']
    # Calculate how many people are in the list of users with low education who make over 50K
    low_over_50k = len(low_high_income_data)

    # Percentage with salary >50K with High Education
    higher_education_rich = round((advanced_over_50k / total_advanced_education) * 100,1)
    # Percentage with salary >50K with Low Education
    lower_education_rich = round((low_over_50k / total_low_education) * 100,1)

    ###
    # -- What is the minimum number of hours a person works per week (hours-per-week feature)?
    # Calculate the minimum hours a week a person can work
    min_work_hours = df['hours-per-week'].min()

    ###
    # -- What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # Filling var with the people work the minimum number of hours
    total_minimum_hour_workers = df[df['hours-per-week'] == min_work_hours]
    # Calculate how many of the minimum workers make over 50K
    salary_over_50k = total_minimum_hour_workers[total_minimum_hour_workers['salary'] == '>50K'].shape[0]
    # Calculating how many people work minimum number of hours
    total_min_hours = total_minimum_hour_workers.shape[0]
    # If-Else to make sure there is at least 1 person working the minimum number of hours,
    #   then calculating percentage to see how many people work minimum hours and make over 50K
    if total_min_hours > 0:
        rich_percentage =round((salary_over_50k / total_min_hours) * 100,1)
    else:
        rich_percentage = 0

    ###
    # -- What country has the highest percentage of people that earn >50K?
    # Filling var with all people who make over 50K
    over_50k = df[df['salary'] == '>50K']
    # Finding out how many unique countries there are and how many people belong to each
    country_groups = df['native-country'].value_counts()
    # Finding out how many people in each unique country make over 50K
    country_over_50k = over_50k['native-country'].value_counts()
    # Percentage of people in each country who make over 50K
    percentage_by_country = (country_over_50k / country_groups) * 100
    # What country has the highest percentage of people making over 50K
    highest_earning_country = percentage_by_country.idxmax()
    # What is the percentage of people in the above country who make over 50K
    highest_earning_country_percentage = round(percentage_by_country.max(),1)

    ###
    # -- Identify the most popular occupation for those who earn >50K in India.
    # What percentage of people make over 50K in India
    indian_high_earners = over_50k[over_50k['native-country'] == 'India']
    # What is the most popular occupation in India for people who make over 50K
    top_IN_occupation = indian_high_earners['occupation'].value_counts().idxmax()
    # How many people in India work the most popular job making over 50K
    number_top_occupation = indian_high_earners['occupation'].value_counts().max()
    

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
