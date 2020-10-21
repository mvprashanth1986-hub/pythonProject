*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}      http://testautomationpractice.blogspot.com/
${browser}      chrome

*** Test Cases ***
TC1
    Login
    select frame  frame-one1434677811
    input text  name:RESULT_TextField-1     James
    input text  name:RESULT_TextField-2     Bond
    input text  name:RESULT_TextField-3     9876543210
    input text  name:RESULT_TextField-4     India
    input text  name:RESULT_TextField-5     Banglore
    input text  name:RESULT_TextField-6     mvprashanth@gmail.com




*** Keywords ***
Login
    open browser    ${url}      ${browser}
    Maximize Browser Window



