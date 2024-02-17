# Testing Spark Submit Locally with Docker Compose

This repository is a way for someone to be able to run spark-submit commands locally in a docker container. 


Make sure you're in the directory `spark-submit-local`

Ensure that you have Docker Desktop Working:

Build the docker container - Run:
```bash
docker build -t local-spark-submit:1.0 .
```

Run the docker container with docker-compose
```bash
docker-compose up
```

Open a separate terminal and exec into your docker container while it is still running - get the CONTAIER for the *master* container

Find the container id and then exec
```bash
docker ps 

 ~/projects/airlow-spark-k8s/spark-submit-local  docker ps
CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS          PORTS                                                                NAMES
21f541c0f478   local-spark-submit:1.0   "/bin/bash /start-sp…"   34 minutes ago   Up 41 seconds   6066/tcp, 7077/tcp, 0.0.0.0:7001->7001/tcp, 0.0.0.0:9091->8080/tcp   spark-submit-local-spark-worker-a-1
f21e3d430db6   local-spark-submit:1.0   "/bin/bash /start-sp…"   34 minutes ago   Up 41 seconds   6066/tcp, 7077/tcp, 0.0.0.0:7002->7001/tcp, 0.0.0.0:9092->8080/tcp   spark-submit-local-spark-worker-b-1
d9bd64998511   local-spark-submit:1.0   "/bin/bash /start-sp…"   34 minutes ago   Up 42 seconds   6066/tcp, 0.0.0.0:7077->7077/tcp, 0.0.0.0:9090->8080/tcp             spark-submit-local-spark-master-1
```

```bash
docker exec <CONTAINTER_ID> /bin/bash

```

You should now be at the root folder of your docker contianer and you can now run your job:
```bash
./bin/spark-submit --master spark://spark-master:7077 /opt/spark/jobs/dataframe_example.py
```

One of the issues I was haing was trying to stop the spark job once it completed. I attempted using `spark.stop()` but the issue seems to be coming from its internal UI (Jetty) during the shut down of the applicaton. This may require you to run a Ctrl + D to stop the process.


References:
https://medium.com/@SaphE/testing-apache-spark-locally-docker-compose-and-kubernetes-deployment-94d35a54f222
The above article was something that allowed a practitioned to run spark-pi, but this was an attempt to allow users to add their own custom job in the `/jobs` directory.