# FastAPI playlist spotify to youtube music

# Installation

## Requirements in your local machine

- Python 3.6+
- Pip(3)

## Virtual environment

Install virtual environment (Linux):
```sh
python3 -m pip install --user virtualenv
```

Install virtual environment (Windows):
```sh
py -m pip install --user virtualenv
```

Create (Linux):
```sh
python3 -m venv venv
```

Create (Windows):
```sh
py -m venv env
```

Activate (Linux):
```sh
source venv/bin/activate
```

Activate (Windows):
```sh
.\env\Scripts\activate
```

Deactivate (Linux):
```sh
deactivate
```

## Clone repository

```sh
git@github.com:jerusprojects/spotify_to_yotube.git
```

Change directory:

```sh
cd spotify_to_youtube
```

## Install requirements (Virtual environmnet activated)

```sh
pip install -r requirements.txt
```

# FastAPI utilities

## run server

```sh
uvicorn main:app —reload
```