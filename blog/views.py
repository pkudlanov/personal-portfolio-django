from django.views import generic
from .models import Post
from portfolio.models import Tag


class AllPosts(generic.ListView):
    model = Post
    ordering = ['-id']


class DetailPost(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        tags = {}
 
        # Add an html popper element for each tag to the dictionary
        for tag in Tag.objects.all():
            if tag.active_popper:
                tags[tag.name] = '<span class="text-popper color-o" tabindex="0" role="button" data-bs-toggle="popover" data-bs-trigger="focus" title="' + tag.name + '" data-bs-content="' + tag.summary + '" data-url-post="' + tag.url_post + '">' + tag.name + '</span>'

        # Working context decleration
        post_body = context['post'].body

        # Replace each instance of the tags from the dictionary in the body of the post with popper element
        for k, v in tags.items():
            post_body = post_body.replace(k, v)

        # Set context equal to new updated context (working context)
        context['post'].body = post_body

        return context
