from pyramid.view import view_config, forbidden_view_config
from pyramid.security import remember, forget, authenticated_userid

from pyramid.httpexceptions import (
    HTTPMovedPermanently,
    HTTPFound,
    HTTPNotFound,
    )

from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer

from models import DBSession, User
from forms import SignupSchema, SigninSchema


@view_config(route_name='signin', renderer='templates/users/signin.pt')
@forbidden_view_config(renderer='templates/users/signin.pt')
def signin(request):
    form = Form(request, schema=SigninSchema())
    if form.validate():
        query = DBSession.query(User).filter(User.email == form.data['email'])
        if query.count():
            user = query.first()
            if user.check_password(form.data['password']):
                headers = remember(request, user.email)
                return HTTPFound(location='/', headers=headers)
            else:
                request.session.flash(u'Wrong email or password', 'error')
        else:
            request.session.flash(u'Wrong email or password', 'error')
    return dict(
        renderer=FormRenderer(form),
        logged_in=authenticated_userid(request)
    )


@view_config(route_name='signup', renderer='templates/users/signup.pt')
def signup(request):
    form = Form(request, schema=SignupSchema())
    if form.validate():
        user = form.bind(User())
        DBSession.add(user)
        request.session.flash(u'Now you can sign in', 'success')
        return HTTPFound(location=request.route_url('signin'))
    return dict(renderer=FormRenderer(form))


@view_config(route_name='signout')
def signout(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('signin'), headers=headers)


def account_settings(request):
    pass


def forgot_password(request):
    pass


@view_config(route_name='notes', renderer='templates/notes/list.pt',
             permission='login_required')
def notes(request):
    return dict(
        logged_in=authenticated_userid(request)
    )


def create_note(request):
    pass


def update_note(request):
    pass


def delete_note(request):
    pass


def create_pad(request):
    pass


def update_pad(request):
    pass


def delete_pad(request):
    pass