curl -X POST -H "Content-Type: application/json" --data '
  {"name": "mongo-atlas-sink",
   "config": {
     "connector.class":"com.mongodb.kafka.connect.MongoSinkConnector",
     "tasks.max":"1",
     "topics":"evh-adxevents-aurlt7utqtfhs",
     "connection.uri":"mongodb+srv://anuraAdmin:8W5fBmsQ58azE83@anuradb.rrmor6f.mongodb.net/?retryWrites=true&w=majority",
     "database":"EventHubDemoooo",
     "collection":"Sink",
     "key.converter":"org.apache.kafka.connect.json.JsonConverter",
     "key.converter.schemas.enable":false,
     "value.converter":"org.apache.kafka.connect.json.JsonConverter",
     "value.converter.schemas.enable":false
}}' http://localhost:8083/connectors -w "\n"