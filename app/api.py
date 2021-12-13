from flask import (
    Blueprint,request,jsonify,abort
)
from datetime import datetime
import json
from app.models import Movie
from flask import Flask, request, url_for, jsonify

bp = Blueprint('api', __name__, url_prefix='/')

@bp.route("/test",methods=["GET"])
def test():
    return jsonify({"status":"success"})


@bp.route('/movies')
def get_movies():
    page = int(request.args.get('page',1))
    limit = int(request.args.get('limit',10))
    movies = Movie.objects.paginate(page=page, per_page=limit)
    return jsonify([movie for movie in movies.items]), 200


@bp.route('/movies/', methods=["POST"])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    print(movie)
    return jsonify(movie), 201


@bp.route('/movies/<title>')
def get_one_movie(title: str):
    movie = Movie.objects(title=title).first()
    if not movie:
        return jsonify({'error': 'Movie not found'})
    else:
        return jsonify(movie), 200


@bp.route('/movies/<title>', methods=['PUT'])
def update_movie(title):
    body = request.get_json()
    movie = Movie.objects(title=title).first()
    if not movie:
        return jsonify({'error': 'Movie not found'})
    else:
        movie.update(**body)
        return jsonify(movie), 200

@bp.route('/movies/<title>', methods=['DELETE'])
def delete_movie(title):
    movie = Movie.objects(title=title).first()
    if not movie:
        return jsonify({'error': 'Movie not found'})
    else:
        movie.delete()
        return jsonify({'Success': f'Movie deleted {movie.title}'})


