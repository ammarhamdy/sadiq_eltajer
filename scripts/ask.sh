#!/usr/bin/env bash

curl --path-as-is -k -X GET 'https://sadiq-eltajer.sa/api/smart-assistant/ask' \
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
  -H 'Priority: u=0' \
  -H 'Te: trailers' \
  -H 'Connection: keep-alive' \
  -b 'XSRF-TOKEN=eyJpdiI6IjcrNXVRN3dUbEJHQzA4T2JuaGtzUnc9PSIsInZhbHVlIjoiOWpPL21XUVBRaHRzVitJUDcvZ1dOb0N0cDFjMUVLYXcwRXF1bmViQXNqMTVHSjNESFpLTHQ3SldkUTJQN2J0S3NTdEUvLzZOV2g3UC9UQ1c3RHJ2U29RaWJDNlBDbWtabnUrRmozcE1vN0tGSnlJNnV5azRZMGFUL0VidnorejciLCJtYWMiOiI2YmMwZmE3ZGUyMTU5NjNiNjU1OTg0ZDkxODIzYWU3N2IzOWE0ZGI3NjJmNmE4ZjA0MTIyYTZmZmFmOTA5MzdiIiwidGFnIjoiIn0%3D; aqarat_session=eyJpdiI6Ik4xanZlWTBhU29zOVIwOXNSN3R0SEE9PSIsInZhbHVlIjoiYnFuS1JoVG81ZmdBa1V2STBlWCtMRHltdVI1U2ZvUFllc2pFTXlQUkVGd1hSejgwRmtzUlF1VVVzZ04ydlZBSlVyVElJWDh1SXM0MHZpQzJnRnQ2NGM4c1lxODZCUnhOT0dXZ01mVUpodlkrby9XQVZrNEhBVG5ZZ3o0b2ErWm4iLCJtYWMiOiIxYmJiYThhMTk0NDM1NDY3ZmQwMjE0NDIzMTZmZDc0NDVhZDNmODNhZGQ2YTQwOTRkZmRmYWE1ZTM3NmU0YmZhIiwidGFnIjoiIn0%3D' \
  -F 'prompt=شالية بحي النقيب شمال شرق بريدة' \
  -F 'max_completion_tokens=1700' \
  -F 'current_search_payload={
    "intent":"unsupported",
    "target_object":"unknown",
    "strategy":"none",
    "area":null,
    "city":null,
    "neighborhood":null,
    "classification":null,
    "type":null,
    "classification_type":null,
    "min_price":null,
    "max_price":null,
    "rooms":null,
    "baths":null,
    "min_area":null,
    "max_area":null,
    "plot_number":null,
    "plate_number":null,
    "land_number":null,
    "exclude_negotiable":null,
    "only_negotiable":null,
    "sort_by":null,
    "sort_order":null,
    "top_result_mode":null,
    "title":null
  }'