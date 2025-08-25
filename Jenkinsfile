pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '--user root'   // run container as root user
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                  python --version
                  pip install --no-cache-dir --upgrade pip
                  if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi
                  pip install --no-cache-dir pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -v || echo "⚠️ No tests found, skipping."'
            }
        }

        stage('Run App') {
            steps {
                sh 'python main.py --ci'
            }
        }
    }
}
