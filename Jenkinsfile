pipeline {
    agent any

    stages {
        stage('Compile') {
            steps {
               bat 'python calc/lst.py'
            }
        }
      stage('Testing Stage'){
        steps{
          bat 'python calc/test/Testcalc.py'
        }
      }
      stage ('Deployment Stage'){
        steps{
          echo 'Deployment successful'
        }
      }
    }
}
