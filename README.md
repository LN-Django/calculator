# boilerplate
Django + REST boilerplate for future services

## Running the App Locally
To run the dev server please run the following command.
```
 python ./boilerplate/manage.py runserver
```

## Docker config
### What is Docker?
> Docker is a "container" to package applications into standardized units for development and deployment ([Source](https://www.docker.com/resources/what-container))

### Prerequisites
- Docker is installed and accessible via terminal

How to use Docker to serve the application locally

Build the docker image
```
docker build -t web:latest .
```

Run the container with the name of `boilerplate` using the image built on the last step
```
docker run -d --name boilerplate -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 web:latest
```

Check on `http://localhost:8007` to see if the app is running.

Stop the docker container
```
docker stop boilerplate
```

Remove the container
```
docker rm boilerplate
```

## Docker Config with Heroku
### What is Heroku?
Heroku is a cloud platform (PaaS) to build and deploy the application ([Heroku documentation site](https://devcenter.heroku.com/categories/reference)). 

Building the image
```
docker build -t registry.heroku.com/intense-reef-35485/web .
```

Push the Docker container
```
docker push registry.heroku.com/intense-reef-35485/web 
```

Release the image
```
heroku container:release -a intense-reef-35485 web
```

# Notes
## Staging
Heroku URLs: https://intense-reef-35485.herokuapp.com/ | https://git.heroku.com/intense-reef-35485.git.

App name: intense-reef-35485

## Production
Heroku URLs: https://enigmatic-dusk-38395.herokuapp.com/ | https://git.heroku.com/enigmatic-dusk-38395.git.

App name: enigmatic-dusk-38395