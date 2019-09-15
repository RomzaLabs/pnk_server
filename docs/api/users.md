# Users
Supports registering, viewing, and updating user accounts.

## Register a new user account

**Request**:

`POST` `/users/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
username   | string | Yes      | The username for the new user.
password   | string | Yes      | The password for the new user account.
first_name | string | No       | The user's given name.
last_name  | string | No       | The user's family name.
email      | string | No       | The user's email address.
user_type  | string | No       | MEM if they're a member, AFF if they're affiliates.

*Note:*

- Not Authorization Protected

**Response**:

Content-Type application/json  
201 Created  
```json
{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "username": "richard",
  "first_name": "Richard",
  "last_name": "Hendriks",
  "email": "richard@piedpiper.com",
  "auth_token": "132cf952e0165a274bf99e115ab483671b3d9ff6",
  "user_type": "AFF"
}
```

The `auth_token` returned with this response should be stored by the client for
authenticating future requests to the API. See [Authentication](authentication.md).


## Get users

**Request**:

`GET` `/users/`

Parameters:

**Response**:

Content-Type application/json  
200 OK  
```json
{
    "count": 17,
    "next": "http://localhost:8000/api/v1/missions/?page=2",
    "previous": null,
    "results": [
        {
            "id": 17,
            "name": "Test",
            "description": "Test",
            "discordURL": "https://www.google.com",
            "videoURL": "https://www.google.com",
            "category": "HUN",
            "location": "Test",
            "feature_image": "https://www.google.com",
            "mission_date": "2019-09-13T21:53:00+0000",
            "mission_status": "ACT",
            "briefing": "Briefing",
            "debriefing": "Debriefing",
            "created_at": "2019-09-14T05:29:34+0000",
            "updated_at": "2019-09-14T05:29:34+0000",
            "commander": "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
            "rsvp_users": [
                "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ],
            "attended_users": [
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ]
        },
        {
            "id": 2,
            "name": "Test",
            "description": "Test",
            "discordURL": "https://www.google.com",
            "videoURL": "https://www.google.com",
            "category": "HUN",
            "location": "Test",
            "feature_image": "https://www.google.com",
            "mission_date": "2019-09-13T21:53:00+0000",
            "mission_status": "ACT",
            "briefing": "Briefing",
            "debriefing": "Debriefing",
            "created_at": "2019-09-13T04:57:03+0000",
            "updated_at": "2019-09-13T04:57:03+0000",
            "commander": "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
            "rsvp_users": [
                "97d16898-74b2-4720-ada0-c189dde46ebc",
                "3786b93a-30ea-447a-a2b7-3bdb187ead6d"
            ],
            "attended_users": [
                "3786b93a-30ea-447a-a2b7-3bdb187ead6d"
            ]
        },
        {
            "id": 3,
            "name": "Test",
            "description": "Test",
            "discordURL": "https://www.google.com",
            "videoURL": "https://www.google.com",
            "category": "HUN",
            "location": "Test",
            "feature_image": "https://www.google.com",
            "mission_date": "2019-09-13T21:53:00+0000",
            "mission_status": "ACT",
            "briefing": "Briefing",
            "debriefing": "Debriefing",
            "created_at": "2019-09-13T04:58:19+0000",
            "updated_at": "2019-09-13T04:58:19+0000",
            "commander": "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
            "rsvp_users": [
                "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ],
            "attended_users": [
                "3786b93a-30ea-447a-a2b7-3bdb187ead6d"
            ]
        },
        {
            "id": 4,
            "name": "Test",
            "description": "Test",
            "discordURL": "https://www.google.com",
            "videoURL": "https://www.google.com",
            "category": "HUN",
            "location": "Test",
            "feature_image": "https://www.google.com",
            "mission_date": "2019-09-13T21:53:00+0000",
            "mission_status": "ACT",
            "briefing": "Briefing",
            "debriefing": "Debriefing",
            "created_at": "2019-09-13T05:22:29+0000",
            "updated_at": "2019-09-13T05:22:29+0000",
            "commander": "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
            "rsvp_users": [
                "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ],
            "attended_users": [
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ]
        },
        {
            "id": 5,
            "name": "Test",
            "description": "Test",
            "discordURL": "https://www.google.com",
            "videoURL": "https://www.google.com",
            "category": "HUN",
            "location": "Test",
            "feature_image": "https://www.google.com",
            "mission_date": "2019-09-13T21:53:00+0000",
            "mission_status": "ACT",
            "briefing": "Briefing",
            "debriefing": "Debriefing",
            "created_at": "2019-09-13T05:22:31+0000",
            "updated_at": "2019-09-13T05:22:31+0000",
            "commander": "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
            "rsvp_users": [
                "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ],
            "attended_users": [
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ]
        },
        {
            "id": 6,
            "name": "Test",
            "description": "Test",
            "discordURL": "https://www.google.com",
            "videoURL": "https://www.google.com",
            "category": "HUN",
            "location": "Test",
            "feature_image": "https://www.google.com",
            "mission_date": "2019-09-13T21:53:00+0000",
            "mission_status": "ACT",
            "briefing": "Briefing",
            "debriefing": "Debriefing",
            "created_at": "2019-09-13T05:22:40+0000",
            "updated_at": "2019-09-13T05:22:40+0000",
            "commander": "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
            "rsvp_users": [
                "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ],
            "attended_users": [
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ]
        },
        {
            "id": 7,
            "name": "Test",
            "description": "Test",
            "discordURL": "https://www.google.com",
            "videoURL": "https://www.google.com",
            "category": "HUN",
            "location": "Test",
            "feature_image": "https://www.google.com",
            "mission_date": "2019-09-13T21:53:00+0000",
            "mission_status": "ACT",
            "briefing": "Briefing",
            "debriefing": "Debriefing",
            "created_at": "2019-09-14T04:10:08+0000",
            "updated_at": "2019-09-14T04:10:08+0000",
            "commander": "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
            "rsvp_users": [
                "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ],
            "attended_users": [
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ]
        },
        {
            "id": 8,
            "name": "Test",
            "description": "Test",
            "discordURL": "https://www.google.com",
            "videoURL": "https://www.google.com",
            "category": "HUN",
            "location": "Test",
            "feature_image": "https://www.google.com",
            "mission_date": "2019-09-13T21:53:00+0000",
            "mission_status": "ACT",
            "briefing": "Briefing",
            "debriefing": "Debriefing",
            "created_at": "2019-09-14T04:13:42+0000",
            "updated_at": "2019-09-14T04:13:42+0000",
            "commander": "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
            "rsvp_users": [
                "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ],
            "attended_users": [
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ]
        },
        {
            "id": 9,
            "name": "Test",
            "description": "Test",
            "discordURL": "https://www.google.com",
            "videoURL": "https://www.google.com",
            "category": "HUN",
            "location": "Test",
            "feature_image": "https://www.google.com",
            "mission_date": "2019-09-13T21:53:00+0000",
            "mission_status": "ACT",
            "briefing": "Briefing",
            "debriefing": "Debriefing",
            "created_at": "2019-09-14T04:13:58+0000",
            "updated_at": "2019-09-14T04:13:58+0000",
            "commander": "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
            "rsvp_users": [
                "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ],
            "attended_users": [
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ]
        },
        {
            "id": 10,
            "name": "Test",
            "description": "Test",
            "discordURL": "https://www.google.com",
            "videoURL": "https://www.google.com",
            "category": "HUN",
            "location": "Test",
            "feature_image": "https://www.google.com",
            "mission_date": "2019-09-13T21:53:00+0000",
            "mission_status": "ACT",
            "briefing": "Briefing",
            "debriefing": "Debriefing",
            "created_at": "2019-09-14T04:52:56+0000",
            "updated_at": "2019-09-14T04:52:56+0000",
            "commander": "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
            "rsvp_users": [
                "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ],
            "attended_users": [
                "97d16898-74b2-4720-ada0-c189dde46ebc"
            ]
        }
    ]
}
```


## Get a user's profile information

**Request**:

`GET` `/users/:username/`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

Content-Type application/json  
200 OK  
```json
{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "username": "richard",
  "first_name": "Richard",
  "last_name": "Hendriks",
  "email": "richard@piedpiper.com",
  "user_type": "AFF"
}
```


## Update your profile information

**Request**:

`PUT/PATCH` `/users/:username/`

Parameters:

Name       | Type   | Description
-----------|--------|---
first_name | string | The first_name of the user object.
last_name  | string | The last_name of the user object.
email      | string | The user's email address.
user_type  | string | MEM if they're a member, AFF if they're affiliates.


*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

Content-Type application/json  
200 OK  
```json
{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "username": "richard",
  "first_name": "Richard",
  "last_name": "Hendriks",
  "email": "richard@piedpiper.com",
  "user_type": "AFF"
}
```
