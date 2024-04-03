## Project setup requirements
### Prerequisites:
Python 3.10 + pip


## Installation
    pip install -r requirements.txt
    playwright install

## Create .ENV file in root folder:
    {
      "url": "https://www.saucedemo.com/",
      "user": "standard_user",
      "password":"secret_sauce"
    }

## PyTest configuration
To run tests in chrome/headed mode - following line should be present in pytest.ini:
    
    addopts = --browser-channel=chrome --headed

# Tests Execution
## Run all tests
    pytest
## Run specific test
    pytest ./test/__Specific_test__
## Run only UI tests
    pytest -m ui
