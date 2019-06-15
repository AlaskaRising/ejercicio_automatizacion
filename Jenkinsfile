pipeline {
  agent any

  options {
    timeout(time: 2, unit: 'MINUTES')
  }

  environment {
    ARTIFACT_ID = "miguelangel/unit_test_python:${env.BUILD_NUMBER}"
  }

  stages {
    stage('Build') {
      steps {
        script {
          dir("") {
            dockerImage = docker.build "${env.ARTIFACT_ID}"
          }
        }
      }
    }
    stage('Run unit tests') {
      steps {
        sh "docker run ${dockerImage.id} python test_pares.py -v"
      }
    }
    stage('Validate feature') {
      steps {
        script {
          dir("") {
            sh "docker run ${dockerImage.id} behave"
          }
        }
      }
    }
  }
}