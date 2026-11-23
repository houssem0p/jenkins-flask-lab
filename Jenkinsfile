pipeline {
    agent any

    environment {
        IMAGE_NAME     = 'jenkins-flask-lab'
        CONTAINER_NAME = 'jenkins-flask-app'
        APP_PORT       = '8081'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is available in the workspace.'
            }
        }

        stage('Build') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%BUILD_NUMBER% .'
            }
        }

        stage('Test') {
            steps {
                bat 'docker run --rm %IMAGE_NAME%:%BUILD_NUMBER% pytest -v'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    docker rm -f %CONTAINER_NAME% 2>nul || exit 0
                    docker run -d --name %CONTAINER_NAME% -p %APP_PORT%:8000 -e APP_VERSION=%BUILD_NUMBER% %IMAGE_NAME%:%BUILD_NUMBER%
                '''
            }
        }

        stage('Verify') {
            steps {
                bat 'curl.exe --fail --retry 10 --retry-delay 2 http://localhost:%APP_PORT%/health'
                bat 'curl.exe --fail http://localhost:%APP_PORT%/'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the stage that reported an error.'
        }
    }
}