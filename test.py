from src.docker_util import call_serverless


command = "echo {}".format("Hello World!")
result = call_serverless("hello_world",command)
print(command," => ",result)