docker run docker_tutorial_postgres:latest --name postgres --env-file ./vars.env --expose 5432
docker run docker_tutorial:latest --name app --expose 3031
docker run docker_tutorial_nginx:latest --name nginx --expose 80