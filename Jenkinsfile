pipeline {
    agent any
    environment {
        IMAGE_NAME = 'davidgamz/wog'
        IMAGE_TAG = 'v1.0'
    }
    stages {
        stage('Clean UP') {
            steps {
                deleteDir()
            }
        }
        stage('Clone Repo') {
            steps {
                sh "git clone https://github.com/DavidGamZu/wog.git wog"
            }
        }
        stage('Read and Increment Build Number') {
            steps {
                script {
                    def versionsFile = 'wog/version.txt'

                    // Read the current build number
                    def currentBuildNumber = 0
                    if (fileExists(versionsFile)) {
                        currentBuildNumber = readFile(versionsFile).trim().toInteger()
                    }

                    // Increment the build number
                    def newBuildNumber = currentBuildNumber + 1

                    // Write the new build number back to the file
                    writeFile file: versionsFile, text: "${newBuildNumber}"

                    // Set the new build number as an environment variable for use in Docker tag
                    env.BUILD_NUMBER = newBuildNumber.toString()
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                dir('wog') {
                    // Create and activate a virtual environment
                    sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Docker') {
            steps {
                script {
                    dir('wog') {
                        sh "docker-compose up --build -d"
                    }
                }
            }
        }
        stage('E2E') {
            steps {
                dir('wog/test') {
                    sh '''
                    . ../venv/bin/activate
                    python e2e.py
                    '''
                }
            }
        }
        stage('Finalize') {
            steps {
                dir('wog') {
                    sh "docker-compose down"
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    def imageTag = "${env.BUILD_NUMBER}"

                    // Tag and push the Docker image with the new build number
                    sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:${imageTag}"
                    sh "docker push ${IMAGE_NAME}:${imageTag}"
                }
            }
        }
    }
}
