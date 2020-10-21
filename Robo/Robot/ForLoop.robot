
*** Test Cases ***
ForLoop1
    : FOR  ${i}  IN RANGE   1  5
    \  log to console   ${i}

ForLoop2
    : FOR  ${i}  IN   1  2  3  4  5  6  7  8
    \  log to console  ${i}

ForLoop3
    : FOR  ${i}  IN   james  bond  john  johnnay
    \  log to console  ${i}

ForLoop4
   @{list}   create list   james  bond  john  johnnay
    : FOR  ${i}  IN   @{list}
    \  log to console   ${i}

ForLoop5
   @{list}   create list   1  2  3  4  5  6  7  8
    : FOR  ${i}  IN   @{list}
    \  log to console   ${i}
    \  exit for loop if  ${i} == 4