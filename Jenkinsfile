pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub')
	}

	stages {

		stage('Build') {

			steps {
				sh 'docker build -t 5095025250950252/coinapi:latest .'

			}
		}
		stage('fetch') {

			steps {
				sh 'docker images'

			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push 5095025250950252/coinapi:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
