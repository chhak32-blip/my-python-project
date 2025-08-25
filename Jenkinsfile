pipeline {
    agent any
    
    stages {
        stage('📋 Preparation') {
            steps {
                echo '🚀 Starting Jenkins Pipeline for Python Application'
                echo '📂 Workspace: ' + env.WORKSPACE
                echo '🏗️  Build Number: ' + env.BUILD_NUMBER
                echo '🌿 Branch: ' + env.BRANCH_NAME
            }
        }
        
        stage('📥 Checkout') {
            steps {
                echo '📥 Checking out source code...'
                checkout scm
                echo '✅ Source code checked out successfully'
            }
        }
        
        stage('🔍 Code Inspection') {
            steps {
                echo '🔍 Inspecting code structure...'
                sh 'ls -la'
                sh 'echo "Python files found:"'
                sh 'find . -name "*.py" -type f'
            }
        }
        
        stage('🐍 Python Environment') {
            steps {
                echo '🐍 Setting up Python environment...'
                sh 'python3 --version'
                sh 'which python3'
                echo '✅ Python environment ready'
            }
        }
        
        stage('📦 Install Dependencies') {
            steps {
                echo '📦 Installing dependencies...'
                sh 'pip3 install -r requirements.txt || echo "No dependencies to install"'
                echo '✅ Dependencies installed'
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
        
        stage('📊 Generate Report') {
            steps {
                echo '📊 Generating build report...'
                script {
                    def report = """
                    =====================================
                    🎉 BUILD REPORT
                    =====================================
                    📅 Date: ${new Date()}
                    🏗️  Build: ${env.BUILD_NUMBER}
                    🌿 Branch: ${env.BRANCH_NAME ?: 'main'}
                    📂 Workspace: ${env.WORKSPACE}
                    ✅ Status: SUCCESS
                    =====================================
                    """
                    echo report
                    writeFile file: 'build-report.txt', text: report
                }
                echo '✅ Report generated successfully!'
            }
        }
    }
    
    post {
        always {
            echo '🏁 Pipeline finished!'
            echo '📝 Archiving build artifacts...'
            archiveArtifacts artifacts: 'build-report.txt', fingerprint: true
        }
        success {
            echo '🎉 Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
