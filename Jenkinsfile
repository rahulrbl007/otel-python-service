pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "rahulrbl007/otel-python-service:latest"
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/rahulrbl007/otel-python-service.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([string(credentialsId: 'docker-hub-pass', variable: 'DOCKERHUB_PASS')]) {
                    sh """
                    echo $DOCKERHUB_PASS | docker login -u rahulrbl007 --password-stdin
                    docker push $DOCKER_IMAGE
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}

