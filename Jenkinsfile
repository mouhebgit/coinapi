pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub')
	}

	stages {

		stage('Build') {

			steps {
				sh './configure && make && echo mouhebnn123. | sudo -S docker build -t mouhebgit/coinapi:latest .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push 5095025250950252/mycoinapp:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
