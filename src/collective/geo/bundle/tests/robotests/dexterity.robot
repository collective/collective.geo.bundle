*** Settings ***
Test Setup        Open SauceLabs test browser
Test Teardown     Run keywords    Report test status    Close All Browsers
Resource          keywords.robot
Resource          plone/app/robotframework/saucelabs.robot

*** Test Cases ***
Test dexterity content type
    [Tags]    dexterity
    Given I'm logged in as a 'Manager'
    Go to homepage
    Create dexterity test content with geo behaviour    Test-content-with-behaviour
    Click Link    link=Edit
    Click Link    link=Coordinates
    Select Checkbox    id=form-widgets-IGeoFeatureStyle-use_custom_styles-0
    Click Button    Save
