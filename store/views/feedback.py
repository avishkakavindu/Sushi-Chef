from django.shortcuts import render, redirect
from django.contrib import messages
from store.forms import FeedbackForm


def feedback(request):
    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect(request.path)
        else:
            messages.error(request, "Something went wrong!")

    context = {
        'feedback_form': form,
    }
    return render(request, 'store/feedback.html', context)