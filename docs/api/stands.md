# Resource: stands

## Stands

---

**URL** : `http://localhost:8000/api/stands/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/stands/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

[
    {
        "id": "0917a540-5262-40a6-a4d7-473296101b2a",
        "event": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa",
        "name": "Regalos"
    },
    {
        "id": "e92e2e65-0997-4017-aeff-e81eadd654a4",
        "event": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa",
        "name": "Premios"
    },
    ...
]
```

---

**URL** : `http://localhost:8000/api/stands/`

**Method** : `POST`

**Authentication Pequired** : Yes

**Request Parameters**

```json
{
    "event": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Event"
    },
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
$ curl -X POST "http://localhost:8000/api/stands/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "event": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa", "name": "Regalos"}'
```

**Example Response** :

```json
HTTP 201 Created

{
    "id": "0917a540-5262-40a6-a4d7-473296101b2a",
    "event": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa",
    "name": "Regalos"
}
```

---

**URL** : `http://localhost:8000/api/stands/{id}/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/stands/0917a540-5262-40a6-a4d7-473296101b2a/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": "0917a540-5262-40a6-a4d7-473296101b2a",
    "event": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa",
    "name": "Regalos"
}
```

---

**URL** : `http://localhost:8000/api/stands/{id}/`

**Method** : `PUT`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "event": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Event"
    },
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
$ curl -X PUT "http://localhost:8000/api/stands/0917a540-5262-40a6-a4d7-473296101b2a/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "event": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa", "name": "Regalos"}'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": "0917a540-5262-40a6-a4d7-473296101b2a",
    "event": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa",
    "name": "Regalos"
}
```

---

**URL** : `http://localhost:8000/api/stands/{id}/`

**Method** : `PATCH`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "event": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Event"
    },
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
$ curl -X PATCH "http://localhost:8000/api/stands/0917a540-5262-40a6-a4d7-473296101b2a/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "event": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa", "name": "Regalos"}'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": "0917a540-5262-40a6-a4d7-473296101b2a",
    "event": "2b7e116d-97c1-4ba2-809e-fa227c6d38fa",
    "name": "Regalos"
}
```

---

**URL** : `http://localhost:8000/api/stands/{id}/`

**Method** : `DELETE`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X DELETE "http://localhost:8000/api/stands/0917a540-5262-40a6-a4d7-473296101b2a/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 204 No Content
```

---

**URL** : `http://localhost:8000/api/stands/{id}/products/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/stands/0917a540-5262-40a6-a4d7-473296101b2a/products/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

[
    {
        "id": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3",
        "stand": "0917a540-5262-40a6-a4d7-473296101b2a",
        "name": "Gorra Gris",
        "description": ""
    },
    {
        "id": "4b60c39b-42dc-4c3b-8ec8-56e2e25c7aa6",
        "stand": "0917a540-5262-40a6-a4d7-473296101b2a",
        "name": "Gorra Azul",
        "description": ""
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