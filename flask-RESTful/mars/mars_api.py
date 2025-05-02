import datetime
from flask import make_response, jsonify, Blueprint, request, abort

from data import db_session
from data.jobs import Jobs
from data.users import User
from data.users import User

blueprint = Blueprint(
    "jobs_api", 
    __name__,
    template_folder='templates'
)


def user_to_dict(user):
    return {
        'id': user.id,
        'surname': user.surname,
        'name': user.name,
        'age': user.age,
        'position': user.position,
        'speciality': user.speciality,
        'address': user.address,
        'email': user.email,
        'modified_date': user.modified_date.isoformat(),
        'city_from': user.city_from,
    }


@blueprint.route('/api/users', methods=['GET'])
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify({'users': [user_to_dict(user) for user in users]})


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")
    return jsonify({'user': user_to_dict(user)})


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        abort(400, message="Empty request")
    
    required_fields = ['surname', 'name', 'email', 'password']
    if not all(field in request.json for field in required_fields):
        abort(400, message=f"Missing required fields: {required_fields}")
    
    db_sess = db_session.create_session()
    
    if db_sess.query(User).filter(User.email == request.json['email']).first():
        abort(400, message="User with this email already exists")
    
    user = User(
        surname=request.json['surname'],
        name=request.json['name'],
        email=request.json['email'],
        age=request.json.get('age'),
        position=request.json.get('position'),
        speciality=request.json.get('speciality'),
        address=request.json.get('address'),
        modified_date=datetime.datetime.now(),
        city_from=request.json.get("city_form"),
    )
    user.set_password(request.json['password'])
    
    db_sess.add(user)
    db_sess.commit()
    
    return jsonify({'success': 'User created', 'id': user.id}), 201


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if not request.json:
        abort(400, message="Empty request")
    
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    
    if not user:
        abort(404, message=f"User {user_id} not found")
    
    fields = ['surname', 'name', 'age', 'position', 
              'speciality', 'address', 'email', 'password']
    
    for field in fields:
        if field in request.json:
            if field == 'email' and request.json['email'] != user.email:
                if db_sess.query(User).filter(User.email == request.json['email']).first():
                    abort(400, message="Email already in use")
                user.email = request.json['email']
            elif field == 'password':
                user.set_password(request.json['password'])
            elif field == "city_from" in request.json:
                user.city_from = request.json["city_from"]
            else:
                setattr(user, field, request.json[field])
    
    user.modified_date = datetime.datetime.now()
    db_sess.commit()
    
    return jsonify({'success': f'User {user_id} updated'})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    
    if not user:
        abort(404, message=f"User {user_id} not found")
    
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': f'User {user_id} deleted'})


@blueprint.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

@blueprint.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400


@blueprint.route("/api/jobs")
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
                 for item in jobs]
        }
    )


@blueprint.route("/api/jobs/<int:job_id>", methods=['GET'])
def get_one_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")
    return jsonify(
        {
            'job': job.to_dict(only=(
                'team_leader', 'job', 'work_size', 'collaborators', 
                'start_date', 'end_date', 'is_finished'
            ))
        }
    )


@blueprint.route("/api/jobs", methods=['POST'])
def create_job():
    if not request.json:
        return make_response(jsonify({"error": "Empty request"}), 400)
    elif not all(key in request.json for key in
                 ["team_leader", "job", "work_size", "collaborators"]):
        return make_response(jsonify({"error": "Bad request"}), 400)
    db_sess = db_session.create_session()
    jobs = Jobs(
        team_leader=request.json["team_leader"],
        job=request.json["job"],
        work_size=request.json["work_size"],
        collaborators=request.json["collaborators"]
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({"id": "jobs"})


@blueprint.route("/api/jobs/<int:job_id>", methods=['DELETE'])
def delete_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'}), 404
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': f'Job {job_id} deleted'}), 200


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET', 'PUT'])
def edit_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    
    if not job:
        return jsonify({'error': 'Not found'}), 404
    
    if request.method == 'GET':
        return jsonify({
            'job': job.to_dict(only=(
                'team_leader', 'job', 'work_size', 'collaborators',
                'start_date', 'end_date', 'is_finished'
            ))
        })
    
    if request.method == 'PUT':
        if not request.json:
            return jsonify({'error': 'Empty request'}), 400
        
        if 'team_leader' in request.json:
            job.team_leader = request.json['team_leader']
        if 'job' in request.json:
            job.job = request.json['job']
        if 'work_size' in request.json:
            job.work_size = request.json['work_size']
        if 'collaborators' in request.json:
            job.collaborators = request.json['collaborators']
        if 'is_finished' in request.json:
            job.is_finished = request.json['is_finished']
        if 'start_date' in request.json:
            job.start_date = request.json['start_date']
        if 'end_date' in request.json:
            job.end_date = request.json['end_date']
        
        db_sess.commit()
        return jsonify({'success': f'Job {job_id} updated'}), 200


@blueprint.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)