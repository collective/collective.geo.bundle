*** Settings ***
Resource          plone/app/robotframework/keywords.robot
Library           Remote    ${PLONE_URL}/RobotRemote

*** Variables ***
${ZOPE_HOST}      localhost
${ZOPE_PORT}      55001
${ZOPE_URL}       http://${ZOPE_HOST}:${ZOPE_PORT}
${PLONE_SITE_ID}    plone
${PLONE_URL}      ${ZOPE_URL}/${PLONE_SITE_ID}


*** Keywords ***
I'm logged in as a '${ROLE}'
    Enable autologin as    ${ROLE}
    Go to    ${PLONE_URL}

I go to c.geo controlpanel
    Go to homepage
    Click link    Manager
    Click link    Site Setup
    Click link    ${PLONE_URL}/@@collectivegeo-controlpanel
    Element should become visible    css=#formfield-form-widgets-geo_content_types

Set document georeferenceable
    [Arguments]    ${name}    ${element}
    Go to    ${PLONE_URL}/@@collectivegeo-controlpanel
    Wait until location is    ${PLONE_URL}/@@collectivegeo-controlpanel
    Select From List    xpath=//select[@name="${name}.from"]    ${element}
    Click Button    xpath=/html/body/div[3]/div[2]/div/div[2]/div/div/div/form/fieldset/div/div/div[3]/table/tbody/tr/td[2]/button
    List Selection Should Be    xpath=//select[@name="${name}.to"]    ${element}
    Click Button    Apply
    Check Status Message    Changes Saved

Create dexterity test content with geo behaviour
    [Arguments]  ${title}
    Open Add New Menu
    Click Link  link=dexterity content with geo behavior
    Input text  name=form.widgets.IBasic.title  ${title}
    Click Button  Save
    Check Status Message  Item created
