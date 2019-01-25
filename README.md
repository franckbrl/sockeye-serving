# sockeye-serving
Sockeye server based on mxnet-model-server

## Getting Started With Docker
Pull the latest Docker image:
```bash
docker pull jwoo11/sockeye-serving
```

Start the server:
```bash
docker run -itd --name mms -p 8080:8080  -p 8081:8081 -v /tmp/models/:/models jwoo11/sockeye-serving serve
```

Try making some requests using a remote model:
```bash
# URL of a remote machine translation model
URL="https://www.dropbox.com/s/pk7hmp7a5zjcfcj/zh.mar?dl=1"

# load the model
curl -X POST "http://localhost:8081/models?synchronous=true&initial_workers=1&url=${URL}"

# show the status of the ZH model
curl -X GET "http://localhost:8081/models/zh"

# translate a sentence
curl -X POST "http://localhost:8080/predictions/zh" -H "Content-Type: application/json" \
    -d '{ "text": "我的世界是一款開放世界遊戲，玩家沒有具體要完成的目標，即玩家有超高的自由度選擇如何玩遊戲" }'
```

## Loading a Local Model
Download the example model archive file (MAR):
* https://www.dropbox.com/s/pk7hmp7a5zjcfcj/zh.mar?dl=0

Move the MAR file to `/tmp/models` and start the server as before.
You may need to stop and remove the container from a previous run.

Load the local model and try some requests. You'll have to unload the model first, if it's already loaded:
```bash
curl -X DELETE "http://localhost:8081/models/zh"
curl -X POST "http://localhost:8081/models?initial_workers=1&url=zh.mar"
```

It's also possible to use the extracted MAR as the URL:
```bash
unzip -d /tmp/models/zh zh.mar
curl -X POST "http://localhost:8081/models?initial_workers=1&url=zh"
```

For more information on MAR files and the built-in REST APIs, see:
* https://github.com/awslabs/mxnet-model-server/tree/master/docs
