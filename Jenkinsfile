pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                  python --version
                  pip install --upgrade pip --user
                  if [ -f requirements.txt ]; then pip install --user -r requirements.txt; fi
                  pip install --user pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m pytest -v'
            }
        }

        stage('Run App') {
            steps {
                sh 'python main.py'
            }
        }
    }
}
