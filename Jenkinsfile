pipeline {
    environment {
        registry = "5095025250950252/coinapi"
        registryCredential = '5095025250950252'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Cloning the git') {
            steps{
                git 'https://github.com/mouhebgit/coinapi.git'
            }
        }
        
        stage('Building image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                            }
            }
    }
        stage ('Deploying image') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Cleaning up') {
            steps{
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }   
}
