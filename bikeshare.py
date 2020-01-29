import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print ('Hello! Let\'s explore some US bikeshare data!')


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print ('Which city would you like to see data for? Chicago, New York City or Washington ?')
    def cityname():
        city = str(input('Enter city name :').lower())
        if city not in ('new york city', 'chicago', 'washington'):
            print ('Please select correct city among Chicago, New York City or Washington.')
            city = cityname()
        return city
    city = cityname()


    # TO DO: get user input for month (all, january, february, ... , june)

    print ('Select a month: January, February, March, April, May, June or all.')
    def monthname():
        month = str(input('Enter month :').lower())
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print ('Please select correct month among January, February, March, April, May, June or all.')
            month = monthname()
        return month
    month = monthname()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print ('Select a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all.')
    def dayname():
        day = str(input('Enter day :').lower())
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print ('Please select correct day among monday, tuesday, wednesday, thursday, friday, saturday, sunday or all.')
            day = dayname()
        return day
    day = dayname()


    print ('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


 # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable

    if month != 'all':

        # use the index of the months list to get the corresponding int

        months = [
            'january',
            'february',
            'march',
            'april',
            'may',
            'june',
            ]
        month = months.index(month) + 1

        # filter by month to create the new dataframe

        df = df[df['month'] == month]

    # filter by day of week if applicable

    if day != 'all':

        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print ('''
Calculating The Most Frequent Times of Travel...
''')
    start_time = time.time()


    # TO DO: display the most common month
    
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    common_month = df['month'].mode()[0]
    months_count = df['month'].value_counts()

    print ('The most common month is {} and count is {}.'.format(common_month,
        months_count.max()))

    # TO DO: display the most common day of week
    df['Week day'] = pd.DatetimeIndex(df['Start Time']).weekday_name
    common_day = df['Week day'].mode()[0]
    days_count = df['Week day'].value_counts()

    print ('The most common day is {} and count is {}.'.format(common_day,
        days_count.max()))

    # TO DO: display the most common start hour

    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    common_hour = df['hour'].mode()[0]
    hours_count = df['hour'].value_counts()

    print ('The most common hour is {} and count is {}.'.format(common_hour,
        hours_count.max()))
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print ('''
Calculating The Most Popular Stations and Trip...
''')
    start_time = time.time()


    # TO DO: display most commonly used start station

    start_station_count = df['Start Station'].value_counts()
    print ('The most commonly used start station is {} and count is {}.'.format(start_station_count.idxmax(),
        start_station_count.max()))

    # TO DO: display most commonly used end station

    end_station_count = df['End Station'].value_counts()
    print ('The most commonly used end station is {} and count is {}.'.format(end_station_count.idxmax(),
        end_station_count.max()))

    # TO DO: display most frequent combination of start station and end station trip

    df['Begin End stations'] = df['Start Station'] + df['End Station']
    begin_end_station = df['Begin End stations'].value_counts()

    print ('Most commonly used start station and end station is {} and count is {}.'.format(begin_end_station.idxmax(),
        begin_end_station.max()))

    print ('\nThis took %s seconds.' % (time.time() - start_time))
    print ('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print ('''
Calculating Trip Duration...
''')
    start_time = time.time()


    # TO DO: display total travel time

    travel_time_sum = df['Trip Duration'].sum()
    print ('Total travel time is {}.'.format(travel_time_sum))

    # TO DO: display mean travel time

    travel_time_mean = df['Trip Duration'].mean()
    print ('Total traveling mean time is {}.'.format(travel_time_mean))

    print ('\nThis took %s seconds.' % (time.time() - start_time))
    print ('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print ('''
Calculating User Stats...
''')
    start_time = time.time()


    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print ('Total of user types are {}.'.format(user_types))

    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        commonest_year = df['Birth Year'].mode()[0]
        print("\nThe earliest year of birth is: " + str(earliest_year))
        print("\nThe most recent year of birth is: " + str(most_recent_year))
        print("\nThe most common year of birth is: " + str(commonest_year))

    print ('\nThis took %s seconds.' % (time.time() - start_time))
    print ('-' * 40)


def raw_data(df):
    
    #capturing user input
    user_input = str(input('\nDo you want to see raw data? Reply yes or no: ').lower())
    line_number = 0
    
    while 1 == 1:
        if user_input == 'yes':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            user_input = str(input('\nDo you want to see raw data? Reply yes or no: ').lower())
        else:
            break
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = \
            input('''
Would you like to restart? Enter yes or no.
''')
        if restart.lower() != 'yes':
            break


if __name__ == '__main__':
    main()
