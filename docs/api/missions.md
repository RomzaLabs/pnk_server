# Missions
Supports adding, viewing, and updating missions.

## Get Mission List

**Request**:  

`GET` `/missions/`

Parameters:  

**Response**:  

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

## Get a Mission

**Request**:

`GET` `/missions/:missionId/`

Parameters:

**Response**:

```json
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
    "updated_at": "2019-09-15T00:17:36+0000",
    "commander": "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
    "rsvp_users": [
        "229a5948-c5a3-4e1f-a075-24bb553335a9",
        "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
        "97d16898-74b2-4720-ada0-c189dde46ebc",
        "61c1fc24-73cb-41f2-9899-d44a1b2bdd54"
    ],
    "attended_users": [
        "97d16898-74b2-4720-ada0-c189dde46ebc"
    ]
}
```

## Create a Mission

**Request**:

`POST` `/missions/`

Parameters:

Name           | Type   | Required | Description
---------------|--------|----------|------------
name           | string | Yes      | The name of the mission.
description    | string | Yes      | The description for the mission.
location       | string | Yes      | The location of the mission.
mission_date   | string | Yes      | The date of the mission with timezone e.g. 2019-09-13T04:57:03+0000.
commander      | string | Yes      | The UUID of the commander for this mission.
discordURL     | string | No       | Link to discord URL.
videoURL       | string | No       | Link to stream or video URL.
discordURL     | string | No       | Link to discord URL if possible.
category       | string | No       | Category choice.
discordURL     | string | No       | Link to discord URL if possible.
feature_image  | string | No       | Link to image.
mission_status | string | No       | ACT, SUC, or FAI
briefing       | string | No       | Mission briefing.
debriefing     | string | No       | Mission debriefing.
created_at     | date   | No       | The date the mission was created e.g. 2019-09-13T04:57:03+0000.
updated_at     | date   | No       | The date the mission was created e.g. 2019-09-13T04:57:03+0000.
rsvp_users     | array  | No       | An array of UUIDs for the RSVP users.
attended_users | array  | No       | An array of UUIDs for the attended users.

*Note:*

- Authorization Protected. Only PNK Members can create missions.

**Response**:

Content-Type application/json  
201 Created  
```json
{
    "id": 20,
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
    "created_at": "2019-09-15T04:02:45+0000",
    "updated_at": "2019-09-15T04:02:45+0000",
    "commander": "ad0f43ea-8e30-4ba9-9ee3-56398fdec759",
    "rsvp_users": [
        "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
        "97d16898-74b2-4720-ada0-c189dde46ebc"
    ],
    "attended_users": [
        "97d16898-74b2-4720-ada0-c189dde46ebc"
    ]
}
```


## Update mission

**Request**:

`PATCH` `/missions/:missionId/`

Parameters:

Name           | Type   | Required | Description
---------------|--------|----------|------------
name           | string | Yes      | The name of the mission.
description    | string | Yes      | The description for the mission.
location       | string | Yes      | The location of the mission.
mission_date   | string | Yes      | The date of the mission with timezone e.g. 2019-09-13T04:57:03+0000.
commander      | string | Yes      | The UUID of the commander for this mission.
discordURL     | string | No       | Link to discord URL.
videoURL       | string | No       | Link to stream or video URL.
discordURL     | string | No       | Link to discord URL if possible.
category       | string | No       | Category choice.
discordURL     | string | No       | Link to discord URL if possible.
feature_image  | string | No       | Link to image.
mission_status | string | No       | ACT, SUC, or FAI
briefing       | string | No       | Mission briefing.
debriefing     | string | No       | Mission debriefing.
created_at     | date   | No       | The date the mission was created e.g. 2019-09-13T04:57:03+0000.
updated_at     | date   | No       | The date the mission was created e.g. 2019-09-13T04:57:03+0000.
rsvp_users     | array  | No       | An array of UUIDs for the RSVP users.
attended_users | array  | No       | An array of UUIDs for the attended users.

**Response**:

Content-Type application/json  
200 OK  
```json
{
    "id": 20,
    "name": "Test",
    "description": "Test",
    "discordURL": "https://www.google.com",
    "videoURL": "https://www.google.com",
    "category": "HUN",
    "location": "Test",
    "feature_image": "https://www.google.com",
    "mission_date": "2019-09-13T21:53:00+0000",
    "mission_status": "ACT",
    "briefing": "Even longer briefing",
    "debriefing": "Debriefing",
    "created_at": "2019-09-15T04:02:45+0000",
    "updated_at": "2019-09-15T04:03:19+0000",
    "commander": "ad0f43ea-8e30-4ba9-9ee3-56398fdec759",
    "rsvp_users": [
        "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
        "97d16898-74b2-4720-ada0-c189dde46ebc"
    ],
    "attended_users": [
        "97d16898-74b2-4720-ada0-c189dde46ebc"
    ]
}
```

*Note:*

- Authorization Protected. Only the mission commander can update a mission.


## Delete a mission

**Request**:

`PATCH` `/missions/:missionId/`

Parameters:

**Response**:

Content-Type application/json  
204 No Content  


*Note:*

- Authorization Protected. Only the mission commander can delete a mission.


## RSVP for a Mission

**Request**:

`PATCH` `/missionrsvp/:missionId/`

Parameters:

```json
{
	"rsvp_users": ["UUIDs of RSVP USERS"]
}
```

*Note:*

- Authorization Protected.

**Response**:

Content-Type application/json  
200 OK  
```json
{
    "rsvp_users": [
        "229a5948-c5a3-4e1f-a075-24bb553335a9",
        "3786b93a-30ea-447a-a2b7-3bdb187ead6d",
        "97d16898-74b2-4720-ada0-c189dde46ebc",
        "61c1fc24-73cb-41f2-9899-d44a1b2bdd54"
    ]
}
```
