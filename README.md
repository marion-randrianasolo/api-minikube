# API Minikube

Ce projet consiste en la création d'une API Flask déployée sur Minikube, avec des fonctionnalités telles que le stockage de données en base, des routes pour tester la résilience, et une route pour simuler une utilisation intensive du CPU.

## Contenu du Projet

- **app.py:** Fichier principal contenant le code de l'API Flask.
- **Dockerfile:** Fichier pour la création de l'image Docker.
- **deployment.yaml:** Fichier de déploiement Kubernetes pour l'application.
- **service.yaml:** Fichier de service Kubernetes pour l'application.
- **ingress.yaml:** Fichier Ingress Kubernetes pour rendre l'application accessible depuis l'extérieur.
- **hpa.yaml:** Fichier Horizontal Pod Autoscaler (HPA) pour l'évolutivité automatique basée sur les ressources.

## Instructions d'Utilisation

### Prérequis

- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

### Déploiement de l'Application

1. Démarrez Minikube : `minikube start`
2. Construisez l'image Docker : `docker build -t mrandrianasolo/api-minikube:latest .`
3. Poussez l'image vers Docker Hub : `docker push mrandrianasolo/api-minikube:latest`
4. Appliquez les fichiers de déploiement : `kubectl apply -f deployment.yaml -f service.yaml -f ingress.yaml -f hpa.yaml`
5. Vérifiez le statut du déploiement : `kubectl get pods`

### Accès à l'Application

1. Obtenez l'adresse IP de l'Ingress : `minikube ip`
2. Ajoutez cette adresse au fichier hosts avec le nom spécifié dans le fichier Ingress (par exemple, `192.168.59.100 localhost`).
3. Accédez à l'application via le navigateur : [http://localhost](http://localhost)

### Fonctionnalités de l'API

- **/store_data (POST):** Stocke des données en base de données.
- **/read_data (GET):** Lit des données depuis la base de données.
- **/exit (GET):** Ferme le serveur Flask.
- **/cpu (GET):** Simule une utilisation intensive du CPU.

### Base de Données

1. Déployez une base de données : [Instructions ici]
2. Configurez la base de données via les variables d'environnement ou ConfigMap.

### Routes Additionnelles

- **POST /store_db (POST):** Stocke des données en base de données.
- **GET /read_db (GET):** Lit une donnée depuis la base de données.

## Auteurs

- [Votre Nom]

N'hésitez pas à contribuer, signaler des problèmes ou proposer des améliorations !


## Auteurs

- Fatima-Zahra BOUHASSOUN
- Alyssa BOYER
- Marion RANDRIANASOLO
- Manelle LAAMARTI
  

N'hésitez pas à contribuer, signaler des problèmes ou proposer des améliorations !
