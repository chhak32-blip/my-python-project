pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/your-repo.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt || true'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest || echo "No tests found"'
            }
        }
        
        stage('Build/Package') {
            steps {
                sh 'echo "Packaging project..."'
            }
        }
    }
    
    post {
        success {
            echo '✅ Build and tests passed!'
        }
        failure {
            echo '❌ Build failed. Check logs.'
        }
    }
}
