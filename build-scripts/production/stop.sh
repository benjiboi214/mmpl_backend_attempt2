## Run Production Docker Compose File ##
# Requires:
# - DOCKER_REGISTRY       ## eg: benjiboi214
# - BUILD_VERSION         ## eg: 0.0.1
export DOCKER_REGISTRY="${DOCKER_REGISTRY:-"413514076128.dkr.ecr.ap-southeast-2.amazonaws.com"}"
export BUILD_VERSION="${BUILD_VERSION:-"0.0.1"}"
export DJANGO_SECRETS_PATH="${DJANGO_SECRETS_PATH:-"./.envs/.production/.django"}"
export POSTGRES_SECRETS_PATH="${POSTGRES_SECRETS_PATH:-"./.envs/.production/.postgres"}"

docker-compose -f production.yml down