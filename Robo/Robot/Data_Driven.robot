*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}          https://www.freelancer.in/
${browser}      chrome

*** Keywords ***
open bro
    open browser    ${url}  ${browser}
    Maximize Browser Window
    set selenium speed  2 seconds

close bro
    close all browsers

open page
    go to  ${url}
    click link      Log In

Input Username
    [Arguments]     ${username}
    input text  xpath://input[@type='email']       ${username}

Input Password
    [Arguments]     ${password}
    input text  xpath://input[@type='password']     ${password}

Click Login Button
    click element   xpath://button[@type='submit']

errror message
    page should contain     Incorrect username or password.

positive message
    page should contain     Dashboard
