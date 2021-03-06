# big-data-covid

# Build images for SPARK and KAFKA
Windows : 
```
./build-images.bat
```

Linux:
```
./build-images.sh
```

# Create custom network

```
docker network create data-net
```

# Setup hive server
inside folder apache-hive-docker run the following command :  
```
docker-compose up -d
```

after this command enter inside hive-server container : 

```
docker exec -it hive-server hive
```

```
use default;
```

```
CREATE TABLE covid (id STRING,lat STRING, lng STRING, aff_date STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ';' STORED AS TEXTFILE; 
```

# Launch kafka cluster  
inside folder apache-kafka-docker run the following command :  
```
docker-compose up -d
```

# Enter to kafka cluster
enter to docker container using the following command:  

```
docker exec -it kafka-server bash
```

# Create topic 
```
bin/kafka-topics.sh --create --topic covid-new-cases --bootstrap-server localhost:9092  
```

check if topic is created  
```
bin/kafka-topics.sh --describe --topic covid-new-cases --bootstrap-server localhost:9092    
```

# Launch spark cluster 

keep terminal of producer running and open new terminal   

cd into apache-spark-docker folder and run  
```
docker-compose up -d  
```
# Submit your app to spark cluster
enter to spark master container using the following command :  
```
docker exec -it spark-master bash  
```

then run inside the container the following command :  
```
bin/spark-submit --jars /opt/spark-apps/spark-streaming-kafka-0-8-assembly_2.11-2.1.0.jar /opt/spark-apps/transformer.py
```
# Build heatmap

inside map-consumer folder run the following command : 

```
docker build -t heat-map-consumer .
```
then run the container
```
docker-compose up -d
```

# Produce data
inside data-producer run the command : 

```
docker build -t data-producer .  
```
then run the container 

```
docker-compose up
```


# Try now
go to http://localhost:5000/demo and you'll see the map 

![Heat Map](https://raw.githubusercontent.com/abdilahboutizwa/big-data-covid/main/map-consumer/public/demo/demo.png?token=AESZIZZCTFM2H2L545CCQTLAH4FPA)

# Contributors
- [Anouar Bouchal](https://github.com/anouar-bouchal)
- [Abdelilah Boutizoua](https://github.com/abdilahboutizwa)