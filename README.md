# Chaos Testing Subsystem for Data Center Network

Part of the Chaos Testing Suite

[Data Center Network](https://github.com/tapankarnik/DCN)
[Stress Testing Subsystem](https://github.com/tapankarnik/Stress-Testing)
[Chaos Testing Subsystem](https://github.com/tapankarnik/Chaos-Testing)

# Docker Build

Run the following the build the docker image for the CTS

    docker build -t cts .

# Testing 

The CTS accepts POST requests on port 5021. Send a POST request with a JSON body with one parameter 'component_id'.
Sample JSON

    {
        'component_id':'worker2'
    }

# Testing with the DCN

Run the DCN and replace 'worker2' from above to one of the components in the DCN while sending the POST request.
