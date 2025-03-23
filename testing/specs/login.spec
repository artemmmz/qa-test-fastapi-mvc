# Login Specification
    Tags: login, auth

## Successful authorization with correct data
    * Send a POST request to "/auth/login" with email "correct_user@example.com" and password "correct_password"
    * Verify response status is "200"

## Unsuccesful authorization with correct email and incorrect password
    * Send a POST request to "/auth/login" with email "correct_user@example.com" and password "incorrect_password"
    * Verify response status is "401"
    * Verify response contains "detail" with data "Incorrect password"

## Unsuccessful authorization with unregistered user
    * Send a POST request to "/auth/login" with email "incorrect_user@example.com" and password "incorrect_password"
    * Verify response status is "404"
    * Verify response contains "detail" with data "User not found"

## Unsuccessful authorization with unregistered user and existed password 
    * Send a POST request to "/auth/login" with email "incorrect_user@example.com" and password "correct_password"
    * Verify response status is "404"
    * Verify response contains "detail" with data "User not found"
