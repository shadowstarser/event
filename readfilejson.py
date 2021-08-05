from datetime import date , datetime
import json

def list_event(filename):
    #dic_list = {'id': 1, 'name': "мой русский текст",'createdate': '2021-08-05'}
    # json.dump(dic_list,open("dist_event.txt","w",encoding="utf-8"))
    #js = open("dist_event.txt", 'r', encoding='utf-8')
    #event_dic_lists = json.load(js)
    with open(filename, 'r', encoding='utf-8') as js: #открываем файл на запись
        data = json.load(js)
        event = data
        #js.write(json.load(event))
        return event

def max_id_into_list(dates):
    data = dates


def add_list_event(id, name):
    idn =id
    name_event = name
    event_date = date.isoformat(datetime.today())
    data = list_event('dist_event2.txt')
    data['event'].append({
    #data.append({
        'id': idn,
        'name': name_event,
        'createdate': event_date
    })
    with open('dist_event2.txt', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile)

add_list_event(8,'testov test 222')
