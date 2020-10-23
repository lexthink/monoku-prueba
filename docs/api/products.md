# Resource: products

## Products

---

**URL** : `http://localhost:8000/api/products/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/products/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
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

**URL** : `http://localhost:8000/api/products/`

**Method** : `POST`

**Authentication Pequired** : Yes

**Request Parameters**

```json
{
    "stand": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Stand"
    },
    "name": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Name",
        "max_length": 100
    },
    "description": {
        "type": "string",
        "required": false,
        "read_only": false,
        "label": "Description",
        "help_text": "a detailed description of the product"
    }
}
```

**Example Request** :

```shell
$ curl -X POST "http://localhost:8000/api/products/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "stand": "0917a540-5262-40a6-a4d7-473296101b2a", "name": "Gorra Gris", "description": ""}'
```

**Example Response** :

```json
HTTP 201 Created

{
    "id": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3",
    "stand": "0917a540-5262-40a6-a4d7-473296101b2a",
    "name": "Gorra Gris",
    "description": ""
}
```

---

**URL** : `http://localhost:8000/api/products/{id}/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/products/fbe92213-06bf-4dd1-ba22-1866f3a7d9a3/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3",
    "stand": "0917a540-5262-40a6-a4d7-473296101b2a",
    "name": "Gorra Gris",
    "description": ""
}
```

---

**URL** : `http://localhost:8000/api/products/{id}/`

**Method** : `PUT`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "stand": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Stand"
    },
    "name": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Name",
        "max_length": 100
    },
    "description": {
        "type": "string",
        "required": false,
        "read_only": false,
        "label": "Description",
        "help_text": "a detailed description of the product"
    }
}
```

**Example Request** :

```shell
$ curl -X PUT "http://localhost:8000/api/products/fbe92213-06bf-4dd1-ba22-1866f3a7d9a3/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "stand": "0917a540-5262-40a6-a4d7-473296101b2a", "name": "Gorra Gris", "description": ""}'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3",
    "stand": "0917a540-5262-40a6-a4d7-473296101b2a",
    "name": "Gorra Gris",
    "description": ""
}
```

---

**URL** : `http://localhost:8000/api/products/{id}/`

**Method** : `PATCH`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "stand": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Stand"
    },
    "name": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Name",
        "max_length": 100
    },
    "description": {
        "type": "string",
        "required": false,
        "read_only": false,
        "label": "Description",
        "help_text": "a detailed description of the product"
    }
}
```

**Example Request** :

```shell
$ curl -X PATCH "http://localhost:8000/api/products/fbe92213-06bf-4dd1-ba22-1866f3a7d9a3/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "stand": "0917a540-5262-40a6-a4d7-473296101b2a", "name": "Gorra Gris", "description": ""}'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3",
    "stand": "0917a540-5262-40a6-a4d7-473296101b2a",
    "name": "Gorra Gris",
    "description": ""
}
```

---

**URL** : `http://localhost:8000/api/products/{id}/`

**Method** : `DELETE`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X DELETE "http://localhost:8000/api/products/fbe92213-06bf-4dd1-ba22-1866f3a7d9a3/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 204 No Content
```

---

**URL** : `http://localhost:8000/api/products/{id}/options/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/products/fbe92213-06bf-4dd1-ba22-1866f3a7d9a3/options/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

[
    {
        "id": "60f6a37f-95c4-4473-90b0-4f6d7dd7deed",
        "description": "L"
    },
    {
        "id": "9318d835-585b-495d-990a-5fb5016f9d98",
        "description": "M"
    },
    {
        "id": "ab06b0a5-d1d4-4406-82ae-0311baec9c76",
        "description": "S"
    },
    {
        "id": "e16d0b34-fa27-4642-b1f9-ec4163f0e598",
        "description": "XS"
    },
    ...
]
```

---

## Resources

- **Events** : `http://localhost:8000/api/events/`    ***[view details](events.md)***.
- **Stands** : `http://localhost:8000/api/products/`    ***[view details](stands.md)***.
- **Products** : `http://localhost:8000/api/products/`    ***[view details](products.md)***.
- **Options** : `http://localhost:8000/api/options/`    ***[view details](options.md)***.