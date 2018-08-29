#! /usr/bin/env bash

set -e

function runserver(){
    exec python app.py
}

function runtests(){
    exec python -m unittest discover
}

if [[ $1 = "runserver" ]]; then
    runserver
elif [[ $1 = "runtests" ]]; then
    runtests
else
    echo "This is not a valid option. "
fi
