## Get rid of local build images ##
docker-compose -f local.yml down --rmi 'all'

## Get rid of dead containers ##
docker ps -a | grep Exit | cut -d ' ' -f 1 | xargs docker rm || true

## Clean up dangling images ##
docker rmi -f $(docker images -f "dangling=true" -q) || true