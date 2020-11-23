[![Open Issues](https://img.shields.io/github/issues/nightwarriorftw/impressive_uploader?style=for-the-badge&logo=github)](https://github.com/nightwarriorftw/impressive_uploader/issues) [![Forks](https://img.shields.io/github/forks/nightwarriorftw/impressive_uploader?style=for-the-badge&logo=github)](https://github.com/nightwarriorftw/impressive_uploader/network/members) [![Stars](https://img.shields.io/github/stars/nightwarriorftw/impressive_uploader?style=for-the-badge&logo=reverbnation)](https://github.com/nightwarriorftw/impressive_uploader/stargazers) ![Maintained](https://img.shields.io/maintenance/yes/2020?style=for-the-badge&logo=github) ![Made with Python](https://img.shields.io/badge/Made%20with-Python-blueviolet?style=for-the-badge&logo=python)![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red?style=for-the-badge&logo=open-source-initiative) ![Built with Love](https://img.shields.io/badge/Built%20With-%E2%99%A5-critical?style=for-the-badge&logo=ko-fi) [![Follow Me](https://img.shields.io/twitter/follow/nightwarriorftw?color=blue&label=Follow%20%40nightwarriorftw&logo=twitter&style=for-the-badge)](https://twitter.com/intent/follow?screen_name=nightwarriorftw) [![Telegram](https://img.shields.io/badge/Telegram-Chat-informational?style=for-the-badge&logo=telegram)](https://telegram.me/nightwarriorftw)

# Impressive Uploader

## About

In this project we will be doing heavy async tasks in the background (like generating thumbnail images) using **Celery**, **Redis** and **Django**. This is just a demo how we can handle heavy intensive task at Backend.

## :wrench: Development

#### Create virtual environment and activate

```
python3 -m venv virtual
source ./virtual/bin/activate
```

#### Clone the repo and install requirements.txt

```
git clone https://github.com/nightwarriorftw/impressive_uploader.git
cd impressive_uploader
pip install -r requirements.txt
```

#### Setup Celery and Redis

- Open 2 terminals and run the following commands respectively in them

```
celery -A creator worker -l info
```

```
redis-server
```

#### Makemgirations and run the server

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## :camera: Gallery

- front page

![front_page](./public/front_page.png)

- upload image

![upload_image](./public/upload_image.png)

- Wait till the image is processing

![processing](./public/processing.png)

- Download the result

![Download](./public/zip.png)

_Spoiler Alert_ - Something cool is coming
