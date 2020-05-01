SOS Shopping Cart API
=====================
PI for shopping cart provides a selection of endpoints for interacting with a shopping cart backend mechanics for an online shopping website's shopping cart micro-service with cart history database is provided as well. It utiltizes continious integration and continuous deployment, or CI and CD respectively, through Travis CI and Heroku. 

# Contents

- [Generals](#generals)
  - [Functions](#funct)
  - [Hello World](#hello)
  - [Authentication - Authorization](#auth)
- [Cart](#cart) 
  - [Cart Object] (#obj)
  - [Cart History Database] (#db)
- [API](#api)
  - [Endpoints](#endpts)
  - [Requests and responses](#req)
    - [GET current shopping carts](#current)
  
## Functions

List of requirements for this API.

- Display a shopping cart
- Display all carts 
- Create a shopping cart.
- Update a shopping cart
- Check out (Complete the purchase of all the items in the shopping cart)
- Search cart history


## Hello World
Our SOS shopping cart is deployed through heroku at: 
```
https://sos-shoppingcart.herokuapp.com/
```
You can try send a `GET` request to the endpoint. You should see the following JSON message:
```
"Welcome to the API"
```
If you look at the header, you should see that the content-type is json:
```
Content-Type: application/json
```

## Authentication - Authorization
Authorization functionality is provided by a separate, web front-end, micro-service. Therefore, a JWT token (or some other token) is provided by this microservice and included in the Authorization header in all HTTP requests. 

# Cart

## Cart Object

| Attribute | Type | Description |
|-----------|------|-------------|
|**cart_id** |integer |ID of the shopping cart|
|**product_list** |List of products within the shopping cart|
|**user_id** |integer |Owner's id of the shopping cart|
|**complete** |boolean |False = current cart, True = history cart|

## Cart Transaction Database

| Parameter | Type | Description |
|-----------|------|-------------|
|**cart_id** |integer |ID of the shopping cart|
|**user_id** |integer |Owner's id of the shopping cart|
|**product_id** |ID of the product put into shopping cart|
|**quantity** |integer |Number of products selected|
|**complete** |boolean |False = current cart, True = history cart|

# API

## Endpoints

|Method|Endpoint/Request|Description|
|-----|---------------------------------|
|GET|    /api/v1/users/:user_id/current_transactions/|Display active carts|
|GET|    /api/v1/users/:user_id/history_transactions/|Display carts that were checked out|
|POST|   /api/v1/users/:product_id/:quantity/| Add and remove a product item|
|POST|   /api/v1/users/:user_id/checkout|Checkout shopping cart|
X|GET|    /api/v1/carts| Display all carts present in the database|
X|DELETE| /api/v1/users/:user_id/carts/:cart_id/:product_id/| Remove a product from current cart|

## Requests and responses 

Example of requests and responses are given for each endpoints:

### GET current shopping carts
|GET|    /api/v1/users/:user_id/current_transactions/|Display active carts|

**Example:** 
```
GET /api/v1/users/2/current_transactions
Content-type: application/json 
Accept: application/json
```
**Reponse to request:**
```
{
}
```

Create new transaction on the basis of `product_id` and `quantity` parameter
Update `False` status of `complete` parameter of current cart to be `True` = PAID
