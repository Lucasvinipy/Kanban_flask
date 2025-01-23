from flask import Blueprint, render_template, request, redirect, url_for
from database.tarefas import TAREFAS

user_route = Blueprint('user_route', __name__)


