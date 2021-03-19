pipeline {
    agent any

    stages {
        stage('Compile') {
            steps {
               bat 'python lst.py'
            }
        }
      stage('Testing Stage'){
        steps{
          bat 'python Testcalc.py'
        }
      }
      stage ('Deployment Stage'){
        steps{
          echo 'Deployment successful'
        }
      }
    }
}
