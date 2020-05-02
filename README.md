SOS Shopping Cart API
=====================
This API for shopping cart provides a selection of endpoints for interacting with backend mechanics for an online shopping website's cart as a micro-service, with cart transaction history database. We utiltize continious integration (CI) and continuous deployment (CD) through Travis CI and Heroku. 

## List of requirements:

- Update a shopping cart (add/remove)
- Check out (Complete purchase of all products in current shopping cart)
- Display history and current shopping carts of each user

# Contents

- [Generals](#generals)
  - [Hello World](#hello)
  - [Authentication - Authorization](#auth)
- [Cart](#cart) 
  - [Cart Object](#obj)
  - [Cart Transaction History Database](#db)
- [API](#api)
  - [Endpoints](#endpts)
  - [Requests and responses](#req)
    - [POST add or remove product items](#transaction)
    - [POST checkout shopping cart](#checkout)
    - [GET current shopping carts](#current)
    - [GET history shopping carts](#history)
 
## Hello World 
Our SOS shopping cart is deployed through heroku at: 
```
https://sos-shoppingcart.herokuapp.com/
```
You can try send a `GET` request to the endpoint. You should see the following JSON message:
```
"Welcome to the shopping cart and cart transaction database API!"
```
If you look at the header, you should see that the content-type is json:
```
Content-Type: application/json
```

## Authentication - Authorization
Authorization functionality is provided by a separate, web front-end, micro-service. Therefore, a JWT token is provided by front-end microservice and included in the Authorization header in all HTTP requests. 

# Cart 

## Cart Object

| Attribute | Type | Description |
|-----------|------|-------------|
|**cart_id** |integer |ID of the shopping cart|
|**product_list**|integer |List of products within the shopping cart|
|**user_id** |integer |Owner's id of the shopping cart|
|**complete** |boolean |False = current cart, True = history cart|

## Cart Transaction History Database

| Parameter | Type | Description |
|-----------|------|-------------|
|**cart_id** |integer |ID of the shopping cart|
|**user_id** |integer |Owner's id of the shopping cart|
|**product_id** |integer |ID of the product put into shopping cart|
|**quantity** |integer |Number of products selected|
|**complete** |boolean |False = current cart, True = history cart|

# API

## Endpoints

|Method|Endpoint/Request|Description|
|------|----------------|-----------|
|**POST**|   /api/v1/transactions| Add or remove product items|
|**POST**|   /api/v1/checkout|Checkout shopping cart|
|**GET**|    /api/v1/users/:user_id/current_transactions/|Display active carts|
|**GET**|    /api/v1/users/:user_id/history_transactions/|Display carts that were checked out|

## Requests and responses

Example of requests and responses are given for each endpoints:

### POST add or remove product items
Create new transaction on the basis of `product_id` and `quantity` parameter
Endpoint: /api/v1/transactions/

**Add Example:** 

```
POST /api/v1/transactions
Content-type: application/json 
Accept: application/json
```
**Reponse to request:**
```
{
	"user_id": 55
	"product id": "1",
	"quantity": "1",
	"complete": "False"
}
```

**Remove Example:** 

```
POST /api/v1/transactions
Content-type: application/json 
Accept: application/json
```
**Reponse to request:**
```
{
	"user_id": 55
	"product id": "1",
	"quantity": "0",
	"complete": True"
}
```

### POST checkout shopping cart
Update `False` status of `complete` parameter of current cart to be `True` = PAID
Endpoint: /api/v1/checkout

**Example:** 

```
GET /api/v1/checkout
Content-type: application/json 
Accept: application/json
```
**Reponse to request:**
```
{
}
```

### GET current shopping carts
Endpoint:  /api/v1/users/:user_id/current_transactions/

**Example:** Current user `id` = 2 

```
GET /api/v1/users/2/current_transactions/
Content-type: application/json 
Accept: application/json
```
**Reponse to request:**
```
{
}
```

### GET history shopping carts
Endpoint: /api/v1/users/:user_id/history_transactions/

**Example:**  Current user `id` = 2 

```
GET /api/v1/users/2/history_transactions
Content-type: application/json 
Accept: application/json
```
**Reponse to request:**
```
{
}
```
