# devops-cources
## Run application
```
cd compose
docker-compose -f app_v4.yml up --quiet-pull -d --no-deps --build
```
## Test application
```
for i in {1..10}; do curl http://localhost:8082; sleep 1; done
```
