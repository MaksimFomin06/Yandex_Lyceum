from flask_restful import Resource, reqparse
from data import db_session
from data.users import User

user_parser = reqparse.RequestParser()
user_parser.add_argument('surname', required=True)
user_parser.add_argument('name', required=True)
user_parser.add_argument('age', type=int, required=True)
user_parser.add_argument('position', required=True)
user_parser.add_argument('speciality', required=True)
user_parser.add_argument('address', required=True)
user_parser.add_argument('email', required=True)
user_parser.add_argument('city_from', required=True)
user_parser.add_argument('password', required=True)

class UsersResource(Resource):
    def get(self, user_id):
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        
        if not user:
            return {'error': 'User not found'}, 404
        
        return {'user': user.to_dict()}
    
    def delete(self, user_id):
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        
        if not user:
            return {'error': 'User not found'}, 404
        
        db_sess.delete(user)
        db_sess.commit()
        return {'success': 'User deleted'}

class UsersListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        return {'users': [user.to_dict() for user in users]}
    
    def post(self):
        args = user_parser.parse_args()
        db_sess = db_session.create_session()
        
        if db_sess.query(User).filter(User.email == args['email']).first():
            return {'error': 'Email already exists'}, 400
        
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            city_from=args['city_from']
        )
        user.set_password(args['password'])
        
        db_sess.add(user)
        db_sess.commit()
        return {'success': 'User created', 'id': user.id}, 201