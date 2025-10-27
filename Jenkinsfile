pipeline {
    agent any

    environment {
        TERRAFORM_PATH = "C:\\terraform/terraform.exe"
        // Cambia si lo tienes en otro lugar
    }

    stages {
        stage('Preparar entorno') {
            steps {
                echo 'Inicializando Terraform...'
                bat "${env.TERRAFORM_PATH} init"
            }
        }

        stage('Validar configuración') {
            steps {
                echo 'Validando sintaxis de Terraform...'
                bat "${env.TERRAFORM_PATH} validate"
            }
        }

        stage('Simular plan') {
            steps {
                echo 'Simulando infraestructura...'
                bat "${env.TERRAFORM_PATH} plan -out=plan.txt"
            }
        }

        stage('Aplicar simulacion') {
            steps {
                echo 'Creando infraestructura simulada (archivo)...'
                bat "${env.TERRAFORM_PATH} apply -auto-approve"
            }
        }

        stage('Preparar entorno2') {
            steps {
                echo "Creando entorno virtual..."
                bat '"C:\\Users\\Angela\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }        
        stage('Ejecutar script1') {
            steps {
                echo "Ejecutando script 1..."
                bat 'venv\\Scripts\\activate && python proyecto.py'
            }
        }
    }
    
    post {
        success {
            archiveArtifacts artifacts:'*-txt, plan.txt', fingerprint: true
            echo '✅ Infraestructura simulada creada correctamente.'
        }
        failure {
            echo '❌ Error en e pipeline o en la configuracion Terraform.'
        }
    }
}



