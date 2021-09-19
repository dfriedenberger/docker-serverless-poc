import docker



PREFIX = "frittenburger/serverless/"


def call_serverless(name,command):
    client = docker.DockerClient()

    docker_image = "frittenburger/serverless/{}".format(name)
    container_name = "frittenburger_serverless_{}".format(name)

    #build image
    path = "/root/dev/serverless/{}".format(name)
    #print("build",path,docker_image)
    client.images.build(path = path, tag=docker_image)

    #start image
    container = client.containers.run(image = docker_image, name = container_name , detach =True, remove = True)
    #print("status",container.status)

    #container = client.containers.get(container_name)
    res = container.exec_run(command,stream=False, demux=False)
    data = res.output.decode().splitlines()

    #stop container
    container.stop()
    #print("status",container.status)

    return data





