from app import app, db
from app.models import User
from flask import render_template, request
from create_fake_users import create_fake_users


@app.route('/')
@app.route('/index')
def index():
    create_fake_users(1000)
    users = User.query.all()
    return render_template('bootstrap-table.html', users=users, title='Bootstrap Table')


@app.route('/basic-table')
def basic_table():
    create_fake_users(1000)
    users = User.query.all()
    return render_template('basic-table.html', users=users, title='Basic Table')


@app.route('/ajax-table')
def ajax_table():
    return render_template('ajax-table.html', title='Ajax Table')


@app.route('/ajax-table-data')
def ajax_table_data():
    return {'data': [user.to_dict() for user in User.query.all()]}


@app.route('/server-side-table')
def server_side_table():
    return render_template('server-side-table.html', title='Server Side Table')


@app.route('/server-side-table-data')
def server_side_table_data():
    query = User.query

    # Search filter
    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            User.username.like(f'%{search}%'),
            User.email.like(f'%{search}%')
        ))
    total_filtered = query.count()

    # Sorting
    order = []
    i = 0
    while True:
        col_index = request.args.get(f'order[{i}][column]')
        if col_index is None:
            break
        col_name = request.args.get(f'columns[{col_index}][data]')
        if col_name not in ['username', 'age', 'email']:
            col_name = 'username'
        descending = request.args.get(f'order[{i}][dir]') == 'desc'
        col = getattr(User, col_name)
        if descending:
            col = col.desc()
        order.append(col)
        i += 1
    if order:
        query = query.order_by(*order)

    # Pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    # Response
    return {
        'data': [user.to_dict() for user in query],
        'recordsFiltered': total_filtered,
        'recordsTotal': User.query.count(),
        'draw': request.args.get('draw', type=int),
    }
