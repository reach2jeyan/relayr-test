Using the public apis hosted at https://binaryjazz.us/genrenator-api/ as a part of github public api project

The end points generate random list of story and genre based on the length provided by the user. In order to test this, pytest framework is used for asserts.

Set ups required:
1. python3 using brew
2. pip3 installation
3. pip3 install pytest
4. pip3 install unittest
5. pip3 install requests
6. pip3 install pytest.html

Request library is used to call the api's and get access to several other properties of the apis.

To Run the tests
1. Build the docker with `docker build tests`
2. After the docker runs you will find the html report
3. To run web tests, you need to install `pip install playwright` & `python -m playwright install` . Could not dockerize as playwright seems to have some run time issue on the linux containers, have to dig more to it.

Test cases for api's:
1. POST request on a GET must throw a relevant error and must not result in 500
2. Passing incorrect Query parameter in the headers must not result in 500 
3. Passing valid GET request must return valid response in the json and must contain mandatory headers returned
4. Appending invalid queries in the get request must either redirect the user to the valid api or must exit gracefully but not throw 500
5. Valid data must be returned as per that exists in the database, the api must point to the relevant table and column in the database. For eg: You could update the database in the before class and then run the test on the loaded data, then clear the data in the afterAll
6. Response body must be properly nested as a valid json. if the backend jsonifies it would be in json itself
7. Passing without query parameter must not throw 500
8. GET request must also accept multiple query parameters and headers as well. Test with various combinations as per the requirements
9. Get request must throw relevant error when queried with incorrect cookie or when unauthorized

Test cases for web:
1. Ensure user can search and the search lists as per the keyword
2. Intercept network call and ensure user can search through multiple search results and load with one search result.
3. Intercept network call and ensure user sees search did not yield results in case the key word has not content matched.
4. Ensure user can backspace search after typing and can see the placeholder
5. Ensure user can click on back from the article and reach back to the search screen
6. Ensure server does not crash when enter pressed in the search without typing keyword
7. Ensure refresh of the page maintains the search results and does not clear the search
