# simple\_nest
A simple library for interacting with nest thermostats

## Setup
1. Go to https://developers.nest.com and create a developer account

2. Create a product. Do not fill in a redirect url, we will use pin-based auth. You need to give the product thermostat access.

3. Once you are done you will get produc ID, product secret, and authorization URL.

4. Navigate to the authorization URL (you will auth to nest.com with your regular nest accounts, not the developer account.

5. Click approve, then copy the pin

6. Enter the pin, product id, and product secret to the creds.py file.

7. Run get\_access\_token.py and enter the access token returned into the creds.py file.

8. Get the device id by using the function in the nest library and enter it in the creds.py file.

9. You can now remove the pin from the creds.py file.

## Examples
You can find examples in examples.py.

## Nest Docs:
You can find the documentation for nest at:

https://developers.nest.com/documentation/cloud/api-thermostat
