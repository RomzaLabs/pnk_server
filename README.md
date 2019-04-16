# pnk_server

[![Build Status](https://travis-ci.org/RomzaLabs/pnk_server.svg?branch=master)](https://travis-ci.org/RomzaLabs/pnk_server)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Backend for purnkleen.com. Check out the project's [documentation](http://RomzaLabs.github.io/pnk_server/).

## Architecture

Documentation on the project architecture can be found [here](.github/ARCHITECTURE.md).

## Contributing

Instructions on how to contribute to this project can be found [here](.github/CONTRIBUTING.md). 

## Deployment

Instructions on how to deploy this application into production can be found [here](.github/DEPLOYMENT.md).

## Installation

Instructions on how to install this project for local development can be found [here](.github/INSTALLATION.md).

## Support

I'm not really going to do support for this project. If you find something you feel needs to be
addressed, please file an issue, but the extent of what I will do for you is covered in
the [support document](.github/SUPPORT.md).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  
- [Travis CLI](http://blog.travis-ci.com/2013-01-14-new-client/)
- [Heroku Toolbelt](https://toolbelt.heroku.com/)

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

# Continuous Deployment

Deployment is automated via Travis. When builds pass on the master or qa branch, Travis will deploy that branch to Heroku. Follow these steps to enable this feature.

Initialize the production server:

```
heroku create pnk_server-prod --remote prod && \
    heroku addons:create newrelic:wayne --app pnk_server-prod && \
    heroku addons:create heroku-postgresql:hobby-dev --app pnk_server-prod && \
    heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="pnk_server-prod" \
        DJANGO_CONFIGURATION="Production" \
        DJANGO_SETTINGS_MODULE="pnk_server.config" \
        --app pnk_server-prod
```

Initialize the qa server:

```
heroku create pnk_server-qa --remote qa && \
    heroku addons:create newrelic:wayne --app pnk_server-qa && \
    heroku addons:create heroku-postgresql:hobby-dev --app pnk_server-qa && \
    heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="pnk_server-qa" \
        DJANGO_CONFIGURATION="Production" \
        DJANGO_SETTINGS_MODULE="pnk_server.config" \
        --app pnk_server-qa
```

Securely add your Heroku credentials to Travis so that it can automatically deploy your changes:

```bash
travis encrypt HEROKU_AUTH_TOKEN="$(heroku auth:token)" --add
```

Commit your changes and push to master and qa to trigger your first deploys:

```bash
git commit -a -m "ci(travis): add Heroku credentials" && \
git push origin master:qa && \
git push origin master
```

You're now ready to continuously ship! ✨ 💅 🛳
