*** Settings ***
Library  SeleniumLibrary

*** Keywords ***

Launch browser
    [Arguments]   ${appurl}    ${appbrowser}
    set selenium speed      3 seconds
    open browser     ${appurl}    ${appbrowser}
    Maximize Browser Window
    ${title}=    get title
    [Return]  ${title}

exit
    close browser