import pymysql as ms
def create_database():
    conn=ms.connect(
        host="localhost",
        user="root",
        password="bharathi"
    )
    cursor=conn.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS daily_habit_tracker")
        print("Database created")
        cursor.execute("USE daily_habit_tracker")
        cursor.execute("""CREATE TABLE IF NOT EXISTS daily_logs(
                    id int auto_increment primary key, 
                    date DATE not null,
                    mood int check(mood between 1 and 10),
                    study_hours int check(study_hours>=0),
                    sleep_hours int check(sleep_hours>=0),
                    entertainment_hours int check(entertainment_hours>=0),
                    topic varchar(250) not null)""")
        print("TABLE CREATED")
    except:
        print("Error creating Database and table")
    finally:
        conn.close()
        cursor.close()