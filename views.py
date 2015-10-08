# encoding: utf-8
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.forms.models import modelformset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from .models import *
#custom project settings
from cms.models import *


class PostListView(ListView):
    queryset = Post.objects.filter(activity=True)
    context_object_name = 'posts'
    paginate_by = 10

    #custom project settings
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['contacts'] = Contact.objects.get(activity=True)
        context['tels'] = context['contacts'].tel.all()
        context['bg'] = Background.objects.get(activity=True)
        context['botlinks'] = BottomNavigation.objects.all()
        context['no_contacts'] = True
        return context


class TaggedPostListView(ListView):
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(activity=True, tags__slug=self.kwargs.get('slug'))

    #custom project settings
    def get_context_data(self, **kwargs):
        context = super(TaggedPostListView, self).get_context_data(**kwargs)
        context['contacts'] = Contact.objects.get(activity=True)
        context['tels'] = context['contacts'].tel.all()
        context['bg'] = Background.objects.get(activity=True)
        context['botlinks'] = BottomNavigation.objects.all()
        context['no_contacts'] = True
        return context


class ProfilePostListView(ListView):
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ProfilePostListView, self).get_context_data(**kwargs)
        context['is_profile'] = True

        #custom project settings
        context['contacts'] = Contact.objects.get(activity=True)
        context['tels'] = context['contacts'].tel.all()
        context['bg'] = Background.objects.get(activity=True)
        context['botlinks'] = BottomNavigation.objects.all()
        context['no_contacts'] = True
        return context


class ProfileCommentListView(ListView):
    context_object_name = 'comments'
    paginate_by = 10

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    #custom project settings
    def get_context_data(self, **kwargs):
        context = super(ProfileCommentListView, self).get_context_data(**kwargs)
        context['current_user'] = self.request.user
        context['contacts'] = Contact.objects.get(activity=True)
        context['tels'] = context['contacts'].tel.all()
        context['bg'] = Background.objects.get(activity=True)
        context['botlinks'] = BottomNavigation.objects.all()
        context['no_contacts'] = True
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = Post.objects.get(slug=self.kwargs['slug'])
        context['comments'] = Comment.objects.filter(post=post).order_by('created')
        context['form'] = CommentForm
        #custom project settings
        context['contacts'] = Contact.objects.get(activity=True)
        context['tels'] = context['contacts'].tel.all()
        context['bg'] = Background.objects.get(activity=True)
        context['botlinks'] = BottomNavigation.objects.all()
        context['no_contacts'] = True
        return context


def add_comment(request, slug):
    p = request.POST
    if p.has_key("content") and p["content"]:
        author = request.user
        comment = Comment(post=Post.objects.get(slug=slug))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("post_detail", kwargs={'slug':slug}))


class PostCreateView(CreateView):
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)

    #custom project settings
    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['contacts'] = Contact.objects.get(activity=True)
        context['tels'] = context['contacts'].tel.all()
        context['bg'] = Background.objects.get(activity=True)
        context['botlinks'] = BottomNavigation.objects.all()
        context['no_contacts'] = True
        return context


class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post

    #custom project settings
    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['contacts'] = Contact.objects.get(activity=True)
        context['tels'] = context['contacts'].tel.all()
        context['bg'] = Background.objects.get(activity=True)
        context['botlinks'] = BottomNavigation.objects.all()
        context['no_contacts'] = True
        return context


class PostDeleteView(DeleteView):
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('my_posts')

    #custom project settings
    def get_context_data(self, **kwargs):
        context = super(PostDeleteView, self).get_context_data(**kwargs)
        context['contacts'] = Contact.objects.get(activity=True)
        context['tels'] = context['contacts'].tel.all()
        context['bg'] = Background.objects.get(activity=True)
        context['botlinks'] = BottomNavigation.objects.all()
        context['no_contacts'] = True
        return context


class ProfileView(DetailView):

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.request.user, activity=True)
        #custom project settings
        context['contacts'] = Contact.objects.get(activity=True)
        context['tels'] = context['contacts'].tel.all()
        context['bg'] = Background.objects.get(activity=True)
        context['botlinks'] = BottomNavigation.objects.all()
        context['no_contacts'] = True
        return context


def profile_update(request):

    # UserFormSet = modelformset_factory(User, fields=('first_name', 'last_name'))
    userforms = []
    post_formsets = []
    users = User.objects.all()
    PostFormSet = inlineformset_factory(User, Post, fields=('title', 'slug'))
    contacts = Contact.objects.get(activity=True)
    tels = contacts.tel.all()
    bg = Background.objects.get(activity=True)
    botlinks = BottomNavigation.objects.all()
    if request.method == 'POST':
        print request.POST
        for user in users:
            userform = UserForm(request.POST, request.FILES, instance=user)
            post_formset = PostFormSet(request.POST, request.FILES, instance=user)
            if userform.is_valid() and post_formset.is_valid():
                userform.save()
                post_formset.save()
                return HttpResponseRedirect('/posts/profile/update/')
    else:
        for user in users:
            userform = UserForm(instance=user)
            userforms.append(userform)
            post_formset = PostFormSet(instance=user)
            post_formsets.append(post_formset)
    # user_form = UserForm(request.POST or None, instance=request.user)
    # user_extend_form = UserExtendForm(request.POST or None, instance=request.user.userextend or None)

        # if user_form.is_valid() and user_extend_form.is_valid():
        #     user_form.save()
        #     user_extend_form.save()
        c = {'userforms': userforms, 'post_formsets': post_formsets, 'contacts': contacts, 'tels': tels, 'bg': bg,
             'botlinks': botlinks, 'no_contacts': True}
    return render(request, 'posts/user_form.html', c)


class UserDetailView(DetailView):

    #custom project settings
    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['contacts'] = Contact.objects.get(activity=True)
        context['tels'] = context['contacts'].tel.all()
        context['bg'] = Background.objects.get(activity=True)
        context['botlinks'] = BottomNavigation.objects.all()
        context['no_contacts'] = True
        #important
        context['user'] = self.request.user
        context['current_user'] = User.objects.get(pk=self.kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        self.object = User.objects.get(pk=self.kwargs['pk'])
        if self.request.user.pk == int(self.kwargs['pk']):
            return redirect('/posts/profile/')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
