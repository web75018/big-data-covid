# big-data-covid

# build images 
docker build -t kafka-base ./kafka-base  
docker build -t kafka-zookeeper ./kafka-zookeeper   
docker build -t kafka-server ./kafka-server  

# setup hive server
inside folder apache-hive-docker run the following command :  

docker-compose up -d

after this command enter inside hive-server container : docker exec -it hive-server bash

CREATE TABLE covid (id INT,lat STRING, lng STRING, aff_date INT)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ';'
    STORED AS TEXTFILE;

# launch kafka cluster  
inside folder apache-kafka-docker run the following command :  

docker-compose up -d

# enter to kafka cluster
enter to docker container using the following command:  

docker exec -it kafka-server bash

# create topic 
bin/kafka-topics.sh --create --topic covid-new-cases --bootstrap-server localhost:9092  

check if topic is created  

bin/kafka-topics.sh --describe --topic covid-new-cases --bootstrap-server localhost:9092    

# produce data
bin/kafka-console-producer.sh --topic covid-new-cases --bootstrap-server localhost:9092  

# launch spark cluster 
keep terminal of producer running and open new terminal   

cd into apache-spark-docker folder and run  
docker-compose up -d  

# submit your app to spark cluster
enter to spark master container using the following command :  

docker exec -it spark-master bash  

then run inside the container the following command :  

bin/spark-submit --jars /opt/spark-apps/spark-streaming-kafka-0-8-assembly_2.11-2.1.0.jar /opt/spark-apps/transformer.py


# try now
go to the terminal where you left kafka-producer.sh command running and start typing ...

you'll see in spark terminal data that you typed