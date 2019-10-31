
## Build Production Docker Image ##
# Requires:
# - DOCKER_REGISTRY       ## eg: benjiboi214
# - BUILD_VERSION         ## eg: 0.0.1
export DOCKER_REGISTRY="${DOCKER_REGISTRY:-"413514076128.dkr.ecr.ap-southeast-2.amazonaws.com"}"
export BUILD_VERSION="${BUILD_VERSION:-"0.0.1"}"
export AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID:-"DEFAULT_USER_DEFINED_SECRET"}"
export AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY:-"DEFAULT_USER_DEFINED_SECRET"}"
export AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION:-"ap-southeast-2"}"
export DJANGO_SECRETS_PATH="${DJANGO_SECRETS_PATH:-"./.envs/.production/.django"}"
export POSTGRES_SECRETS_PATH="${POSTGRES_SECRETS_PATH:-"./.envs/.production/.postgres"}"

eval $(aws ecr get-login)

docker-compose -f production.yml push