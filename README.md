# TotoCare
LA Girls in Tech hackathon contribution

### Installation Instructions 

```
sudo pip install -r requirements.txt
```

Ensure MongoDb is running 

```
brew services start mongodb
```

Run the application 
```
python run_server.py 
```

### Prerequisites 

1. Heroku 

See detailed instructions for each system here https://devcenter.heroku.com/articles/heroku-cli#macos

```
brew install heroku/brew/heroku
```

2. Mongo DB 

Detailed description available here https://docs.mongodb.com/manual/administration/install-community/

```
brew update
brew install mongodb
```


### To get started

* Download code

* Create a virtual environment 

		virtualenv venv

* Install all requirements for app

		. runpip

	or 

		. venv/bin/activate
		pip install -r requirements.txt

* Create Heroku app

		heroku create

* Add MongoLab Starter Addon to your app, from your code directory in Terminal

		heroku addons:add mongolab

* Add MONGOLAB_URI from Heroku config to your .env file

		heroku config --shell | grep MONGOLAB_URI >> .env

### Create a SECRET_KEY for your .env and Heroku Config

We need a SECRET_KEY for salting the user passwords.

* Open your .env and add a new line 

		SECRET_KEY=SOMETHINGSECRETANDRANDOMHERE
		DEBUG=True

* We need to add this secret key to Heroku config vars too

		heroku config:add SECRET_KEY=SOMETHINGSECRETANDRANDOMHERE

This will add a new key and value to the App on Heroku.

## Run it

With your MONGOLAB_URI and SECRET_KEY configured in .env and on Heroku config you should be good to run the code.

Ensure that foreman is installed 

```
gem install foreman 
```

Run,

	. start

or 

	. venv/bin/activate
	foreman start