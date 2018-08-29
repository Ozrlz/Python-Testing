# Repo to save the progress of the udemy course

https://www.udemy.com/automated-software-testing-with-python



# How to use it
The Dockerfile has an entrypoint and a CMD that passes a default argument (runserver).

The valid arguments are,
    * runserver (runs the flask app)
    * runtests (run the tests in the flask app)

So, a valid command to run it would be

> docker-compose run --rm --service-ports web runtests

In case that you wan to run a bash session inside, do the following

> docker-compose run --rm --service-ports --entrypoint=bash web