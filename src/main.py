import sys
import docker

if __name__ == "__main__":
    inputfile = sys.argv[1]

    client = docker.from_env()

    with open(inputfile) as f:
        lines = f.readlines()
        for line in lines:
            client.images.pull(line.strip())