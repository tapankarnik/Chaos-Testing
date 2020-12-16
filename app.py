import docker
from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

def validate_component_id(component_id):
    if len(component_id)>20 or len(component_id)==0 or component_id == None:
        return True
    else:
        return False

@app.route('/kill', methods=['POST'])
def kill_container():

    if request.is_json:
        data = request.get_json()
        try:
            if validate_component_id(data['component_id']):
                raise Exception('Invalid Component ID')

        except Exception:
            return "Invalid Input", 400
        
        component_id = data['component_id']

        client = docker.from_env()
        containers = client.containers.list()
        container_kill_list = [container for container in containers if component_id in container.name]
        
        try:
            if len(container_kill_list) == 0:
                raise Exception('Requested Component is not running')
            for container in container_kill_list:
                container.stop()
                print("Killed Container "+str(container.name))
        except Exception:
            return b"Error killing the requested component. Already killed or does not exist.", 400

        return b"OK", 200

    else:
        return b"Not a JSON input", 400

@app.route('/disconnect', methods=['POST'])
def disconnect_container():
    if request.is_json:
        data = request.get_json()
        try:
            if validate_component_id(data['component_id']):
                raise Exception('Invalid Component ID')

        except Exception:
            return "Invalid Input", 400

        component_id = data['component_id']

        client = docker.from_env()
        containers = client.containers.list()
        container_disconnect_list = [container for container in containers if component_id in container.name]

        networks = client.networks.list()
        dcn_network = [network for network in networks if 'dcn' in network.name][0]

        try:
            if len(container_disconnect_list)==0:
                raise Exception('Requested Component is not running.')

            for container in container_disconnect_list:
                dcn_network.disconnect(container)
                print("Disconnected Container "+str(container.name))
        except Exception:
            return b"Error disconnecting the requested component. Already disconnected or does not exist.", 400
        
        return b"OK", 200

    else:
        return b"Not a JSON input", 400

@app.route('/reconnect', methods=['POST'])
def reconnect_container():
    if request.is_json:
        data = request.get_json()
        try:
            if validate_component_id(data['component_id']):
                raise Exception('Invalid Component ID')

        except Exception:
            return "Invalid Input", 400

        component_id = data['component_id']

        client = docker.from_env()
        containers = client.containers.list()
        container_reconnect_list = [container for container in containers if component_id in container.name]

        networks = client.networks.list()
        dcn_network = [network for network in networks if 'dcn' in network.name][0]

        try:
            if len(container_reconnect_list)==0:
                raise Exception('Requested Component is not running.')

            for container in container_reconnect_list:
                dcn_network.connect(container)
                print("Connected Container "+str(container.name))
        except Exception:
            return b"Error connecting the requested component. Component does not exist.", 400
        
        return b"OK", 200

    else:
        return b"Not a JSON input", 400


if __name__ == "__main__":
    print("Starting Chaos Testing Subsystem")
    app.run(host='0.0.0.0', port=5021, debug=True)
