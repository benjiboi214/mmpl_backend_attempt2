
## Deploy The Project From CI/CD ##
# Requires:
# - GITHUB_REPO
# - GITHUB_BRANCH
# - DOCKER_REGISTRY
# - BUILD_VERSION
# - AWS_ECR_KEY_ID
# - AWS_ECR_ACCESS_KEY

export GITHUB_REPO="${GITHUB_REPO:-"https://github.com/benjiboi214/mmpl_backend_attempt2.git"}"
export GITHUB_BRANCH="${GITHUB_BRANCH:-"feature/implement_deploy_step"}"
export DOCKER_REGISTRY="${DOCKER_REGISTRY:-"413514076128.dkr.ecr.ap-southeast-2.amazonaws.com"}"
export BUILD_VERSION="${BUILD_VERSION:-"0.0.1"}"
export AWS_ECR_KEY_ID="${AWS_ECR_KEY_ID:-"NONE"}"
export AWS_ECR_ACCESS_KEY="${AWS_ECR_ACCESS_KEY:-"NONE"}"
export DJANGO_SECRETS_PATH="${DJANGO_SECRETS_PATH:-"./.envs/.production/.django"}"
export POSTGRES_SECRETS_PATH="${POSTGRES_SECRETS_PATH:-"./.envs/.production/.postgres"}"

ansible-playbook -v -i staging.mmpl.systemiphus.com, \
  -u django --key-file=/Users/ben/.ssh/id_rsa \
  -e "github_repo=$GITHUB_REPO github_version=$GITHUB_BRANCH \
      docker_registry=$DOCKER_REGISTRY build_version=$BUILD_VERSION \
      aws_ecr_key_id=$AWS_ECR_KEY_ID aws_ecr_access_key=$AWS_ECR_ACCESS_KEY \
      django_secrets_path=$DJANGO_SECRETS_PATH postgres_secrets_path=$POSTGRES_SECRETS_PATH" \
  deploy.yml