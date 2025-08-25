pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-u root'   // run container as root user
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                  python --version
                  pip install --upgrade pip
                  if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                  pip install pytest
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
