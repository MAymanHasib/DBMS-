#SRN: PES2UG21CS297, NAME: Mohammed Ayman Hasib (aymanhasib33@gmail.com)
#SRN: PES1UG21CS336, NAME: Miha Parveez (miha.parveez@gmail.com)
import streamlit as st
import pandas as pd
from back import (
    connect_to_database,
    add_student,
    add_extracurricular_activity,
    update_student,
    delete_student,
    register_student_to_activity,
    get_students,
    get_extracurricular_activities,
    add_student_team,
    add_staff,
    add_coach,
    add_team,
    get_registered_students,
    get_coaches,
    get_teams,
    get_staff,
    get_student_teams,
    update_activity,
    delete_activity,
    delete_team,
    update_team,
    update_coach,
    delete_coach,
    update_staff,
    delete_staff,
    count_students_function,
    count_activities
)


# Define user roles
ROLES = ["Student", "Coach", "Staff", "Admin"]


def set_user_role(role):
    st.session_state.user_role = role


def is_user_logged_in():
    return "user_role" in st.session_state


def is_user_admin():
    return is_user_logged_in() and st.session_state.user_role == "Admin"


def is_user_student():
    return is_user_logged_in() and st.session_state.user_role == "Student"


def is_user_coach():
    return is_user_logged_in() and st.session_state.user_role == "Coach"


def is_user_staff():
    return is_user_logged_in() and st.session_state.user_role == "Staff"

def home_page():
    st.title("⚽️🏈🏐🏉🏏🎱🏓🥎🏸🏋🏽‍♀️🤺🏀🎾")
    st.write("Welcome to Sportsync! This is the University Extracurricular Activities Database For PES University.")
    


def login_form():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        
        if username == "student" and password == "student":
            set_user_role("Student")
            st.success("Login successful!")
        elif username == "coach" and password == "coach":
            set_user_role("Coach")
            st.success("Login successful!")
        elif username == "staff" and password == "staff":
            set_user_role("Staff")
            st.success("Login successful!")
        elif username == "admin" and password == "admin":
            set_user_role("Admin")
            st.success("Login successful!")
        else:
            st.error("Invalid credentials. Please try again.")

