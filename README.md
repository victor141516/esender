# Esender

Send emails using HTTP GETs


## How to use

Make a request to `/` with some of the

## parameters

All of the parameters are optional:
 - `to`: Receiver of the email (default to `GATEWAY_EMAIL` environment variable)
 - `title`: Subject of the email (default to _esender_)
 - `body`: Body of the email (default to _\__)
 - `html`: Whether or not the `body` is HTML code (default to false)


## Environment variables

 - `GATEWAY_EMAIL`: Default email if not set in the request
 - `FROM_EMAIL`: Email that will figure in the from field
 - `API_KEY`: Sendgrid API key


## How to deploy

```
$ git clone https://github.com/victor141516/esender
$ docker build -t esender esender
$ docker run --rm -d \
    --name esender \
    --p 80:8000
    -e GATEWAY_EMAIL=youremail@example.com \
    -e FROM_EMAIL=fromemail@gmail.com \
    -e API_KEY=A_SENDGRID_API_TOKEN \
    esender
```
