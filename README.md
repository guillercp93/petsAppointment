# Pets Appointment
This is a restful project that contains **user**, **pets** and **appointments** modules.
An appointment is between user and his pet, in a date and a place.
A pets have a user(*assignedTo*), this is optional.

### API´s urls
###### For user administration.
fields:
	username: String,
	password: String,
	first_name: String
	last_name: String
	email: String
1. */admin/login/*
 	This url is to login user in the app (username, password).
2. */admin/logout/*
    This url to logout user from app.
3. */account/{:id}*
  	{GET} Get data of user(s)
 	{POST} Create a new user
  	{PUT} Update user data
4. */get-token/*
  	This url generate a token from user data (username, password). This access token is 		used in the **Authorization header** when the user take actions over modules. 
 	Return example:
 		{
			'refresh': '9274f2yf7492yf4279',
			'access': '238fy932yf382yf',
		}

------------
###### Pets module
	Fields:
		description: String
		name: String
		assignedTo: Integer(user´s id).
		typePet: String.
5. /pets/{:id}
	{GET} Get data of pet(s)
 	{POST} Create a new pet
  	{PUT} Update a pet
	{DELETE} Delete a pet


------------
###### Appointments module
    Fields:
    	pet: Integer (pet´s id)
    	owner: Integer (user´s id)
    	dateAppointment: Date
    	place: String
6. /appointments/
	{GET} Get data of appointment(s)
 	{POST} Create a new appointment
  	{PUT} Update a appointment
	{DELETE} Delete a appointment
