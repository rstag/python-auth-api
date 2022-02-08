# python-auth-api

**[Git Hub](https://github.com/rstag/python-auth-api)**

https://python-api-auth.herokuapp.com/

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
