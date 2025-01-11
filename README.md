# Testing Website UI with Python Pytest and Selenium

## Purpose
- For testing, which using 
  - Pytest framework
  - Selenium
  - Docker 
- Support testing 
  - Website UI testing (Testing resouces : https://automationexercise.com/test_cases)

## Directory Structure
```commandline
git ls-tree -r --name-only HEAD | tree --fromfile

.
├── .gitignore
├── README.md
├── action
│   ├── api_request.py
│   └── driver.py
├── conftest.py
├── deployments
│   └── Dockerfile
├── logger.py
├── page
│   ├── acc_create_confirmation_page
│   │   ├── acc_create_confirmation_page.py
│   │   └── locator.py
│   ├── home_page
│   │   ├── home_page.py
│   │   └── locator.py
│   ├── login_page
│   │   ├── locator.py
│   │   └── login_page.py
│   └── signup_page
│       ├── locator.py
│       └── signup_page.py
├── readme
│   └── docker_log_test_result.png
├── requirements.txt
└── test_suites
    ├── test_01_user
    │   └── test_register_user.py
    └── test_02_services
        └── test_services.py

```

## Step-by-step
1. Build up a simple Docker
```
$ docker build --platform linux/amd64 --no-cache  -t ui_selenium -f ./deployments/Dockerfile .
```

2. Run the test command
```commandline
$ pytest -v -s
OR
$ pytest -v -s test_suites/test_01_user/test_register_user.py
```
![docker_log_test_result.png](readme%2Fdocker_log_test_result.png)

