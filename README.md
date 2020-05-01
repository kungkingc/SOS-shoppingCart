SOS Shopping Cart API
=====================
This repo contains API for shopping cart provides a selection of endpoints for interacting with a shopping cart backend mechanics for an online shopping website's shopping cart micro-service. Additionally, cart history database is provided as well. 

# Contents

- [Generals](#generals)
-- [Hello World](#hello)
-- [Functions](#funct)
- [Cart](#cart) 
-- [API Endpoints](#endpts)
-- [Cart Object] (#obj)
-- [Cart History Database] (#db)

## Hello World
Our SOS shopping cart is located at: `https://sos-shoppingcart.herokuapp.com/`
You can try send a `GET` request to the endpoint. You should see the following JSON message:
`"Welcome to the API"`
If you look at the header, you should see that the content-type is json:
`Content-Type: application/json`

## Functions

List of requirements for this API.

- Display a shopping cart
- Display all carts 
- Create a shopping cart.
- Update a shopping cart
- Check out (Complete the purchase of all the items in the shopping cart)
- Search cart history
