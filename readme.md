## Fast API

**Application Running Command**

`uvicorn sample:app --reload --host 0.0.0.0 --port 80`

**_Basic Urls that you can try out_**

```sh
http://localhost/docs#/default/
http://localhost/

```

By using the first API on Browser it will show all the APIs list which you have been developing. Also it Shows the methods of operation like GET, POST, PUT etc , the Fastapi have one of the dashboard looks like an REST API dashboard that you can execute and test the your fast apis.

### Docker Image

```sh
docker pull saikrish12345/fastapi1:1
```

### Docker running command

```sh
docker run -d -p 80:80 saikrish12345/fastapi1:1
```
