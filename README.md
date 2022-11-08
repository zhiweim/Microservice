# CS 361

Repository for CS361

# Microservice receive and request data

## How to request data:

Data requests can be made by sending a request to the server in the form of a string. If the location is a city and state located in the United States, then the format should be 'city, state'. For example, if the user wants to request location information for Portland, Oregon the format should be 'portland, oregon'. Otherwise, the location can just be a one word string. For example, the user wants to request information for Singapore, the format should be 'singapore'. 

## How to receive data:

After receiving the request, the microservice will perform a simple wikipedia web scrape for the requested location. Data will be sent in the form of a string, and the data will be the first summary of the wikipedia article of the location.


## UML Diagram

![cs361ass8](https://user-images.githubusercontent.com/97495576/198922330-c9c29f59-7798-4fc1-bb01-e4c86ba6f364.jpg)
