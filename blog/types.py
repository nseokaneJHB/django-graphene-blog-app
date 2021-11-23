from graphene_django import DjangoObjectType, DjangoListField
from .models import BlogModel, LikeModel, CommentModel


class LikeModelType(DjangoObjectType):
	class Meta:
		model = LikeModel
		fields = ('id', 'author')


class CommentModelType(DjangoObjectType):
	class Meta:
		model = CommentModel
		fields = ('id', 'author', 'post', 'comment', 'likes', 'date_created', 'date_modified')


class BlogModelType(DjangoObjectType):
	comments = DjangoListField(CommentModelType)

	class Meta:
		model = BlogModel
		fields = ( 'id', 'author', 'title', 'body', 'likes', 'meta_description', 'date_created', 'date_modified', 'published', 'publish_date', 'slug', 'comments' )

	def resolve_comments(self, info):
		return CommentModel.objects.all().filter(post=self.pk)