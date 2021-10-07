from flask import Flask, render_template, request, redirect, session
from private_wall_app import app
from private_wall_app.controllers import users_controller

if __name__ == "__main__":
    app.run( debug = True )