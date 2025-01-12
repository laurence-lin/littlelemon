# littlelemon
repo for Meta Backend course

Endpoints: Can be tested with Insomnia

(GET) Static content endpoint: /restaurant/index/
(GET) Get all Menu-items (Don't need authentication): /restaurant/menu-items/   
(GET) Get single menu-items (Require authentication): /restaurant/menu-items/1
(POST) Register new user: /api/auth/users/        Remember to add JSON body: {username: "testuser", password: "testpassword"}
(POST) Authenticate a user: /api/auth/token/login/     Remember to add JSON body: {username: "testuser", password: "testpassword"}

Unit Test:
Test script contained in restaurant/tests
Run the test: python3 manage.py test restaurant/tests