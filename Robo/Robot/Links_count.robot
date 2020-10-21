*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
case
    open browser  http://www.amazon.in/  chrome
    ${c} =  get element count  xpath://a
    log to console  ${c}

    : FOR  ${i}  IN RANGE  1   ${c}
    \  ${j}=  get text  xpath:(//a)[${i}]
    \  log to console  ${j}
