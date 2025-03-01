pipeline {
    agent any  // Ejecuta en cualquier agente disponible

    environment {
        // Configuración del Docker Hub (o tu registro de Docker)
        DOCKER_CREDENTIALS = credentials('docker-hub-credentials') // Debes configurar esto en Jenkins
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
                    // Autenticación con Docker Hub (si no quieres subir, no necesitas este paso)
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS}") {
                        // Este paso se ejecuta con las credenciales configuradas en Jenkins
                    }
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
