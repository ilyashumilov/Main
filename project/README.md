<h1 align="center">Education process organization system</h1>

[Click “Watch” in this repository](https://help.github.com/en/github/receiving-notifications-about-activity-on-github/watching-and-unwatching-repositories) to keep track of the latest changes in the project.

Please read through our [Contribution Guidelines](CONTRIBUTING.md), [Architecture Overview](ARCHITECTURE.md) and [Installation Instructions](INSTALL.md).

The repository is a part of the [metasharks.ru](https://metasharks.ru/ru). This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).


## Overview

## API calls

### Create new Area instance `area/`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-d "{"title":"area's title"}"
"<hostname>/api/v1/area"

```

Response:

```
{
    "message": "The new Area instance has been created"
}
```

### Retrieve all Area's instances `area/`

Метод: `GET`

```
curl -XGET
-H "Content-Type: application/json"
"<hostname>/api/v1/area"

```

Response:

```
[
    {
        "id": 4,
        "title": "third"
    },
    {
        "id": 5,
        "title": "4"
    },
]
```

### Delete Area instance `area/?id=instance's id`

Method: `DELETE`

```
curl -XDELETE
-H "Content-Type: application/json"
"<hostname>/api/v1/area/?id=instance's id"

```

Response:

```
{
    "message": "The Area instance with id 4 has been deleted"
}
```


### Create new Curator instance `curator/`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-d "{"name":"curator's name", "area_id":"Curator's area's id"}"
"<hostname>/api/v1/curator"

```

Response:

```
{
    "message": "The new Curator instance has been created"
}
```

### Retrieve all Curator's instances `curator/`

Метод: `GET`

```
curl -XGET
-H "Content-Type: application/json"
"<hostname>/api/v1/curator"

```

Response:

```
[
    {
        "id": 3,
        "name": "curators name",
        "area_id": "8"
    },
    {
        "id": 4,
        "name": "curators name",
        "area_id": "8"
    }
]
```

### Delete Curator instance `curator/?id=instance's id`

Method: `DELETE`

```
curl -XDELETE
-H "Content-Type: application/json"
"<hostname>/api/v1/curator/?id=instance's id"

```

Response:

```
{
    "message": "The Curator instance with id 4 has been deleted"
}
```


### Create new Discipline instance `discipline/`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-d "{"title":"discipline's title", "area_id":"Discipline's area's id"}"
"<hostname>/api/v1/discipline"

```

Response:

```
{
    "message": "The new Discipline instance has been created"
}
```

### Retrieve all Discipline instances `discipline/`

Метод: `GET`

```
curl -XGET
-H "Content-Type: application/json"
"<hostname>/api/v1/discipline"

```

Response:

```
[
    {
        "id": 3,
        "title": "discipline's title",
        "area_id": "8"
    },
    {
        "id": 4,
        "title": "discipline's title",
        "area_id": "8"
    }
]
```

### Delete Discipline instance `discipline/?id=instance's id`

Method: `DELETE`

```
curl -XDELETE
-H "Content-Type: application/json"
"<hostname>/api/v1/discipline/?id=instance's id"

```

Response:

```
{
    "message": "The Discipline instance with id 4 has been deleted"
}
```


### Create new Group instance `group/`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-d "{"title":"group's title", "area_id":"Discipline's area's id"}"
"<hostname>/api/v1/group"

```

Response:

```
{
    "message": "The new Group instance has been created"
}
```

### Retrieve all Group's instances `group/`

Метод: `GET`

```
curl -XGET
-H "Content-Type: application/json"
"<hostname>/api/v1/group"

```

Response:

```
[
    {
        "id": 3,
        "title": "group's title",
        "area_id": "8"
    },
    {
        "id": 4,
        "title": "group's title",
        "area_id": "8"
    }
]
```

### Delete Group instance `group/?id=instance's id`

Method: `DELETE`

```
curl -XDELETE
-H "Content-Type: application/json"
"<hostname>/api/v1/group/?id=instance's id"

```

Response:

```
{
    "message": "The Group instance with id 4 has been deleted"
}
```


### Create new Student instance `student/`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-d "{"name":"student's title", "group_id":"Group's id", "sex":"male/female"}"
"<hostname>/api/v1/student"

```

Response:

```
{
    "message": "The new Student instance has been created"
}
```

### Retrieve all Student instances `student/`

Метод: `GET`

```
curl -XGET
-H "Content-Type: application/json"
"<hostname>/api/v1/student"

```

Response:

```
[
    {
        "id": 3,
        "name": "student's name",
        "sex": "male",
        "group_id": "8"
    },
    {
        "id": 4,
        "name": "discipline's title",
        "sex": "male",
        "group_id": "8"
    }
]
```

### Delete Student instance `student/?id=instance's id`

Method: `DELETE`

```
curl -XDELETE
-H "Content-Type: application/json"
"<hostname>/api/v1/student/?id=instance's id"

```

Response:

```
{
    "message": "The Student instance with id 4 has been deleted"
}
```


### Schedule report generation `create_report`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
"<hostname>/api/v1/create_report/"

```

Response:

```
{
    "message": "The report has been scheduled to be generated"
}
```

### Retrieve status of report's generation task `task_status`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-d "{"task_id":"tasks's id"}"
"<hostname>/api/v1/task_status"
```


Response:

```
]
```

### Retrieve created report `retrieve_report`

Method: open the following url in the browser, and generated report file will be uploaded automatically.

```
<hostname>/api/v1/retrieve_report/
```

Response:

```
report.xlsx file
```