def add_student_form():
    st.subheader("Add a New Student")

    if is_user_student():
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        phone_number = st.text_input("Phone Number")
        year_of_enrollment = st.number_input("Year of Enrollment", min_value=1900, max_value=2100, step=1)
        dob = st.date_input("Date of Birth")
        email = st.text_input("Email")

        if st.button("Add Student"):
            add_student(first_name, last_name, phone_number, year_of_enrollment, dob, email)
            st.success("Student added successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def add_extracurricular_activity_form():
    st.subheader("Add a New Extracurricular Activity")

    
    activity_name = st.text_input("Activity Name")
    description = st.text_area("Description")
    schedule = st.text_input("Schedule")
    location = st.text_input("Location")

    if st.button("Add Activity"):
        
        add_extracurricular_activity(activity_name, description, schedule, location)
        st.success("Activity added successfully!")

def update_student_form():
    st.subheader("Update Student Information")

    if is_user_admin():
        student_id = st.text_input("Student ID")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        phone_number = st.text_input("Phone Number")
        year_of_enrollment = st.number_input("Year of Enrollment", min_value=1900, max_value=2100, step=1)
        dob = st.date_input("Date of Birth")
        email = st.text_input("Email")

        if st.button("Update Student"):
            update_student(student_id, first_name, last_name, phone_number, year_of_enrollment, dob, email)
            st.success("Student information updated successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def delete_student_form():
    st.subheader("Delete Student")

    if is_user_admin():
        student_id = st.text_input("Student ID")

        if st.button("Delete Student"):
            delete_student(student_id)
            st.success("Student deleted successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")



def update_team_form():
    st.subheader("Update Team Information")

    if is_user_admin():
        team_id = st.text_input("Team ID")
        team_name = st.text_input("Team Name")
        year_formed = st.number_input("Year Formed", min_value=1900, max_value=2100, step=1)
        activity_id = st.text_input("Activity ID")

        if st.button("Update Team"):
            update_team(team_id, team_name, year_formed, activity_id)
            st.success("Team information updated successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def delete_team_form():
    st.subheader("Delete Team")

    if is_user_admin():
        team_id = st.text_input("Team ID")

        if st.button("Delete Team"):
            delete_team(team_id)
            st.success("Team deleted successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")


def register_student_form():
    st.subheader("Register for an Extracurricular Activity")

    
    student_id = st.text_input("Student ID")

    if is_user_student() and student_id:
        activities = get_extracurricular_activities()
        activity_options = {f"{activity['activity_id']} - {activity['activity_name']}": activity['activity_id'] for activity in activities}
        selected_activity = st.selectbox("Select Activity", list(activity_options.keys()))

        if st.button("Register"):
            activity_id = activity_options[selected_activity]
            register_student_to_activity(student_id, activity_id)
            st.success("Registration successful!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")



def update_activity_form():
    st.subheader("Update Extracurricular Activity")

    if is_user_admin():
        activity_id = st.text_input("Activity ID")
        activity_name = st.text_input("Activity Name")
        description = st.text_area("Description")
        schedule = st.text_input("Schedule")
        location = st.text_input("Location")

        if st.button("Update Activity"):
            update_activity(activity_id, activity_name, description, schedule, location)
            st.success("Extracurricular Activity updated successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def delete_activity_form():
    st.subheader("Delete Extracurricular Activity")

    if is_user_admin():
        activity_id = st.text_input("Activity ID")

        if st.button("Delete Activity"):
            delete_activity(activity_id)
            st.success("Extracurricular Activity deleted successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def view_registered_students():
    st.subheader("View Registered Students")

    if is_user_admin():
        activities = get_extracurricular_activities()
        activity_options = {f"{activity['activity_id']} - {activity['activity_name']}": activity['activity_id'] for activity in activities}
        selected_activity = st.selectbox("Select Activity", list(activity_options.keys()))

        if st.button("View Registered Students"):
            activity_id = activity_options[selected_activity]
            registered_students = get_registered_students(activity_id)

            if registered_students:
                df = pd.DataFrame(registered_students, columns=(['student_id']))
                st.table(df)
            else:
                st.warning("No students registered for this activity.")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def display_students():
    st.subheader("View Students")

    students = get_students()
    if students:
        df = pd.DataFrame(students, columns=['student_id', 'first_name', 'last_name', 'phone_number', 'year_of_enrollment', 'dob', 'email'])
        st.table(df)
    else:
        st.warning("No students found.")

def display_extracurricular_activities():
    st.subheader("View Extracurricular Activities")

    activities = get_extracurricular_activities()
    if activities:
        df = pd.DataFrame(activities, columns=['activity_id', 'activity_name', 'description', 'schedule', 'location'])
        st.table(df)
    else:
        st.warning("No extracurricular activities found.")

def display_coaches():
    st.subheader("View Coaches")

    coaches = get_coaches()
    if coaches:
        df = pd.DataFrame(coaches, columns=['coach_id', 'first_name', 'last_name', 'phone_number', 'email', 'activity_id'])
        st.table(df)
    else:
        st.warning("No coaches found.")

def display_teams():
    st.subheader("View Teams")

    teams = get_teams()
    if teams:
        df = pd.DataFrame(teams, columns=['team_id', 'team_name', 'year_formed', 'activity_id', 'coach_id'])
        st.table(df)
    else:
        st.warning("No teams found.")

def display_staff():
    st.subheader("View Staff")

    staff = get_staff()
    if staff:
        df = pd.DataFrame(staff, columns=['staff_id', 'first_name', 'last_name', 'role', 'email', 'phone_number'])
        st.table(df)
    else:
        st.warning("No staff found.")

def display_student_teams():
    st.subheader("View Student Teams")

    student_teams = get_student_teams()
    if student_teams:
        df = pd.DataFrame(student_teams, columns=['student_id', 'team_id'])
        st.table(df)
    else:
        st.warning("No student teams found.")

def add_team_form():
    st.subheader("Add Team")

    if is_user_admin():
        team_name = st.text_input("Team Name")
        year_formed = st.number_input("Year Formed", min_value=1900, max_value=2100, step=1)
        activity_id = st.text_input("Activity ID")
        coach_id = st.text_input("Coach ID")

        if st.button("Add Team"):
            add_team(team_name, year_formed, activity_id, coach_id)
            st.success("Team added successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def add_coach_form():
    st.subheader("Add Coach")

    if is_user_coach():
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        phone_number = st.text_input("Phone Number")
        email = st.text_input("Email")
        activity_id = st.text_input("Activity ID")

        if st.button("Add Coach"):
            add_coach(first_name, last_name, phone_number, email, activity_id)
            st.success("Coach added successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def add_staff_form():
    st.subheader("Add Staff")

    if is_user_staff():
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        role = st.text_input("Role")
        phone_number = st.text_input("Phone Number")
        email = st.text_input("Email")
        

        if st.button("Add Staff"):
            add_staff(first_name, last_name, role, phone_number, email)
            st.success("Staff member added successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def add_student_team_form():
    st.subheader("Add Student to Team")

    if is_user_admin():
        student_id = st.text_input("Student ID")
        team_id = st.text_input("Team ID")

        if st.button("Add Student to Team"):
            add_student_team(student_id, team_id)
            st.success("Student added to team successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def update_coach_form():
    st.subheader("Update Coach Information")

    if is_user_admin():
        coach_id = st.text_input("Coach ID")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        phone_number = st.text_input("Phone Number")
        email = st.text_input("Email")
        activity_id = st.text_input("Activity ID")

        if st.button("Update Coach"):
            update_coach(coach_id, first_name, last_name, phone_number, email, activity_id)
            st.success("Coach information updated successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def delete_coach_form():
    st.subheader("Delete Coach")

    if is_user_admin():
        coach_id = st.text_input("Coach ID")

        if st.button("Delete Coach"):
            delete_coach(coach_id)
            st.success("Coach deleted successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def update_staff_form():
    st.subheader("Update Staff Information")

    if is_user_admin():
        staff_id = st.text_input("Staff ID")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        role = st.text_input("Role")
        phone_number = st.text_input("Phone Number")
        email = st.text_input("Email")
        

        if st.button("Update Staff"):
            update_staff(staff_id, first_name, last_name, role, phone_number, email)
            st.success("Staff information updated successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def delete_staff_form():
    st.subheader("Delete Staff")

    if is_user_admin():
        staff_id = st.text_input("Staff ID")

        if st.button("Delete Staff"):
            delete_staff(staff_id)
            st.success("Staff deleted successfully!")
    else:
        st.warning("Access denied. You don't have permission to perform this action.")

def display_student_count():
    st.subheader("Student Count")

    if is_user_admin() or is_user_staff():
        total_students = count_students_function()
        st.write(f"Total Students: {total_students}")
    else:
        st.warning("Access denied. You don't have permission to view student count.")

def display_activity_count():
    st.subheader("Activity Count")

    activity_count = count_activities()
    st.write(f"Total Activities: {activity_count}")







st.set_page_config(page_title="Sportsync⚽️", page_icon=":⚽️:")  

st.title("Sportsync: University Extracurricular Activities Database")


if not is_user_logged_in():
    login_form()
else:
    
    menu = ["Home", "Add Student", "Add Extracurricular Activity", "Register Student", "View Students", "View Extracurricular Activities", "View Registered Students", "View Coaches", "View Teams", "View Staff", "View Student Teams","Delete Student","update Student","update activity","delete activity","delete team","update team","add student team","add staff","add team","add coach","update coach","delete coach","update staff","delete staff","student count","activity count"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        home_page()

    elif choice == "Add Student":
        add_student_form()

    elif choice == "Add Extracurricular Activity":
        add_extracurricular_activity_form()

    elif choice == "Register Student":
        register_student_form()

    elif choice == "View Students":
        display_students()

    elif choice == "View Extracurricular Activities":
        display_extracurricular_activities()

    elif choice == "View Registered Students":
        view_registered_students()

    elif choice == "View Coaches":
        display_coaches()

    elif choice == "View Teams":
        display_teams()

    elif choice == "View Staff":
        display_staff()

    elif choice == "View Student Teams":
        display_student_teams()

    elif choice == "Delete Student":
        delete_student_form()

    elif choice == "update Student":
        update_student_form()  

    elif choice == "update activity":
        update_activity_form()


    elif choice == "delete activity":
        delete_activity_form()  

    elif choice == "delete team":
        delete_team_form()

    elif choice == "update team":
        update_team_form()
   
    elif choice == "add coach":
        add_coach_form()
    
    elif choice == "add team":      
        add_team_form()
    
    elif choice == "add staff":      
        add_staff_form()
    
    elif choice == "add student team":     
        add_student_team_form()

    elif choice == "update coach":
        update_coach_form()

    elif choice == "delete coach":
        delete_coach_form()

    elif choice == "update staff":
        update_staff_form()

    elif choice == "delete staff":
        delete_staff_form()



    elif choice == "student count":
        display_student_count()


    elif choice == "activity count":
        display_activity_count()



   


    