import time
import pandas as pd
import numpy as np
import datetime as dt
import math

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago','new york city','washington']
    city = " "
    while city.lower() not in cities:
        city = input("enter a city: ")
    city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january','february','march','april','may','june']
    month = " "
    while month.lower() not in months :
        month = input("enter a month: ")
    month = month.lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    weekdays = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = " "
    while day.lower() not in weekdays:
        day = input("enter a weekday: ")
    day = day.lower()
    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].value_counts().idxmax()
    print("Most common month: ", popular_month)
    
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name                            
    popular_weekday = df['day_of_week'].value_counts().idxmax()
    print("Most common day of week: ", popular_weekday)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    print("Most common Start Hour: ", popular_hour)                                                                         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print("Most commonly used Start Station: ", popular_start_station)
                                         
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print("Most commonly used End Station: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print("Most frequent combination of Start Station and End Station trip: ", popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print("Total travel time(in seconds): ", travel_time) 
    # TO DO: display mean travel time
    mean_travel_time = travel_time/len(df['Trip Duration'])
    print("Mean travel time: ", mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User types count: ", df['User Type'].value_counts())
    
    if 'Gender' in df:
    # TO DO: Display counts of gender
        print("Male count: ", df['Gender'].value_counts()['Male'])
        print("Female count: ", df['Gender'].value_counts()['Female'])

    # TO DO: Display earliest, most recent, and most common year of birth           
        df['year1'] = df['Birth Year']
        print("Earliest year: ",df['year1'].min())
        print("Most recent year: ",df['year1'].max())
        popular_year1 = df['year1'].value_counts().idxmax()
        print("Most common year of birth: ", popular_year1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
        """" displays 5 rows of individual trip data.""""
        
    display_trip = input("Do you wish to see 5 rows of individual trip data? ")
    start_loc = 0
    while display_trip == 'yes' :
        print(df.iloc[start_loc:start_loc + 5])
        start_loc = start_loc + 5
        display_trip = input("do you wish to continue? ").lower()
 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
