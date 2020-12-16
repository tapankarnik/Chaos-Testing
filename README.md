# Chaos Testing Subsystem for Data Center Network

# Docker Build

Run the following the build the docker image for the CTS

    docker build -t cts .

# Testing 

The CTS accepts POST requests on port 5021. Run the DCN StubSend a POST request with a JSON body with one parameter 'component_id'.
Sample JSON

{
    'component_id':'worker2'
}

# Testing with the DCN

Run the DCN and replace 'worker2' from above to one of the components in the DCN while sending the POST request.
