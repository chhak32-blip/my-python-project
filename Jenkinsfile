pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root'
        }
    }
    
    stages {
        stage('📋 Preparation') {
            steps {
                echo '🚀 Starting Jenkins Pipeline for Python Application'
                echo '📂 Workspace: ' + env.WORKSPACE
                echo '🏗️  Build Number: ' + env.BUILD_NUMBER
            }
        }
        
        stage('📥 Checkout') {
            steps {
                echo '📥 Checking out source code...'
                checkout scm
                echo '✅ Source code checked out successfully'
            }
        }
        
        stage('🐍 Python Environment') {
            steps {
                echo '🐍 Checking Python environment...'
                sh 'python3 --version'
                sh 'pip3 --version'
                echo '✅ Python environment ready'
            }
        }
        
        stage('🧪 Run Tests') {
            steps {
                echo '🧪 Running unit tests...'
                sh 'python3 test_app.py'
                echo '✅ All tests passed!'
            }
        }
        
        stage('🏃‍♂️ Run Application') {
            steps {
                echo '🏃‍♂️ Running the main application...'
                sh 'python3 app.py'
                echo '✅ Application executed successfully!'
            }
        }
    }
    
    post {
        success {
            echo '🎉 Pipeline completed successfully!'
        }
    }
}
