from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
from training_log.models import Entry
from users.forms import EntryForm
from users.models import User


@login_required
def user_dashboard(request):
    user = request.user
    entries = Entry.objects.filter(student=user)
    total_hours = entries.aggregate(total_hours=Sum('hours'))

    return render(
        request,
        'dashboard.html',
        {
            'user': user,
            'entries': entries,
            'total_hours': total_hours['total_hours'],
        })


def edit_entry(request, entry_id=None):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.student = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Entry has been saved')
            return redirect('/accounts/profile/')

    else:
        if entry_id:
            entry = get_object_or_404(Entry, id=entry_id)
            if entry.student != request.user:
                messages.add_message(request, messages.ERROR, 'You do not have permissions to see this entry')
                return redirect('/accounts/profile/')
            form = EntryForm(instance=entry)
        else:
            form = EntryForm()

    return render(
        request,
        "entry_edit.html",
        {
            'form': form,
        }
    )