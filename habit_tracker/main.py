import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import track_habit, Habit 


def main():
    habits = [track_habit('Coffee', datetime(2024,7,12), cost=10, minutes_used=10),
              track_habit('Being lazy', datetime(2024, 6, 24, 10), cost=1, minutes_used=60)]
    

    df = pd.DataFrame(habits)

    print(tabulate(df, headers='keys', tablefmt='psql'))


if __name__ == '__main__':
    main()