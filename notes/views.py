from django.shortcuts import render
from .models import NotionPage
from django.conf import settings
from notion.client import NotionClient

import time


# Create your views here.
def meeting_overview(request):
    html = ''

    client = NotionClient(token_v2=settings.NOTION_COOKIE)
    page = client.get_block(settings.NOTION_URL)

    meeting_block = None
    for block in page.children:
        if block.id == '383b2866-a0ae-4f4e-b246-4131117721c0':
            meeting_block = block.collection
            break
    sort_dict = {}
    for meeting in meeting_block.get_rows():
        month = meeting.title.split(' ')[0].lower()
        if month in sort_dict:
            sort_dict[month].append(meeting)
        else:
            sort_dict[month] = [meeting]
        # html = f'<h4 class="meeting"><a href="/notes/meeting/{meeting.id}">{meeting.title}</a></h4>' + html

    for month in sort_dict.keys():
        string = '<div class="wrapper">{}{}</div>'
        button = f'<div class="button" id="button_{month}" onclick="dropdown(this, \'{month}\');"><p>{month}</p></div>'
        tmp = '</ul></div>'
        for meeting in sort_dict[month]:
            tmp = f'<li class="meeting_{month}"><a href="/notes/meeting/{meeting.id}">{meeting.title}</a></li>' + tmp

        tmp = f'<div class="dropdown1" id="dropdown_{month}"><ul class="content" id="content_{month}">' + tmp + '<br><br>'
        html = string.format(button, tmp) + html

    return render(request, 'notes/notes.html', {'html': html})


def has_children(block):
    try:
        block.children
        return True
    except AttributeError:
        return False


def pprint(dicti):
    print('{')
    for k in dicti.keys():
        print(f'\t{k.title} : {dicti[k]}')
    print('}')


def getHtml(html_dict, meeting_dict, node):
    string = html_dict[node]
    temp = ''
    for child in meeting_dict.get(node, {}):
        temp += getHtml(html_dict, meeting_dict, child)
    return string.format(temp)


def show_meeting(request, meeting_id):

    now = time.time()

    client = NotionClient(token_v2=settings.NOTION_COOKIE)
    page = client.get_block(settings.NOTION_URL)

    meeting = None
    for block in page.children:
        if block.id == '383b2866-a0ae-4f4e-b246-4131117721c0':
            for row in block.collection.get_rows():
                if row.id == meeting_id:
                    meeting = row
                    break

    meeting_dict = dict()
    title = meeting.title.strip()
    html_dict = {meeting: '<ul>{}</ul>'}

    q = [meeting]

    index = 0

    while q and index < len(q) and has_children(temp := q[index]):
        index += 1
        for children in temp.children:

            if children.parent in meeting_dict.keys():
                meeting_dict[children.parent].append(children)
            else:
                meeting_dict[children.parent] = [children]

            q.append(children)

            block_type = str(type(children)).replace('<class', '').replace('>', '').replace('notion.block.', '').replace("'", "").strip()
            html_dict[children] = "<li class='" + block_type + "'>" + children.title.strip() + "<ul>{}</ul></li>"

    html = getHtml(html_dict, meeting_dict, meeting)
    return render(request, "notes/meeting.html", {'html': html, 'title': title})
