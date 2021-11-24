import graphene
from graphene_django import DjangoListField, DjangoObjectType

# User
from accounts.models import CustomUser
from accounts.types import CustomUserType

# Blog
from blog.models import BlogModel, LikeModel, CommentModel
from blog.types import BlogModelType, CommentModelType

# Mutation
from .mutation import Mutation


class Query(graphene.ObjectType ):
	# ================================================= Users =================================================
    '''
        - Get All Users
        - Get One User
        - Get Me
    '''
    users = DjangoListField(CustomUserType)
    user = graphene.Field(CustomUserType, slug=graphene.String())
    me = graphene.Field(CustomUserType)

    def resolve_users(self, info):
	    return CustomUser.objects.all()

    def resolve_user(self, info, slug):
	    try:
	    	return CustomUser.objects.get(slug=slug)
	    except CustomUser.DoesNotExist:
	    	return None

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user

	# ================================================= Blog =================================================
    '''
        - Get All Blog Posts
        - Get One Blog Post
    '''
    posts = DjangoListField(BlogModelType)
    post = graphene.Field(BlogModelType, slug=graphene.String())
    
    def resolve_posts(root, info):
    	return BlogModel.objects.select_related("author").all()
    
    def resolve_post(root, info, slug):
        try:
    	    return BlogModel.objects.select_related("author").get(slug=slug)
        except BlogModel.DoesNotExist:
            return None

    
    # ================================================= User's activities =================================================
    '''
        - Get All User Blog Posts
        - Get All User Comments
        - Get All Blog Posts Liked By A User
        - Get All Comments Liked By A User
        - Get All My Blog Posts
        - Get All My Comments
    '''
    user_blog_posts = DjangoListField(BlogModelType, author=graphene.Int())
    user_comments = DjangoListField(CommentModelType, author=graphene.Int())
    user_liked_blog_posts = DjangoListField(BlogModelType, author=graphene.Int())
    user_liked_comments = DjangoListField(CommentModelType, author=graphene.Int())

    my_blog_posts = DjangoListField(BlogModelType)
    my_comments = DjangoListField(CommentModelType)
    blog_posts_i_liked = DjangoListField(BlogModelType)
    comments_i_liked = DjangoListField(CommentModelType)

    def resolve_user_blog_posts(root, info, author):
        return BlogModel.objects.filter(author=author)

    def resolve_user_comments(root, info, author):
        return CommentModel.objects.filter(author=author)

    def resolve_user_liked_blog_posts(root, info, author):
        return BlogModel.objects.filter(likes__author=author)

    def resolve_user_liked_comments(root, info, author):
        return CommentModel.objects.filter(likes__author=author)

    def resolve_my_blog_posts(root, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return BlogModel.objects.filter(author=user.id)

    def resolve_my_comments(root, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return CommentModel.objects.filter(author=user.id)

    
    def resolve_blog_posts_i_liked(root, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return BlogModel.objects.filter(likes__author=user.id)

    def resolve_comments_i_liked(root, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return CommentModel.objects.filter(likes__author=user.id)


schema = graphene.Schema(query=Query, mutation=Mutation)