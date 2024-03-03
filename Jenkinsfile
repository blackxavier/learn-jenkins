pipeline {
    agent { 
        node {
            label 'docker-temp-1'
            }
      }
    stages {
        stage('Build and Test') {
            steps {
                // Set up your virtual environment and install dependencies
                script {
                    sh 'python -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }

                // Run your Django migrations and tests
                script {
                    sh 'python manage.py migrate'
                    sh 'python manage.py test'
                }
            }
        }
        stage('Docker Build') {
            steps {
                // Build Docker image
                script {
                    sh 'docker build -t project .'
                }
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}