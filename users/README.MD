The project starts by cerating the elearning platform folder.
Move to the folder and open the terminal and start by using the:
 pip install pipenv to create a virtual environment
 Use the pipenev startproject project_name to start the project
 Use manage.py to start the necessary apps for the project

This elearning platform has six installed apps : 
    courses: This app stores the courses that are offered in an institution. The courses are stored in the database.

    enrollments: This app is meant to ensure the record for the enrolled students is well stored. It is in this app that instructores have to enroll into the institution's system as instructors

    progress: This app keeps the record for how content coverage is done. It keeps track of the lessons, quizzes, as well as the grades scored and the total average for an entire academic year

    quizzes: This is an applicaton enables the instructors to add quizzes as well as asignments for content covered. It also allows for students get access to the uploaded assignment and do the assignment

    users: This app keeps the record for all students as well as the instructors. This is the app will have the authentication roles. If an individual is authorised, they will have access to the platform, otherwise, they get restricted from accessing the platform

The root api endpoints have been set up and are well running. The endpoints are : 
    users endpoint
    courses endpoint
    lessons endpoint
    enrollments endpoint
    progress endpoints
    quizzes endpoint
    questions endpoint
    submissions endpoint
    answer's endpoint
    

