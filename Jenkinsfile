pipeline {
  agent any
  environment {
    BUILD_VERSION = sh(returnStdout: true, script: 'python3.6 -c "import mmpl_backend as mb; import sys; sys.stdout.write(mb.__version__)"')
    DOCKER_REGISTRY = '413514076128.dkr.ecr.ap-southeast-2.amazonaws.com'
    AWS_DEFAULT_REGION = 'ap-southeast-2'
    DEPLOY_USER = 'django'
  }
  stages {
    stage('Testing: Build Test Docker Image') {
      when { not { buildingTag() } }
      steps {
        sh './build-scripts/local/build.sh'
      }
    }
    stage('Testing: Run Style, Tests, Coverage') {
      when { not { buildingTag() } }
      steps {
        sh './build-scripts/local/test.sh'
        recordIssues enabledForFailure: true, blameDisabled: true, tool: flake8(pattern: '**/flake8.xml'), healthy: 10, unhealthy: 100, minimumSeverity: 'HIGH'
        junit '**/pytest.xml'
        cobertura coberturaReportFile: '**/coverage.xml'
      }
    }
    stage('Deploy: Build Production Docker Image') {
      when { allOf {
          not { buildingTag() }
          branch 'feature/implement_deploy_step'
      } }
      steps {
        withCredentials([
          file(credentialsId: 'mmpl-backend-postgres', variable: 'POSTGRES_SECRETS_PATH'),
          file(credentialsId: 'mmpl-backend-django', variable: 'DJANGO_SECRETS_PATH')
        ]) {
          sh './build-scripts/production/build.sh'
        }
      }
    }
    stage('Deploy: Push Production Image to ECR') {
      when { allOf {
          not { buildingTag() }
          branch 'feature/implement_deploy_step'
      } }
      steps {
        withCredentials([
          file(credentialsId: 'mmpl-backend-postgres', variable: 'POSTGRES_SECRETS_PATH'),
          file(credentialsId: 'mmpl-backend-django', variable: 'DJANGO_SECRETS_PATH'),
          usernamePassword(credentialsId: 'aws-ecr-pusher', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')
        ]) {
          sh './build-scripts/production/push.sh'
        }
      }
    }
    stage('Deploy: Run Ansible Deploy Script') {
      when { allOf {
          not { buildingTag() }
          branch 'feature/implement_deploy_step'
      } }
      steps {
        withCredentials([
          file(credentialsId: 'mmpl-backend-postgres', variable: 'POSTGRES_SECRETS_PATH'),
          file(credentialsId: 'mmpl-backend-django', variable: 'DJANGO_SECRETS_PATH'),
          usernamePassword(credentialsId: 'aws-ecr-pusher', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')
        ]) {
          sh 'printenv'
          sh './build-scripts/production/deploy.sh'
        }
      }
    }
  }
  // post {
  //   cleanup {
  //     sh "docker-compose -f local.yml down --rmi 'all'"
  //     sh "docker ps -a | grep Exit | cut -d ' ' -f 1 | xargs docker rm || true"
  //     sh 'docker rmi $(docker images -f "dangling=true" -q) || true'
  //     cleanWs()
  //   }
  // }
}