from django.shortcuts import render, get_object_or_404
from .models import Story

def home(request):
    stories = Story.objects.all()
    return render(request, 'stories/home.html', {'stories': stories})

def story_form(request, story_id):
    story = get_object_or_404(Story, id=story_id)

    if request.method == "POST":
        user_words = {}
        for label in story.field_labels:
            user_words[label] = request.POST.get(label, '')

        completed_story = story.template.format(**user_words)

        return render(request, 'stories/story_form.html', {
            'story': story,
            'completed_story': completed_story,
            'user_words': user_words
        })

    return render(request, 'stories/story_form.html', {
        'story': story
    })

