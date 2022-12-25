# HTTP-S-Endpoint-Monitor

This code defines a function check_endpoint that sends a GET request to the specified endpoint and searches for a given pattern in the response. If the request is successful and the pattern is found, it prints a message in green indicating that the endpoint is up and the pattern was found. If the request is successful but the pattern is not found, it prints a message in red indicating that the endpoint is up but the pattern was not found. If the request fails, it prints a message in red indicating that the endpoint is down.

The script also defines two helper functions, print_green and print_red, that print text in green and red, respectively.

At the end of the script, the code defines a list of endpoints to check and prompts the user to enter the pattern to search for. It then enters an infinite loop in which it repeatedly checks each endpoint in the list using the check_endpoint function and waits for 60 seconds before checking the endpoints again. This allows the script to continuously monitor the endpoints and report any changes in their status or the presence of the pattern.
