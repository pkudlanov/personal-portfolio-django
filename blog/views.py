from django.views import generic
from .models import Post
from portfolio.models import Tag

import re


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
                tags[tag.id] = {
                    # 'length': len(tag.name.split()),
                    'length': len(re.split(' |/', tag.name)),
                    'name': tag.name, 
                    'html_element': '<span class="text-popper color-o" tabindex="0" role="button" data-bs-toggle="popover" data-bs-trigger="focus" title="' + tag.name + '" data-bs-content="' + tag.summary + '" data-url-post="' + tag.url_post + '">' + tag.name + '</span>'
                }

        # Working context decleration
        post_body = context['post'].body

        # Replace all 2 word long tags with unique id so if they include another tag thats 1 word long they wont get affected by that tag
        for k, v in tags.items():
            if v['length'] > 1:
                padded_id = str(k).zfill(4)
                dollar_k_id = '$$' + padded_id
                s = v['name']

                post_body = re.sub(r'\b%s\b' % s,  dollar_k_id, post_body, flags=re.IGNORECASE)

        for k, v in tags.items():
            if v['length'] <= 1:
                padded_id = str(k).zfill(4)
                dollar_k_id = '$$' + padded_id
                s = v['name']

                post_body = re.sub(r'\b%s\b' % s,  dollar_k_id, post_body, flags=re.IGNORECASE)

        # Replace each instance of the tags from the dictionary in the body of the post with popper element
        for k, v in tags.items():
            padded_id = str(k).zfill(4)
            dollar_k = '$$' + padded_id
            post_body = post_body.replace(dollar_k, v['html_element'])

        # Set context equal to new updated context (working context)
        context['post'].body = post_body

        return context
