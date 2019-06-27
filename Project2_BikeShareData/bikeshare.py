import time
import calendar
import pandas as pd

city_data = {
    'chicago': 'chicago.csv',
    'new york': 'new_york_city.csv',
    'washington': 'washington.csv'
}

filter_choices = ("none", "month", "day", "both")

months_dict = {}
for month_index in range(1, 7):
    months_dict[month_index] = calendar.month_name[
        month_index].lower()

days_dict = {}  # 1 = sunday
for days_index in range(0, 7):
    days_dict[days_index] = \
        calendar.day_name[days_index].lower()


def get_filters():
    filtr = 'none'
    month = day = 'all'
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to
                    apply no month filter
        (str) day - name of the day of week to filter by, or "all"
                    to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for '
                     'Chicago, '
                     'New York or '
                     'Washington?\n')
        if city.lower() not in city_data.keys():
            print('Invalid input for city. Please try again')
            continue
        else:
            break

    # get the filter specification from user
    while True:
        filtr = input(
            'Would you like to filter the data by month, day, '
            'both or not at all? Type "none" for no time filter.\n')
        if filtr.lower() not in filter_choices:
            print('Invalid input for filter. Please try again')
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while filtr == 'month' or filtr == 'both':
        month = input(f"Which month to choose from: "
                      f"{list(months_dict.values())}?\n")
        if month.lower() not in months_dict.values():
            print('Invalid input for month. Please try again. Make '
                  'sure you choose from first six months of a year.')
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ..sunday)
    while filtr == 'day' or filtr == 'both':
        day = input(f"Which day? Please write response as integer. "
                    f"0=monday.....6=sunday\n")
        try:
            day = int(day)
            if day not in days_dict.keys():
                raise Exception("days not found from choice list")
            else:
                break
        except Exception as msg:
            print(msg)
            print('Invalid input for day. Please try again')
            continue

    print('-' * 40)
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
    # get the unfiltered df first
    raw_city_df = pd.read_csv(city_data.get(city))

    # convert the start time column to a date time object
    raw_city_df['Start Time'] = \
        pd.to_datetime(raw_city_df['Start Time'])

    # create a month column
    raw_city_df.insert(2, 'start_month',
                       raw_city_df['Start Time']
                       .dt.month_name())
    # create a weekday column
    raw_city_df.insert(3,
                       'start_day',
                       raw_city_df['Start Time']
                       .dt.weekday)
    raw_city_df['start_month'] = \
        raw_city_df['start_month'].apply(lambda mnth: mnth.lower())

    if month != 'all':
        raw_city_df = \
            raw_city_df[(raw_city_df['start_month'] == month)]
    if day != 'all':
        raw_city_df = \
            raw_city_df[(raw_city_df['start_day'] == day)]

    return raw_city_df


def time_stats(df: pd.DataFrame):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['start_month'].mode().iloc[0]
    df_with_common_month = df[df['start_month'] == most_common_month]
    total_occurances = df_with_common_month['start_month'].count()
    print(f"The most common month of travel is: {most_common_month}"
          f" and it occurs {total_occurances} times")

    # display the most common day of week
    most_common_day = df['start_day'].mode().iloc[0]
    df_with_common_day = df[df['start_day'] == most_common_day]
    total_occurances = df_with_common_day['start_day'].count()
    print(f"The most common day of travel is:"
          f" {days_dict[most_common_day]}"
          f" and it occurs {total_occurances} times")
    # display the most common start hour
    most_common_hr = df['Start Time'].dt.hour.mode().iloc[0]
    print(
        f"The most common Start Hour of travel is: {most_common_hr}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df: pd.DataFrame):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = \
        df['Start Station'].mode().iloc[0]
    print(f"The most commonly used Start Station is: "
          f"{most_common_start_station}")

    # display most commonly used end station
    most_common_end_station = \
        df['End Station'].mode().iloc[0]
    print(f"The most commonly used End Station is: "
          f"{most_common_end_station}")

    # display most frequent combination of start station and end
    # station trip. Lets create a combo column
    most_common_station_combination = \
        (df['Start Station'] + ":" + df['End Station']).mode().iloc[0]
    print(f"The most common Start : End Station combinations are: "
          f"{most_common_station_combination}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df: pd.DataFrame):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print(f"Total travel time is: {total_trip_duration}")

    # display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print(f"The mean trip duration is: {mean_trip_duration: 0.2f}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df: pd.DataFrame):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The different counts of users are: ")
    print(user_types)
    print()

    # Display counts of gender - only for NYC/Chicago
    try:
        gender_types = df['Gender'].value_counts()
        print("The different counts of gender are: ")
        print(gender_types)
        print()

        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode().iloc[0]

        print(f"Earliest birth year: {earliest_birth_year: 0.0f}")
        print(f"Recent birth year: {recent_birth_year: 0.0f}")
        print(f"Most common birth year: {common_birth_year: 0.0f}")

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)
    except Exception as msg:
        print("This dataframe has no Gender or Birth Year related "
              "information.")
        print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input(
            '\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
