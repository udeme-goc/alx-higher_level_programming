#!/bin/bash
# Send GET request using curl with custom header and display body of response
curl -sH "X-School-User-Id: 98" "$1"
