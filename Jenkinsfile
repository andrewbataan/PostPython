pipeline {
    agent any  // Ejecuta en cualquier agente disponible

    environment {
        // Asignar las credenciales de Docker Hub como variables de entorno
        DOCKER_USERNAME = credentials('docker-hub-username')  // Este es el ID de la credencial que contiene tu usuario de Docker Hub
        DOCKER_PASSWORD = credentials('docker-hub-password')  // Este es el ID de la credencial que contiene tu contraseña o token
        IMAGE_NAME = 'andrewbataan/postpython' // Reemplaza con tu nombre y nombre de la imagen
        REPO_URL = 'https://github.com/andrewbataan/PostPython.git' // URL de tu repositorio
    }

    stages {
        stage('Clonar código') {
            steps {
                git branch: 'main', url: "${REPO_URL}"  // Clona el repositorio en la rama main
            }
        }

        stage('Construir imagen Docker') {
            steps {
                script {
                    // Construir la imagen Docker
                    docker.build("${IMAGE_NAME}")  // Crea la imagen con el nombre que especificaste
                }
            }
        }

        stage('Iniciar sesión en Docker Hub') {
            steps {
                script {
                    // Autenticación con Docker Hub usando las credenciales almacenadas
                    docker.login(
                        registryUrl: 'https://index.docker.io/v1/'
                        username: "${DOCKER_USERNAME}", 
                        password: "${DOCKER_PASSWORD}"
                    )
                }
            }
        }

        stage('Subir imagen a Docker Hub') {
            steps {
                script {
                    // Subir la imagen al Docker Hub
                    docker.image("${IMAGE_NAME}").push()  // Empuja la imagen al repositorio Docker Hub
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado con éxito!'
        }
        failure {
            echo 'El pipeline falló'
        }
    }
}
