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

Set dxdocument georeferenceable
    Go to    ${PLONE_URL}/@@dexterity-types
    Wait until location is    ${PLONE_URL}/@@dexterity-types
    Click Link  link=Page
    Click Link  link=Behaviors
    Select checkbox  form-widgets-collective-geo-behaviour-interfaces-ICoordinates-0
    Select checkbox  form-widgets-collective-geo-behaviour-interfaces-IGeoFeatureStyle-0
    Click button  Save
    Page should contain  Behaviors successfully updated

Create dexterity document with geo behaviour
    [Arguments]  ${title}
    DEBUG
    Click element  css=.icon-plone-contentmenu-factories
    Click Link  document
    Input text  name=form.widgets.IBasic.title  ${title}
    Click Button  Save
    Check Status Message  Item created
