#from django.views.generic import ListView

from django.shortcuts import render, get_object_or_404

from .models import Post


def blog_posts(request):
    """Display all blog posts"""

    posts = Post.objects.all().order_by('-created_date')

    return render(request, 'blog/blog.html', {'posts': posts})


def post(request, pk, slug):
    """Display specific blog posts"""

    post_detail = get_object_or_404(Post, pk=pk, slug=slug)

    return render(request, 'blog/post.html', {'post_detail': post_detail})


'''
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic


from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'blog/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'blog/results.html'




def retail(request, question_id, foo_id):
	overall_id = question_id * foo_id;
	return HttpResponse("You're looking at question %s, retail %s. The conjoined is %s" % (question_id, foo_id, overall_id))

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'blog/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))
		'''