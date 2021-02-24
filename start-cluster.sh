echo "\n============================================"
echo "start hive server"
echo "\n============================================"
cd apache-hive-docker
docker-compose up -d

docker exec -it hive-server hive


