*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
Window
    set selenium speed  1 seconds
    open browser    http://www.seleniumframework.com/Practiceform/  chrome
    ${title} =	 get title
    log to console      ${title}

    ${url} =	 get location
    log to console      ${url}

    go to   http://testautomationpractice.blogspot.com/
    ${url} =	 get location
    log to console      ${url}

    go back
    ${url} =	 get location
    log to console      ${url}


