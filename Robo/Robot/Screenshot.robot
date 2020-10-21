*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
Window
    set selenium speed  2 seconds
    open browser    http://testautomationpractice.blogspot.com/  chrome
    Maximize Browser Window
    #click link      Log In
    #input text      xpath://input[@type = 'email']      mvprashanth1986@gmail.com
    #input text      xpath://input[@type = 'password']   Sunshine@1
    #click element   xpath://button[@type='submit']
    #click element   xpath://a[contains(text(),'Post a Project')]
    #capture element screenshot      xpath://img[@class='ImageElement' and @alt='No Projects']
    #capture page screenshot     C:/pythonutils/test.png
    #open context menu   //span[contains(text(),'right click me')]
    double click element    xpath://button[contains(text(),'Copy Text')]
    drag and drop       //ul[@id='gallery']/li[1]   //div[@id='trash']