pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'cricket-game'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }
        
       stage('Test') {
    steps {
        echo 'No tests to run for this project'
    }
}
        
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                bat "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest"
                // Example deployment step - adjust according to your needs
                // bat "docker run -d -p 8000:8000 --name cricket-game-container ${DOCKER_IMAGE}:latest"
            }
        }
    }
    
    post {
        always {
            // Clean up - remove unused images
            bat "docker rmi ${DOCKER_IMAGE}:${DOCKER_TAG} || echo 'Failed to remove image'"
        }
        success {
            echo 'Build and deployment successful!'
        }
        failure {
            echo 'Build or deployment failed'
        }
    }
}
