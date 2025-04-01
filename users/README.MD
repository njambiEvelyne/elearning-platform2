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




3. Courses app
This is the app that I accorded the role for handling issues pertaining the courses
Courses and the lessons have been registered for accesibility in the backend
Courses can be added by an instructor who is added by the admin
The instructor takes upmthe role for adding courses ans the lessons for thecourses they'll be tutoring

Databases:
The database has three tables, that is;
    1. Course table
    This table has the following fields and their respective relationships
        1. title:Takes the title for the added course
        2. description: A textfield where a descrption on the cours is given
        3. instructor field: This is a foreign field which relates with the user's table in te users app. The relationship is meant to ensure the course is associated with the appropriate instructor
        4. created at: This field records the time a course was added in the platform

    2. Lesson table
    This is the table to handle the lessons for a particular course. Below are the fields in the table and their relationships
        1. course: This is a foreign field that uis related with the coures field in the courses table
        2. title: A textfield to add the title for the lesson that has been added 
        3. video_url: This is a URLfield where the instructor can add the url for a totour video that they have they have created. Though this field is not a must filed field, it can be left empty
        4. created-at: A date-time field that keeps the record for the time a lesson was created for eae of follow up

    3. Enrollment table
    This table is to keep tha records for those who enroll in a particular course to give them accessibility for the content. Below are the filed and thair relationships:
        1. student: A foreign key that relates with the student in the users table that is in the users app
        2. course: This is a foreign filed that relates with the course fieldin the course table in the courses app
        3. enrolled at: This is a datefield that records the time a particular student enrolled for a given course

    Templates
        The templates are meant for the formulation of the appearance of the frontend that the user interacts with
            1. Course_detail This template gives information about a particular course that a student enrolls


    URLS
        The urls for this app have been handled in urls.py in this app(courses)
        there are the routers for the lessons and the courses

    

Profile_pics
This directory keeps the profile photos that have been added by the users during the account setup

COMMON FILES IN ALL THE APPS
1. serializer.py 
    These files allow for the serialization as well as deserilization to allow for there to be API endpoints.
    Python code is converted into json format that can be hosted as a API endpoint

2. Views.py
    It is in this file that the viewsets are created

3. models.py
    These files allow for one to interact with the database as one gets to create tables as classes and the fields are reprsented as attributes for the class

4. admin.py
    It is in this file that models,/fileds are registered so that they are accessible by the superusers that are created. 
    This allows for actions to be done in the backend using the admin  dashboard

5. forms.py
    Though not compulsory, I have these files in my apps as the forms allow for data collection using the templates in the frontend and have them in the backend

6. urls.py
    This is the file in whick the url paths are registered for browsing
    There are some paths that are registered in the app, where by the app urls are added to the ain urls.py file to allow for accessiblity


THE PROJECT OVERVIEW FILES
The project directory is the elearning . It has the follolwing :

    1. Tempates diretory
        It us in this directory that i have created the base template. I have declared it a a global base template for all my templates that I have in y project

    2. Settings.py
        This is the file where i have all the installed apps for this entire project
        It also has the authentication key and the authenticared users for the project
        The templates in the various apps have been registerd in the settings.py file, eg, users/templates, enrollment/templates
        THE DATABASE THAT HAS BEEN USED IS REGISTERED IN THIS FILE. 
        For this project, I have used the db.sqlite3
        

        




 




