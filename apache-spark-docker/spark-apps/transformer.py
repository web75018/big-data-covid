#!/usr/bin/python3                                                                                                      
                                                                                                                        
from pyspark import SparkContext                                                                                        
from pyspark.sql import SparkSession                                                                                    
from pyspark.streaming import StreamingContext                                                                          
from pyspark.streaming.kafka import KafkaUtils
                                                                                                                        
def handle_rdd(rdd):                                                                                                    
    if not rdd.isEmpty():
        global ss                                                                                                       
        df = ss.createDataFrame(rdd, schema=['text', 'words', 'length'])                                                
        print("=========================================================")
        print(df.show())                                                                                                                                                                                                      
        print("=========================================================")
        # df.write.saveAsTable(name='default.covid_cases', format='hive', mode='append')                                       


sc = SparkContext(appName="Something")                                                                                     
ssc = StreamingContext(sc, 5)                                                                                           
                                                                                                                        
ss = SparkSession.builder.appName("covid streaming").getOrCreate()
        # .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \                                                    
        # .config("hive.metastore.uris", "thrift://localhost:9083") \                                                     
        # .enableHiveSupport() \                                                                                          
                                                                                                                        
# ss.sparkContext.setLogLevel('WARN')                                                                                     
                                                                                                                        
ks = KafkaUtils.createDirectStream(ssc, ['covid-new-cases'], {'metadata.broker.list': 'kafka-server:9092'})                       
                                                                                                                        
lines = ks.map(lambda x: x[1])                                                                                          
                                                                                                                        
transform = lines.map(lambda data: (data, int(len(data.split())), int(len(data))))                                  
                                                                                                                        
transform.foreachRDD(handle_rdd)                                                                                        
                                                                                                                        
ssc.start()                                                                                                             
ssc.awaitTermination()