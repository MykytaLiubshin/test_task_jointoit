# Django Test Task

## Documentation

### How to start? 

You have to build images with 
* docker compose build 
After that, make sure that images are working and call
* docker compose up
, which will run the web image and the db image

### How to use it?

There is a set of endpoints, that will allow you to do certain things.
Using Postman, you can send 


#### Auth

Auth is handled at endpoints on `/auth/`

Link                            | Description                                                               | Requires Auth with JWT
------                          | --------                                                                  | -----
localhost:8000/auth/register/   | Handles user registration                                                 | No
localhost:8000/auth/login/      | Handles Login, checks the login/password and responds with a JWT token    | No
localhost:8000/auth/user/       | Handles user data retrieval, responds with id, username and email         | Yes
localhost:8000/auth/logout/     | Handles Logout, requires a valid Bearer JWT token and deletes it          | Yes


#### Events

Events is handled at endpoints on `/events/`

Link                                        | Description                           | Requires Auth with JWT
------                                      | --------                              | ----
localhost:8000/events/events/               | Handles events retrieval as a list    |   Yes
localhost:8000/events/retrieve-event/[id]   | Handles event retrieval as an entity  |   Yes
localhost:8000/events/create-event/         | Handles event creation                |   Yes
localhost:8000/events/update-event/[id]     | Handles event updates                 |   Yes
localhost:8000/events/delete-event/[id]     | Handles event deletion                |   Yes

#### Filters

On endpoint `localhost:8000/events/events/` there are the following params for filtering:

Parameter        | Description                                                                                | Example                              | Related Field 
------           | --------                                                                                   | ----                                 | ---
date__gte        | Returns Events with date greater than or equal to date in the parameter                    | `2024-05-03` , `2024-05-03T15:30:00` |   date
date__lte        | Returns Events with date less than or equal to date in the parameter                       | `2024-05-03` , `2024-05-03T15:30:00` |   date
title__iexact    | Returns Events with title that is case-insensibly exact to the title in the parameter      | `Daily Meeting`                      |   title
title__icontains | Returns Events with title that contain case-insensibly contains the title in the parameter | `Daily`                              |   title


### To stop the application

To stop the application you can use the command: 
* docker compose down
