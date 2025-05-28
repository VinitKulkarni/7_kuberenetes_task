### Create ec2 machine in aws:
```sh
type: t2.medium
volume_size: 30gb
```

### Ports allowed in security group:
```sh
3000  -> frontend
5000  -> backend
27017 -> mongodb
8081  -> mongodb-express
30007 -> nodeport_for_frontend
```

### Install docker in ec2:
```sh
sudo apt update
sudo apt install docker.io -y
usermod -aG docker $USER   (exit and login in ec2)
docker images
```

### To install minikube and kubectl:
```sh
minikube_ link : https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download
kubectl_link   : https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux
```

### Build & push docker images:
```sh
cd frontend
docker build -t vinitkulkarni/express-frontend:5.2

cd backend
docker build -t vinitkulkarni/flask-backend:5.3

docker login

docker push vinitkulkarni/express-frontend:5.2
docker push vinitkulkarni/flask-backend:5.3
```

### To create deployment and svc:
```sh
kubectl apply -f mongo.yml
kubectl apply -f mongo-express.yml
kubectl apply -f backend.yml
kubectl apply -f frontend.yml

To check deployment and svc:
kubectl get all 
kubectl get pods
kubectl get deployments
kubectl get svc

To check the logs of pod:
kubectl logs <pod_id>
```

### Port forwarding:
```sh
syntax: kubectl port-forward --address 0.0.0.0 svc/<service-name> <nodeport>:<container_port>
kubectl port-forward --address 0.0.0.0 svc/frontend 30007:3000
kubectl port-forward --address 0.0.0.0 svc/backend 5000:5000
kubectl port-forward --address 0.0.0.0 svc/mongo 27017:27017
kubectl port-forward --address 0.0.0.0 svc/mongo-exp 8081:8081
```

### minikube basic commands used:
```sh
minikube start
minikube status
minikube stop
```
