*** Settings ***
Test Setup        Open SauceLabs test browser
Test Teardown     Run keywords    Report test status    Close All Browsers
Resource          keywords.robot
Resource          plone/app/robotframework/saucelabs.robot

*** Test Cases ***
create document and georeference it
    [Tags]    user
    Given I'm logged in as a 'Manager'
    set document georeferenceable    form.widgets.geo_content_types    Document
    Go to homepage
    Add Document    georeferenced document
    Page Should Contain Link    Coordinates
