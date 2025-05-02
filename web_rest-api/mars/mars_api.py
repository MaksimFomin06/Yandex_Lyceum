from flask import make_response, jsonify, Blueprint, request, abort

from data import db_session
from data.jobs import Jobs


blueprint = Blueprint(
    "jobs_api", 
    __name__,
    template_folder='templates'
)


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

@blueprint.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)