*** Settings ***
Library    BuiltIn
Library    api_calls.py


*** Variables ***
${BASE_URL}    192.168.0.35
${USERNAME}    musa
${TOKEN}       0599d4dc-ecdf-4798-9bd8-2d5bc2ffe555
${STATESET}    StateSet
${UPALI}       {\"bri\":5000}
${UGASI}       {\"bri\":0}

*** Test Cases ***
Turn On Load
    ${auth_token}=    Set Variable   ${TOKEN} 
    ${load_id}=    Set Variable    ${1} 
   # ${target_state}=    ${UPALI} 
    ${response}=    Set Load State    ${BASE_URL}    ${auth_token}    ${load_id}    ${UPALI}
    Should Be Equal    ${response}    ${STATESET}
    Sleep    5s

Turn Off Load
    ${auth_token}=    Set Variable    ${TOKEN} 
    ${load_id}=    Set Variable    ${1} 
    #${target_state}=    ${UPALI}  
    ${response}=    Set Load State    ${BASE_URL}    ${auth_token}    ${load_id}     ${UGASI}
    Should Be Equal    ${response}    ${STATESET}

