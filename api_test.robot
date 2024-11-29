*** Settings ***
Library    BuiltIn
Library    api_calls.py


*** Variables ***
${BASE_URL}    192.168.0.35
${USERNAME}    musa
${TOKEN}       1125cf2f-2b28-4929-925f-5b1ab433b5a5
${STATESET}    StateSet
${UPALI}       {\"bri\":1}
${UGASI}       {\"bri\":0}
${SSID}        203727
${SEC}         WPA2
${PASSWORD}    peugeot307
${ROOM_NAME}   Living room
${ROOM_KIND}   1 
${LOAD_NAME}   Living bulb
${ROOM_ID}     3
${LOAD_ID}     1

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

Get API Info
    ${info}=    Get API Info    ${BASE_URL}
    Log    ${info}

# Post Account Claim
#     ${response}=    Post Account Claim    ${BASE_URL}    ${USERNAME}
#     Log    ${response}

# Post Network WLAN
#     ${response}=    Post Network Wlan    ${BASE_URL}    ${TOKEN}    ${SSID}    ${SEC}    ${PASSWORD}  
#     Log    ${response}

Post Room Creation
    ${response}=    Post Room Creation    ${BASE_URL}    ${TOKEN}    ${ROOM_NAME}    ${ROOM_KIND}
    Log    ${response}

Patch Load Update
    ${response}=    Patch Load Update    ${BASE_URL}    ${TOKEN}    ${LOAD_ID}    ${LOAD_NAME}    ${ROOM_ID}
    Log    ${response}

Put Target State Update
    ${response}=    Put Target State Update    ${BASE_URL}    ${TOKEN}    ${LOAD_ID}     ${UPALI}
    