# Interact with Django CLI using console
# Exmaple: >> bash backend_cli.sh "ls -lart" 
command=$1
echo "docker exec -it backend $command"
docker exec -it backend $command
# python manage.py startapp first_app