pipeline {
    agent {
        docker {
            image 'python:3.10'   // Official Python image from DockerHub
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                  python --version
                  pip install -r requirements.txt || true
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -v'
            }
        }

        stage('Run App') {
            steps {
                sh 'python main.py'
            }
        }
    }
}
