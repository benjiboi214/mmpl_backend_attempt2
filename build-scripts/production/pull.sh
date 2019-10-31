## Build Production Docker Image ##
# Requires:
# - DOCKER_REGISTRY       ## eg: benjiboi214
# - BUILD_VERSION         ## eg: 0.0.1
export DOCKER_REGISTRY="${DOCKER_REGISTRY:-"413514076128.dkr.ecr.ap-southeast-2.amazonaws.com"}"
export BUILD_VERSION="${BUILD_VERSION:-"0.0.1"}"
export AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID:-"NONE"}"
export AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY:-"NONE"}"
export DJANGO_SECRETS_PATH="${DJANGO_SECRETS_PATH:-"./.envs/.production/.django"}"
export POSTGRES_SECRETS_PATH="${POSTGRES_SECRETS_PATH:-"./.envs/.production/.postgres"}"

echo $AWS_ACCESS_KEY_ID
echo $AWS_SECRET_ACCESS_KEY

eval $(AWS_ACCESS_KEY_ID="$AWS_ACCESS_KEY_ID" AWS_SECRET_ACCESS_KEY="$AWS_SECRET_ACCESS_KEY" aws ecr get-login --no-include-email)

docker-compose -f production.yml pull