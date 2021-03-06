from flask import Blueprint,jsonify
from flask_restful import Api
from resources.Hello import Hello
from resources.requests import RequestResource, Request
from resources.user import UserResource, User

from resources.auth.user_auth import (UserSignup, UserLogin, UserLogoutAccess, UserLogoutRefresh, 
                                    UserSignup, TokenRefresh, AllUsers)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#Route
api.add_resource(Hello, '/','/Hello')
api.add_resource(RequestResource, '/user/request','/user/request/', endpoint ="requests")
api.add_resource(Request, '/user/request/<int:req_id>','/user/request/<int:req_id>/', endpoint ="request" )
api.add_resource(UserResource, '/user','/user/')
api.add_resource(User, '/user/<int:uid>','/user/<int:uid>/')

#authentication endpoints
api.add_resource(UserSignup, '/auth/signup', '/auth/signup/')
api.add_resource(UserLogin, '/auth/login')
api.add_resource(UserLogoutAccess, '/auth/logout/access')
api.add_resource(UserLogoutRefresh, '/auth/logout/refresh')
api.add_resource(TokenRefresh, '/auth/token/refresh')
api.add_resource(AllUsers, '/users')
