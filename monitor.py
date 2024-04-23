import time
import docker

client = docker.from_env()

while True:
    containers = client.containers.list()
    
    for container in containers:
        if 'python_container' in container.name:
            stats = container.stats(stream=False)
            uptime = time.time() - stats['created']
            
            if uptime > 3600:
                container.stop()
                print("Process aborted")
    
    time.sleep(120)