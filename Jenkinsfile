pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               bat 'pipenv --python python3 sync'
            }
        }
        stage('Test') {
            steps {
               bat 'pipenv run pytest'
            }
        }
        stage('Package') {
	    when{
		    anyOf{ branch "master" ; branch 'release' }
	    }
            steps {
               bat 'zip -r sbdl.zip lib'
            }
        }
	stage('Release') {
	   when{
	      branch 'release'
	   }
           steps {
              bat "scp -i /home/prabatant/cred/edge-node_key.pem -o 'StrictHostKeyChecking no' -r sbdl.zip log4j.properties sbdl_main.py sbdl_submit.bat conf prabatant@40.117.123.105:/home/prabatant/sbdl-qa"
           }
        }
	stage('Deploy') {
	   when{
	      branch 'master'
	   }
           steps {
               bat "scp -i /home/prabatant/cred/edge-node_key.pem -o 'StrictHostKeyChecking no' -r sbdl.zip log4j.properties sbdl_main.py sbdl_submit.bat conf prabatant@40.117.123.105:/home/prabatant/sbdl-prod"
           }
        }
    }
}
