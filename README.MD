# Public API Automation Project

[![Build Status](https://travis-ci.org/shashikumarraja/public_api_automation_project.svg?branch=master)](https://travis-ci.org/shashikumarraja/public_api_automation_project)

A Sample project creating a basic pytest based framework to automate APIs

APIs used for automation are available here-
https://alexwohlbruck.github.io/cat-facts/docs/endpoints/facts.html

## Project Structure Overview

```
public_api_automation_project         # root dir
├── README.MD                 
├── Dockerfile                        # docker files to create container
├── docker-compose.yaml
├── requirements.txt                  # project requirement libraries are here
├── .travis.yaml                      # travis configuration to run tests on public travis ci
├── src
    ├── conftest.py
    ├── pytest.ini
    ├── tests                          # This is where tests are written
    │   └── test.py
    └── utils                          # Helper utils are written here
        ├── api_utils.py
        ├── file_utils.py
        ├── logger_utils.py
```

## Steps to run the project

### 1. Using [`Docker`](https://docs.docker.com/docker-for-mac/install/):

```sh
# install docker first and then
$ docker-compose up
#check the containers
$ docker ps
```

#### To run `tests`

```sh
docker exec -ti public_api_automation_project pytest src/tests/*.py
```

### 2. Without docker (in local machine)

```sh
# install python 3 first
$ brew install python3
$ cd public_api_automation_project
$ pip install -r requirements.txt
$ export PYTHONPATH="$PYTHONPATH:/public_api_automation_project/"
```

#### To run `tests` locally

```sh
$ pytest src/tests/*.py  

# with html report file
pytest src/tests/*.py --html=report.html --self-contained-html
```

## Test Cases

| Test Case Type   | S.No | Test Description                                                                          | Pre-requisite and Test Data                                                | Test Steps                                                                                                                                                                                                                   | Expected Behaviour                                                                                                                                                                                                    |
|------------------|------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Positive         | 1    | Verify host name/base url is reachable                                                    | valid host name                                                            | GET https://cat-fact.herokuapp.com                                                                                                                                                                                           | Should return status code:200                                                                                                                                                                                         |
|                  | 2    | Verify path "/facts" is reachable and serving request                                     | valid path                                                                 | GET https://cat-fact.herokuapp.com/facts                                                                                                                                                                                     | 1. Should return status code:2002. Should return a json response body                                                                                                                                                 |
|                  | 3    | Verify path "/facts/random" is reachable and serving request                              | valid path                                                                 | GET https://cat-fact.herokuapp.com/facts/random                                                                                                                                                                              | 1. Should return status code:200 2. Should return a json response body 3. Should return the details of default animal Cat in the response body                                                                        |
|                  | 4    | Verify path "/facts/random" with query params                                             | valid path and query params                                                | GET https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1                                                                                                                                                     | 1. Should return status code:200 2. Should return a json response body 3. The returned response count is same as amount passed in the param 4. The response body of animal is same as animal_type passed in the param |
|                  | 5    | Verify path "facts/{fact_id} is reachable and serving request                             | valid fact_id                                                              | GET https://cat-fact.herokuapp.com/facts/591f98803b90f7150a19c229                                                                                                                                                            | 1. Should return status code:200 2. Should return a json response body 3. The returned response count is same as amount passed in the param 4. The response body of animal is of the animal whose id is passed        |
|                  | 6    | Verify response body schema                                                               | 1.valid path2.valid json schema                                            | GET https://cat-fact.herokuapp.com                                                                                                                                                                                           | 1. Should return status code:200 2. Should return a json response body 3. Response body should follow the response schema structure                                                                                   |
|                  |      |                                                                                           |                                                                            |                                                                                                                                                                                                                              |                                                                                                                                                                                                                       |
| Negative         | 1    | Verify invalid path with valid hostname/base url                                          | 1. valid hostname2. random string in path name                             | GET https://cat-fact.herokuapp.com/invalid_path                                                                                                                                                                              | 1. Should return status code: 404 Not found                                                                                                                                                                           |
|                  | 2    | Verify invalid query param name                                                           | 1. valid path2. Invalid query param name                                   | GET https://cat-fact.herokuapp.com/facts/random?invalid_type=cat                                                                                                                                                             | 1. Should return status code 200 2. Should return response as per the default value of params                                                                                                                         |
|                  | 3    | Verify Invalid Request Type                                                               | 1. One of POST, PUT, DELETE                                                | POST https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1PUT https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1DELETE https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1 | 1. Should return status code 404 Not found                                                                                                                                                                            |
|                  | 4    | Verify out of range query param values of amount                                          | 1. valid path2. Invalid query param values of amount(500 is the max limit) | GET https://cat-fact.herokuapp.com/facts/random?amount=700                                                                                                                                                                   | 1. Should return status code 405 Method Not Allowed 2. Should return an error response message                                                                                                                        |
|                  | 5    | Verify with non-existent/invalid animal type                                              | 1. valid path2. Invalid animal_type                                        | GET https://cat-fact.herokuapp.com/facts/random?animal_type=random_string                                                                                                                                                    | 1. Should return status code 200 2. Should return empty response                                                                                                                                                      |
|                  | 6    | Verify path with invalid headers                                                          | 1. valid path2. invalid header                                             | GET https://cat-fact.herokuapp.com/facts                                                                                                                                                                                     | 1. Should return status code 400 Bad Request                                                                                                                                                                          |
|                  |      |                                                                                           |                                                                            |                                                                                                                                                                                                                              |                                                                                                                                                                                                                       |
| Load/Performance | 1    | Verify path "/facts" is reachable and serving request for n user requests simulataneously | 1. Resource to simulate n user request2. Valid path                        | GET https://cat-fact.herokuapp.com/facts                                                                                                                                                                                     | 1. Should return status code 200 for all requests 2. The response time should be within acceptable limits|

## To do

1. Automate all test cases written above
2. Implement more testing strategies like hypothesis test to get better coverage
3. Refactor the code
4. Integrate more reports for better test result analysis
   