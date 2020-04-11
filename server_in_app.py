import json
import time
from core_logic import Board, Card, Estimation, ErrorApi
from app_in_bd import get_users, get_card, delete, report


def client_wrapper(user_name, user_secret, commands, data=None):
    clss, command = commands.split('_')
    print(command)
    try:
        if command == 'report':
            lst_report = report(data)
            return pars_for_rep(lst_report)

        if commands == 'user_list':
            return {"count" :len(get_users()['users']), 
                        "users": [{'username':i['user_name']} for i in get_users()['users']] }
        
        if command == 'create':
            obj = crete_class(data, clss, user_name)
            status = f'{obj.save_in_bd()}'
            return status

        if command == 'delete':
            status = str(delete(data, clss))
            return status
        
        if command == 'update':
            status = update_card(data, user_name)
            return status
    except ErrorApi:
        return ''


def pars_for_rep(lst_card):
    try:
        json_card = dict()
        sum_estimation = list()
        lst = list()
        for card in lst_card:
            (user_name, times, title, board,
            status, description, assignee, estimation,
            board_id, last_update_at, last_update_by) = card

            sum_estimation.append(estimation)
            estimation = (estimation[:-1], estimation[-1:])
            lst.append({
                        "title": title,
                        "board": board,
                        "status": status,
                        "description": description, 
                        "assignee": assignee,
                        "estimation": str(Estimation(*estimation).pars()),
                        "created_at": time.ctime(float(times)),#### Сделать перевод
                        "created_by": user_name,
                        "last_updated_at": time.ctime(float(last_update_at)),#### Сделать перевод
                        "last_updated_by": last_update_by
                        })

        sum_e = Estimation(0, 'h')
        for estam in sum_estimation:
            sum_e += Estimation(*(estam[:-1], estam[-1:]))
        json_card['board'] = board
        json_card['column'] = status
        json_card['assignee'] = assignee
        json_card['count'] = len(lst_card)
        json_card['estimation'] = str(sum_e.pars())
        json_card['cards'] = lst
        print(json_card)
        json_card = json.dumps(json_card)
        return json_card
    except UnboundLocalError:
        raise ErrorApi


def crete_class(data, clss, user_name):
    data['user_name'] = user_name
    data['times'] = time.time()
    classes = {'board': Board, 'card': Card}
    new_cls = classes[clss]
    new_cls = new_cls.create_from_dict(data)
    return new_cls


def update_card(data, user_name):
    try:
        name_card = data['title']
        name_board = data['board']
        card = get_card(name_card, name_board)
        obj_card = Card.create_from_dict(card)
        print(obj_card.estimation)
        obj_card = update_obj(data, obj_card, user_name)
        status = obj_card.save_in_bd()
        return status

    except ErrorApi:
        return ''


def update_obj(data, obj, user_name):
    update_list = ['status', 'description', 'assignee', 'estimation']
    
    for key in ['title', 'board']:
        if data.get(key): data.pop(key)
    for key in data:
        if key == 'status':
            obj.status = data[key]
        if key == 'description':
            obj.description = data[key]
        if key == 'assignee':
            obj.assignee = data[key]
        if key == 'estimation':
            obj.estimation = data[key]
        if key not in update_list:
            raise ErrorApi
    obj.last_update_by = user_name
    return obj




