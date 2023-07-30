from django.shortcuts import render, redirect, get_object_or_404
from .models import Member, Theme, History

def index(request):
    member_list = Member.objects.all()
    theme_list = Theme.objects.all()

    history_five_list = History.objects.all().order_by('date').reverse()[:5]

    for history in history_five_list:
        member_list = member_list.exclude(name=history.member)
        theme_list = theme_list.exclude(theme=history.theme)

    if request.method == 'POST':
        member = get_object_or_404(Member, name=request.POST["member_post"])
        theme = get_object_or_404(Theme, theme=request.POST["theme_post"])
        history = History(member=member, theme=theme)
        history.save()
        return redirect('index')

    context = {"member_list" : member_list, "theme_list" : theme_list}
    return render(request, "index.html", context)