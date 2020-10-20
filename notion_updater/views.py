from django.shortcuts import render
from .models import NotionPage
from django.conf import settings


# Create your views here.
def test(request):
    html = ''

    page = NotionPage.objects.get(url=settings.NOTION_URL).page

    meeting_block = None
    for block in page.children:
        if block.id == '383b2866-a0ae-4f4e-b246-4131117721c0':
            meeting_block = block.collection
            break

    for meeting in meeting_block.get_rows():
        html += f'<h4><a href="/notes/meeting/{meeting.id}">{meeting.title}</a></h4>'

    html += '<hr>'
    return render(request, 'test.html', {'html': html})


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

    page = NotionPage.objects.get(url=settings.NOTION_URL).page

    meeting = None
    for block in page.children:
        if block.id == '383b2866-a0ae-4f4e-b246-4131117721c0':
            for row in block.collection.get_rows():
                if row.id == meeting_id:
                    meeting = row
                    break

    meeting_dict = dict()
    html_dict = {meeting: '<h2>' + meeting.title.strip() + '</h2><ul>{}</ul>'}

    q = [meeting]

    while q and has_children(temp := q.pop(0)):
        for children in temp.children:

            if children.parent in meeting_dict.keys():
                meeting_dict[children.parent].append(children)
            else:
                meeting_dict[children.parent] = [children]

            q.append(children)

            block_type = str(type(children)).replace('<class', '').replace('>', '').replace('notion.block.', '').replace("'", "").strip()
            html_dict[children] = "<li class='" + block_type + "'>" + children.title.strip() + "<ul>{}</ul></li>"

    html = getHtml(html_dict, meeting_dict, meeting)
    print(html)

    return render(request, "meeting.html", {'html': html})
