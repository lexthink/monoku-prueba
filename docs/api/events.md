# Resource: events

## Events

---

**URL** : `http://localhost:8000/api/events/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/events/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

[
    {
        "id": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa",
        "title": "Python 3 Programming Specialization"
    },
    ...
]
```

---

**URL** : `http://localhost:8000/api/events/`

**Method** : `POST`

**Authentication Pequired** : Yes

**Request Parameters**

```json
{
    "name": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Name",
        "max_length": 100
    }
}
```

**Example Request** :

```shell
$ curl -X POST "http://localhost:8000/api/events/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "name": "Python 3 Programming Specialization" }'
```

**Example Response** :

```json
HTTP 201 Created

{
    "id": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa",
    "name": "Python 3 Programming Specialization"
}
```

---

**URL** : `http://localhost:8000/api/events/{id}/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/events/2b7e116d-97c1-4ba2-809e-fa227c6d38fa/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa",
    "name": "Python 3 Programming Specialization"
}
```

---

**URL** : `http://localhost:8000/api/events/{id}/`

**Method** : `PUT`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "name": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Name",
        "max_length": 100
    }
}
```

**Example Request** :

```shell
$ curl -X PUT "http://localhost:8000/api/events/2b7e116d-97c1-4ba2-809e-fa227c6d38fa/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "name": "Python 3 Programming Specialization" }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa",
    "name": "Python 3 Programming Specialization"
}
```

---

**URL** : `http://localhost:8000/api/events/{id}/`

**Method** : `PATCH`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "name": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Name",
        "max_length": 100
    }
}
```

**Example Request** :

```shell
$ curl -X PATCH "http://localhost:8000/api/events/2b7e116d-97c1-4ba2-809e-fa227c6d38fa/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "name": "Python 3 Programming Specialization" }'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa",
    "title": "Python 3 Programming Specialization"
}
```

---

**URL** : `http://localhost:8000/api/events/{id}/`

**Method** : `DELETE`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X DELETE "http://localhost:8000/api/events/2b7e116d-97c1-4ba2-809e-fa227c6d38fa/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 204 No Content
```

---

**URL** : `http://localhost:8000/api/events/{id}/stands/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/events/2b7e116d-97c1-4ba2-809e-fa227c6d38fa/stands/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

[
    {
        "id": "e92e2e65-0997-4017-aeff-e81eadd654a4",
        "event": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa",
        "name": "Premios"
    },
    {
        "id": "0917a540-5262-40a6-a4d7-473296101b2a",
        "event": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa",
        "name": "Regalos"
    },
    ...
]
```

---

## Resources

- **Events** : `http://localhost:8000/api/events/`    ***[view details](events.md)***.
- **Stands** : `http://localhost:8000/api/stands/`    ***[view details](stands.md)***.
- **Products** : `http://localhost:8000/api/products/`    ***[view details](products.md)***.
- **Options** : `http://localhost:8000/api/options/`    ***[view details](options.md)***.