
## Deploy The Project From CI/CD ##
# Requires:
# - GITHUB_REPO
# - GITHUB_BRANCH
# - DOCKER_REGISTRY
# - BUILD_VERSION
# - AWS_ECR_KEY_ID
# - AWS_ECR_ACCESS_KEY

export GIT_URL="${GITHUB_REPO:-"https://github.com/benjiboi214/mmpl_backend_attempt2.git"}"
export GIT_BRANCH="${GITHUB_BRANCH:-"feature/implement_deploy_step"}"
export DOCKER_REGISTRY="${DOCKER_REGISTRY:-"413514076128.dkr.ecr.ap-southeast-2.amazonaws.com"}"
export BUILD_VERSION="${BUILD_VERSION:-"0.0.1"}"
export AWS_ECR_KEY_ID="${AWS_ECR_KEY_ID:-"NONE"}"
export AWS_ECR_ACCESS_KEY="${AWS_ECR_ACCESS_KEY:-"NONE"}"
export AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION:-"ap-southeast-2"}"
export DJANGO_SECRETS_PATH="${DJANGO_SECRETS_PATH:-"./.envs/.production/.django"}"
export POSTGRES_SECRETS_PATH="${POSTGRES_SECRETS_PATH:-"./.envs/.production/.postgres"}"
export ANSIBLE_HOST_KEY_CHECKING=False
export DEPLOY_USER="${DEPLOY_USER:-"ben"}"
export SSH_KEY="${SSH_KEY:-"~/.ssh/id_rsa"}"
export ANSIBLE_SCP_IF_SSH=True

ansible-playbook -v -i staging.mmpl.systemiphus.com, \
  -u $DEPLOY_USER --key-file=$SSH_KEY \
  -e "github_repo=$GITHUB_REPO github_version=$GITHUB_BRANCH \
      docker_registry=$DOCKER_REGISTRY build_version=$BUILD_VERSION \
      aws_ecr_key_id=$AWS_ECR_KEY_ID aws_ecr_access_key=$AWS_ECR_ACCESS_KEY \
      django_secrets_path=$DJANGO_SECRETS_PATH postgres_secrets_path=$POSTGRES_SECRETS_PATH \
      aws_default_region=$AWS_DEFAULT_REGION" \
  deploy.yml