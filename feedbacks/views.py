from feedbacks.models import Feedback
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import mail_admins
from django.contrib import messages


class FeedbackView(CreateView):
    model = Feedback
    template_name = "feedback.html"
    success_url = reverse_lazy('feedback')
    context_object_name = "form"
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        data = self.request.POST
        mail_admins(data['subject'], data['message'])
        messages.success(
            self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return super(FeedbackView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Feedback"
        return context
