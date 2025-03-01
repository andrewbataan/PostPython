pipeline {
    agent any  // Ejecuta en cualquier agente disponible

    environment {
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
