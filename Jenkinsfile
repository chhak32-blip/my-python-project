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
                sh 'find . -name "*.py" -type f || echo "No Python files found"'
            }
        }
        
        stage('🐍 Install Python') {
            steps {
                echo '🐍 Installing Python...'
                sh '''
                    # Update package list
                    apt-get update
                    
                    # Install Python
                    apt-get install -y python3 python3-pip
                    
                    # Verify installation
                    python3 --version
                    pip3 --version
                '''
                echo '✅ Python installed successfully'
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
