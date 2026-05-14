#!/usr/bin/env bash

curl --path-as-is -k -X GET 'https://sadiq-eltajer.sa/api/ads/keywords-list' \
  -H 'Host: sadiq-eltajer.sa' \
  -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0' \
  -H 'Accept: application/json' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Accept-Encoding: gzip, deflate, br' \
  -H 'Referer: https://sadiq-eltajer.sa/' \
  -H 'X-App-Api-Token: o3fNzP7ZeAX97q5mjjtqRVon51jrOol8' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Priority: u=4' \
  -H 'Te: trailers' \
  -b 'XSRF-TOKEN=eyJpdiI6IjlqcDNqQ2ZSNHZEeStOSVBnQ0VRSmc9PSIsInZhbHVlIjoiWVJCb2hlWmxyNXpxU08rbEZwOXNxSmdCTE5DRDduTGEwaFB0QlpSQ1BrNXY2cVR5QzFRcVp1SFlZaFY4dVY2WlZvY0tPMjMzbG5UcStqcTJmUDdQZFcrRWJNUHk0em9Jcy94bkVsbUFMdFRNZytCdmlieExmbEdZZmwxTHl3Tk8iLCJtYWMiOiI3MDg3M2Q0NjMyZTJmZjE3ZjNlZGVhYjY1OGY5M2YxNDlkZmMyMDFhMzZmYTVmMGEzOWExMTlmYzVhYTI3YzI4IiwidGFnIjoiIn0%3D; aqarat_session=eyJpdiI6IkYwSjNmZUxGWEZEWHBzdHl3cGo4VkE9PSIsInZhbHVlIjoiMW1WUFAzS2lldFE0YUREaHBBUTJiM0R1aHREZjBTdzZBVGJFOVhRajZpMVlSd29ZMFBKWlJTTkRhcTRHSElQM2V6NFlIcnZUOG1vV3pUYmxPaHFsbFR1K0w0SlhlQ1FMbHdkb1lSM2RRdjJHOHJGYUR0N1pnVzhrUFg2UXRRc3ciLCJtYWMiOiI3MDYwNjRlY2I1MDc0NDFkOWVhMzNhMDIwYTdjZjI4NjI3MDZiYTlkNDQ4YzUzZjViYjQ4MjQ1OTk2NTdmM2MzIiwidGFnIjoiIn0%3D' \
  -F 'keyword=القصيم' \
  -F 'per_page=100' \
  -F 'page=1'