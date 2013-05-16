*** Settings ***
Test Setup        Open SauceLabs test browser
Test Teardown     Run keywords    Report test status    Close All Browsers
Resource          keywords.robot
Resource          plone/app/robotframework/saucelabs.robot

*** Test Cases ***
Set collective.geo preferences
    [Tags]    settings
    Given I'm logged in as a 'Manager'
    When I go to c.geo controlpanel
