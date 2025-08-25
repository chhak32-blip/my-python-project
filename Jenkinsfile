pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/chhak32-blip/my-python-project.git'
            }
        }

        stage('Set up Python') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt || true'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest -v'
            }
        }

        stage('Run Application') {
            steps {
                sh '. venv/bin/activate && python main.py'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline succeeded!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs.'
        }
    }
}
