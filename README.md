# Python-Auth-API

**[Git Hub](https://github.com/rstag/python-auth-api)**

The main purpose of this application is to provide the authentication services like OAuth, it is an authentication protocol
that allows you to approve one application interacting with another on your behalf without giving away your password
and authentication with 24 Hrs session timeout, Token Generation. 

Technology used - **python3**

Live Application - https://python-api-auth.herokuapp.com/

Authentication with 24 Hrs timeout Token Generation 

API's

|No| API | Body | Authorization | Response |
|--|------------|-------------------------------------|------------------------|----------------|
|1 | users/new | {"user":"ps","password":"rs123"} | |{"success": "user ** added"} , {"fail": "user not added"} |
|2 | login | {"user":"ps","password":"rs123"} | |{"login": "success", "auth-token": ""} , {"login": "fail"} |
|3 | profile | {"user":"ps"} | "auth-token" : "" |{"user ": u + " profile"} , {"user ": u + " unauthorized"} |
|4 | all | | |{"allusers": allusers} |
|5 | alltokens | | |{"alltokens": tokens} |
|6 | / | | |{"Read Me": "https://github.com/rstag/python-auth-api"} |
|7 | /users | {"user":"ps"} | "auth-token" : "" |{"user": ""} , {"NA"} |
