import flask
from flask import jsonify
from jobs import Jobs
from flask import make_response

from . import db_session

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(
                    only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
                    for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>')
def get_jobs(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    item = jobs[job_id]
    return jsonify(
        {
            'jobs':
                [item.to_dict(
                    only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))]
        }
    )


@blueprint.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
