#SRN: PES1UG21CS336, NAME: Miha Parveez (miha.parveez@gmail.com)
#SRN: PES2UG21CS297, NAME: Mohammed Ayman Hasib (aymanhasib33@gmail.com)
import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="select12",
        database="newproj"
    )

def add_student(first_name, last_name, phone_number, year_of_enrollment, dob, email):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = "INSERT INTO Student ( first_name, last_name, phone_number, year_of_enrollment, dob, email) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, phone_number, year_of_enrollment, dob, email)
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def add_extracurricular_activity(activity_name, description, schedule, location):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = "INSERT INTO ExtracurricularActivity (activity_name, description, schedule, location) VALUES ( %s, %s, %s, %s)"
        values = (activity_name, description, schedule, location)
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
def get_coaches():
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT Coach.*, ExtracurricularActivity.activity_name FROM Coach "
                       "LEFT JOIN ExtracurricularActivity ON Coach.activity_id = ExtracurricularActivity.activity_id")
        coaches = cursor.fetchall()
        return coaches
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
def get_teams():
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""SELECT 
    Team.team_id,
    Team.team_name,
    Team.year_formed,
    Coach.coach_id,
    ExtracurricularActivity.activity_id
FROM 
    Team
LEFT JOIN 
    ExtracurricularActivity ON Team.activity_id = ExtracurricularActivity.activity_id
LEFT JOIN 
    Coach ON Team.coach_id = Coach.coach_id;
;
""")
        teams = cursor.fetchall()
        return teams
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
def get_student_teams():
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM StudentTeam")
        student_teams = cursor.fetchall()
        return student_teams
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()            
def get_staff():
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Staff")
        staff = cursor.fetchall()
        return staff
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
def register_student_to_activity(student_id, activity_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = "INSERT INTO StudentRegistration (student_id, activity_id) VALUES (%s, %s)"
        values = (student_id, activity_id)
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_students():
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Student")
        students = cursor.fetchall()
        return students
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_extracurricular_activities():
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ExtracurricularActivity")
        activities = cursor.fetchall()
        return activities
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_registered_students(activity_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT student_id, first_name, last_name, email, phone_number
FROM Student
WHERE student_id IN (
    SELECT s.student_id
    FROM Student s
    JOIN StudentRegistration sr ON s.student_id = sr.student_id
    WHERE sr.activity_id = %s
);
        """
        cursor.execute(query, (activity_id,))
        registered_students = cursor.fetchall()
        return registered_students
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()



def add_team(team_name, year_formed, activity_id, coach_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        
        activity_id = int(activity_id)
        coach_id = int(coach_id)

        query = "INSERT INTO Team (team_name, year_formed, activity_id, coach_id) VALUES (%s, %s, %s, %s)"
        values = (team_name, year_formed, activity_id, coach_id)

        print("Executing query:", query)
        print("Query values:", values)

        cursor.execute(query, values)
        connection.commit()
        print("Team added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def add_coach(first_name, last_name, phone_number, email, activity_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = "INSERT INTO Coach (first_name, last_name, phone_number, email, activity_id) VALUES (%s, %s, %s, %s, %s)"
        values = (first_name, last_name, phone_number, email, activity_id)
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def add_staff(first_name, last_name, role, phone_number, email):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = "INSERT INTO Staff (first_name, last_name, role, phone_number, email) VALUES (%s, %s, %s, %s, %s)"
        values = (first_name, last_name, role, phone_number, email)
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def add_student_team(student_id, team_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = "INSERT INTO StudentTeam (student_id, team_id) VALUES (%s, %s)"
        values = (student_id, team_id)
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def update_student(student_id, first_name, last_name, phone_number, year_of_enrollment, dob, email):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = """
            UPDATE Student
            SET first_name=%s, last_name=%s, phone_number=%s, year_of_enrollment=%s, dob=%s, email=%s
            WHERE student_id=%s
        """
        values = (first_name, last_name, phone_number, year_of_enrollment, dob, email, student_id)
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_student(student_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = "DELETE FROM Student WHERE student_id=%s"
        cursor.execute(query, (student_id,))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def update_activity(activity_id, activity_name, description, schedule, location):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = """
            UPDATE ExtracurricularActivity
            SET activity_name=%s, description=%s, schedule=%s, location=%s
            WHERE activity_id=%s
        """
        values = (activity_name, description, schedule, location, activity_id)
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_activity(activity_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = "DELETE FROM ExtracurricularActivity WHERE activity_id=%s"
        cursor.execute(query, (activity_id,))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def update_team(team_id, team_name, year_formed, activity_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = """
            UPDATE Team
            SET team_name=%s, year_formed=%s, activity_id=%s
            WHERE team_id=%s
        """
        values = (team_name, year_formed, activity_id, team_id)
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_team(team_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = "DELETE FROM Team WHERE team_id=%s"
        cursor.execute(query, (team_id,))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()  

def update_coach(coach_id, first_name, last_name, phone_number, email, activity_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = """
            UPDATE Coach
            SET first_name=%s, last_name=%s, phone_number=%s, email=%s, activity_id=%s
            WHERE coach_id=%s
        """
        values = (first_name, last_name, phone_number, email, activity_id, coach_id)
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def delete_coach(coach_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = "DELETE FROM Coach WHERE coach_id=%s"
        cursor.execute(query, (coach_id,))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()     



def update_staff(staff_id, first_name, last_name, role, phone_number, email):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = """
            UPDATE Staff
            SET first_name=%s, last_name=%s, role=%s, phone_number=%s, email=%s
            WHERE staff_id=%s
        """
        values = (first_name, last_name, role, phone_number, email, staff_id)
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()



def delete_staff(staff_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = "DELETE FROM Staff WHERE staff_id=%s"
        cursor.execute(query, (staff_id,))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()                                                     


def count_students_function():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("SELECT CountStudents()")
        result = cursor.fetchone()
        return result[0] if result else 0
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def count_activities():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(activity_id) FROM ExtracurricularActivity")
        result = cursor.fetchone()
        return result[0] if result else 0
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

          