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
├── readme
│   └── docker_log_test_result.png
├── requirements.txt
├── screenshots
│   └── screenshot_20240401_001956.jpg
└── test_suites
    ├── test_01_user
    │   ├── locator.py
    │   └── test_register_user.py
    └── test_02_test_cases
        ├── locator.py
        └── test_verify_test_cases_page.py
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

