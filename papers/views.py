from django.shortcuts import render
import datetime


def paper(request):
    today = datetime.date.today()
    paper_title = 'Sample Paper Title'
    paper_content = 'This is a sample paper content for demonstration purposes'

    context = {
        'paper_title': paper_title,
        'paper_content': paper_content,
        'date': today,
    }

    return render(request, 'papers/paper.html', context)


def paper_archive(request):
    papers = [
        {'title': 'Paper 1', 'date': '2023-01-01'},
        {'title': 'Paper 2', 'date': '2023-01-02'},
    ]

    context = {
        'papers': papers,
    }

    return render(request, 'papers/paper_archive.html', context)
