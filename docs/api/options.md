# Resource: options

## Options

---

**URL** : `http://localhost:8000/api/options/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/options/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

[
    {
        "id": "60f6a37f-95c4-4473-90b0-4f6d7dd7deed",
        "product": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3",
        "description": "L"
    },
    {
        "id": "9318d835-585b-495d-990a-5fb5016f9d98",
        "product": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3",
        "description": "M"
    },
    {
        "id": "ab06b0a5-d1d4-4406-82ae-0311baec9c76",
        "product": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3",
        "description": "S"
    },
    {
        "id": "e16d0b34-fa27-4642-b1f9-ec4163f0e598",
        "product": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3",
        "description": "XS"
    },
    ...
]
```

---

**URL** : `http://localhost:8000/api/options/`

**Method** : `POST`

**Authentication Pequired** : Yes

**Request Parameters**

```json
{
    "product": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Product"
    },
    "description": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Description",
        "max_length": 100
    }
}
```

**Example Request** :

```shell
$ curl -X POST "http://localhost:8000/api/options/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "product": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3", "description": "XS"}'
```

**Example Response** :

```json
HTTP 201 Created

{
    "id": "e16d0b34-fa27-4642-b1f9-ec4163f0e598",
    "product": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3",
    "description": "XS"
}
```

---

**URL** : `http://localhost:8000/api/options/{id}/`

**Method** : `GET`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X GET "http://localhost:8000/api/options/e16d0b34-fa27-4642-b1f9-ec4163f0e598/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": "e16d0b34-fa27-4642-b1f9-ec4163f0e598",
    "product": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3",
    "description": "XS"
}
```

---

**URL** : `http://localhost:8000/api/options/{id}/`

**Method** : `PUT`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "product": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Product"
    },
    "description": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Description",
        "max_length": 100
    }
}
```

**Example Request** :

```shell
$ curl -X PUT "http://localhost:8000/api/options/e16d0b34-fa27-4642-b1f9-ec4163f0e598/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "product": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3", "description": "XS"}'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": "e16d0b34-fa27-4642-b1f9-ec4163f0e598",
    "product": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3",
    "description": "XS"
}
```

---

**URL** : `http://localhost:8000/api/options/{id}/`

**Method** : `PATCH`

**Authentication Pequired** : Yes

**Request Parameters** :

```json
{
    "product": {
        "type": "field",
        "required": true,
        "read_only": false,
        "label": "Product"
    },
    "description": {
        "type": "string",
        "required": true,
        "read_only": false,
        "label": "Description",
        "max_length": 100
    }
}
```

**Example Request** :

```shell
$ curl -X PATCH "http://localhost:8000/api/options/e16d0b34-fa27-4642-b1f9-ec4163f0e598/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -d '{ "product": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3", "description": "XS"}'
```

**Example Response** :

```json
HTTP 200 OK

{
    "id": "e16d0b34-fa27-4642-b1f9-ec4163f0e598",
    "product": "fbe92213-06bf-4dd1-ba22-1866f3a7d9a3",
    "description": "XS"
}
```

---

**URL** : `http://localhost:8000/api/options/{id}/`

**Method** : `DELETE`

**Authentication Pequired** : Yes

**Request Parameters** : None

**Example Request** :

```shell
$ curl -X DELETE "http://localhost:8000/api/options/e16d0b34-fa27-4642-b1f9-ec4163f0e598/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```

**Example Response** :

```json
HTTP 204 No Content
```

---

## Resources

- **Events** : `http://localhost:8000/api/options/`    ***[view details](events.md)***.
- **Stands** : `http://localhost:8000/api/stands/`    ***[view details](stands.md)***.
- **Products** : `http://localhost:8000/api/products/`    ***[view details](products.md)***.
- **Options** : `http://localhost:8000/api/options/`    ***[view details](options.md)***.