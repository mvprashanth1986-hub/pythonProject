*** Settings ***

Library  SeleniumLibrary
Resource  ../resources/resources.robot

*** Variables ***
${url}      https://www.countries-ofthe-world.com/flags-of-the-world.html
${browser}      chrome


*** Test Cases ***
Login
    Launch browser  ${url}      ${browser}
    execute javascript      window.scrollTo(1,1500)
    scroll element into view    xpath://td[contains(text(),'India')]
    execute javascript      window.scrollTo(0,document.body.scrollHeight)



*** Keywords ***
