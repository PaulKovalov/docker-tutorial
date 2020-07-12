docker run --name postgres --env-file ./vars.env --expose 5432 docker_tutorial_postgres:latest
docker run --name app --expose 3031 docker_tutorial:latest
docker run --name nginx --expose 80 docker_tutorial_nginx:latest