*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
Alert
    Open Browser    http://testautomationpractice.blogspot.com/     chrome
    click element   xpath://button[contains(text(),'Click Me')]
#    handle alert  Accept
#    handle alert  Dismiss
#    handle alert  Leave

    alert should be present      Press a button!