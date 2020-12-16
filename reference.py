import docker
client = docker.from_env()
#containers = client.containers.list()
#container_list = [container.name for container in containers if 'rabbitmq' in container.name]
#print(container_list)

#print(client.containers.list(all=True))
networks = client.networks.list()
dcn_network = [network for network in networks if 'dcn' in network.name][0]
print(dcn_network)
print(dcn_network.name)
