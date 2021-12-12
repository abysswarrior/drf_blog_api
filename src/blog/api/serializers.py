from rest_framework import serializers

from blog.models import Blog, Category

# create serializers 


class BlogListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(method_name='get_author')
    category = serializers.SerializerMethodField(method_name='get_category')

    def get_author(self,obj):
        return {
            "username":obj.author.username,
            "first_name":obj.author.first_name,
            "last_name":obj.author.last_name,
        }

    def get_category(self,obj):
        category = [cat.title for cat in obj.category.get_queryset()]
        return category

    class Meta:
        model = Blog
        exclude = [
            'id', 'likes',
            'dislikes', 'create',
            'body', 'status',
            'updated', 'publish',
            'visits', 'special',
        ]


class BlogCreateSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(
        many=True, 
        queryset=Category.objects.all(),
        slug_field='id'
    )

    class Meta:
        model = Blog
        fields = [
            'title', 'body',
            'image', 'summary',
            'category', 'publish',
            'special', 'status',
        ]


class BlogDetailUpdateDeleteSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(method_name='get_author')
    slug = serializers.ReadOnlyField()

    def get_author(self,obj):
        return {
            "username":obj.author.username,
            "first_name":obj.author.first_name,
            "last_name":obj.author.last_name,
        }

    likes = serializers.SerializerMethodField(method_name='get_likes')

    def get_likes(self, obj):
        return obj.likes.count()

    dislikes = serializers.SerializerMethodField(method_name='get_dislikes')

    def get_dislikes(self, obj):
        return obj.dislikes.count()


    class Meta:
        model = Blog
        exclude =[
            "summary", "create", 
            "updated",
        ]
        read_only_fields = [
            "likes", "dislikes",
        ]


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "parent", "title" 
        ]
