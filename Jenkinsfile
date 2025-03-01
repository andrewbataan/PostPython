pipeline {
    agent any  

    environment {
        IMAGE_NAME = 'andrewbataan/postpython' 
        REPO_URL = 'https://github.com/andrewbataan/PostPython.git' 
    }

    stages {
        stage('Clone code from git') {
            steps {
                git branch: 'main', url: "${REPO_URL}"  
            }
        }

        stage('Login into Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        echo "Login succesfully"
                    }
                }
            }
        }

        stage('build image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}") 
                }
            }
        }

        stage('Upload image to docker hub') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}").push()
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline run succesfully'
        }
        failure {
            echo 'Pipeline down'
        }
    }
}

