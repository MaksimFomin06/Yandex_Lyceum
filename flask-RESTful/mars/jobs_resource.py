from flask_restful import Resource, reqparse
from data import db_session
from data.jobs import Jobs

job_parser = reqparse.RequestParser()
job_parser.add_argument('team_leader', type=int, required=True)
job_parser.add_argument('job', required=True)
job_parser.add_argument('work_size', type=int, required=True)
job_parser.add_argument('collaborators', required=True)
job_parser.add_argument('start_date')
job_parser.add_argument('end_date')
job_parser.add_argument('is_finished', type=bool)


class JobsResource(Resource):
    def get(self, job_id):
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        
        if not job:
            return {'error': 'Job not found'}, 404
        
        return {'job': job.to_dict()}
    
    def delete(self, job_id):
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        
        if not job:
            return {'error': 'Job not found'}, 404
        
        db_sess.delete(job)
        db_sess.commit()
        return {'success': 'Job deleted'}, 200
    
    def put(self, job_id):
        args = job_parser.parse_args()
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        
        if not job:
            return {'error': 'Job not found'}, 404
        
        job.team_leader = args['team_leader']
        job.job = args['job']
        job.work_size = args['work_size']
        job.collaborators = args['collaborators']
        
        if args['start_date']:
            job.start_date = args['start_date']
        if args['end_date']:
            job.end_date = args['end_date']
        if args['is_finished'] is not None:
            job.is_finished = args['is_finished']
        
        db_sess.commit()
        return {'success': 'Job updated', 'job': job.to_dict()}, 200


class JobsListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()
        return {'jobs': [job.to_dict() for job in jobs]}
    
    def post(self):
        args = job_parser.parse_args()
        db_sess = db_session.create_session()
        
        job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args.get('is_finished', False)
        )
        
        if args['start_date']:
            job.start_date = args['start_date']
        if args['end_date']:
            job.end_date = args['end_date']
        
        db_sess.add(job)
        db_sess.commit()
        return {'success': 'Job created', 'id': job.id}, 201