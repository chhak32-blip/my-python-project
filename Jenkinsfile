pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root'  // Ensure pip works with no permission issues
        }
    }

    stages {
        stage('📋 Preparation') {
            steps {
                echo '🚀 Starting Jenkins Pipeline for Python Application'
                echo "📂 Workspace: ${env.WORKSPACE}"
                echo "🏗️ Build Number: ${env.BUILD_NUMBER}"
            }
        }

        stage('📥 Checkout') {
            steps {
                echo '📥 Checking out source code...'
                checkout scm
            }
        }

        stage('🐍 Python Environment') {
            steps {
                echo '🐍 Checking Python version...'
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }

        stage('📦 Install Dependencies') {
            steps {
                echo '📦 Installing required packages...'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('🧪 Run Tests') {
            steps {
                echo '🧪 Running unit tests...'
                sh 'python3 test_app.py'
            }
        }

        stage('🏃‍♂️ Run Application') {
            steps {
                echo '🏃‍♂️ Executing app.py...'
                sh 'python3 app.py'
            }
        }

        stage('📊 Generate Report') {
            steps {
                echo '📊 Generating build report...'
                sh 'ls -la'
            }
        }
    }

    post {
        success {
            echo '🎉 Build and tests succeeded!'
        }
        failure {
            echo '❌ Build failed. Please check the logs.'
        }
    }
}
