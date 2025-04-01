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
    

There are various functionalities for te platform: 
   To access all the endpoints for the apps ie; general endpoints, browse using this url: http://127.0.0.1:8000/api/ It gives a list of all the endpoints included in the platform

   To access users app, use the following urls whereby there are other accessible endpoints inside the users app

        To allow for login use this url: http://127.0.0.1:8000/users/login/

        To register: http://127.0.0.1:8000/users/register/

    
    The app also has dashbords that get to redirect users according to their roles. The roles are for the admin, instructor as well as the students.


    The admin has been accorded all the previledges, they can add users, lessons, courses, remove/delete users and also manage the students

    The instructor can add lessons, courses, as well as give assignments to be worked on

    The students can only read from the platform. The dashboard also gives them an opportunity to leave their opinions, improvements as well as experience they have with the platform

Each of the users have their respective dashboards: 
    Admin-dashboard url: http://127.0.0.1:8000/users/admin/dashboard/

    Instructor-dashboard url: http://127.0.0.1:8000/users/instructor/dashboard/

    Student-dashboard url: http://127.0.0.1:8000/users/student/dashboard/


In the student dashbord, there is a list of the available courses and allows for them to enroll as well as get the details of the course when they get to click on the enroll button

HANDLED APPS:
 1. users app
    This app is responsible for handling users. It is in this app that login, registartion and template display is handled

    Databases:
        The table is the user's table- It has the following records/attributes/fields:
            1. role field: This is for the various accorded roles; admin, instructor, student
            2. profile picture filed: It alllows for the users to add a profile photo for their accounts. Though it is optional to have a profile photo or not
            3. Date_of_birth: Takes the date of birth for the user

        Templates:
        There are several templates in this app:     
            1. add_user.html - Thsi is linked with the admin's dashboard where they can add users as they have overall previledges
            2. admin_dashboard.html- This template is the one that creates the frontend dashboard for the admin
            3. student_dashboard.html- The establisher of the students dashboard. It jas been linked with another template in the enrollments app
            4. instructor_dashboard.html- The builder of the instructor's dashboard in the frontend
            5. login.html- This handles the login functionality in the front end. THis is for the users that have an account in the platform
            6. register.html- Thistemplate enables the users to create an account in the platform
            7. dashbord_redirect.html- Menat for redirection. It also has the dashboard and logout redirects
    
The users have also been registered in the backend so that they can be accessed by the admins and the created superuser
        URLS:
            The urls to various pathas have been registered in the urls.py file in the users app
            It has the path to :
                a)main dashboard
                b)students dashboard-http://127.0.0.1:8000/users/student/dashboard/
                c)instructor's dashboard- http://127.0.0.1:8000/users/instructor/dashboard/
                d)admin's dashboard- http://127.0.0.1:8000/users/admin/dashboard/
                e)login- http://127.0.0.1:8000/users/login/
                f)logout
                g)register- http://127.0.0.1:8000/users/register/
                h)add user- This is under the admin's dashboard
                










2. Enrollments app
    This is the app that deals with the enrollment role for the students
     
     Database- The fields present in this app's model are:
        1. student field which is a foreign key
        2. limit choices This ensures that only the students can enroll for courses
        3. course field. It is a foreign key that relates with the course in the courses app
        enrolled at field: This keeps the record of the when the students was enrolled

    Templates
        There is an enroll_form template in this directory. It is for collecting the student information before enrolling for a particular course

    Urls
        The url paths for this app are in the urls.py file 
        It has the enrollment link that is linked with the template to allow for data collection








