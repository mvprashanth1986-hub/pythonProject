*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Time out
   open browser  http://testautomationpractice.blogspot.com/  chrome
   ${spead}=  get selenium speed
   log to console  ${spead}
   set selenium speed   3 seconds
   ${spead}=  get selenium speed
   log to console  ${spead}
   set selenium timeout     10 seconds
   wait until page contains  Volunteer Sign Up