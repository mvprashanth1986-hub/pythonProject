*** Settings ***
Library  SeleniumLibrary
Resource   ../resources/resources.robot


*** Variables ***
${url}  https://www.freelancer.in/
${browser}  Chrome


*** Test Cases ***
Login Test
    ${pagetitle} =  Launch browser  ${url}      ${browser}
    log to console   ${pagetitle}
    click link       Log In
    input text       xpath://input[@type='email']  mvprashanth1986@gmail.com
    input text       xpath://input[@type='password']   Sunshine@1
    click element    xpath://button[@type='submit']
    exit
    exit