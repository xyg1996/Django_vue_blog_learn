from rest_framework import serializers
from article.models import Article
from user_info.serializers import UserDescSerializer
# 父类变成了 ModelSerializer
class ArticleListSerializer(serializers.ModelSerializer):
    # read_only 参数设置为只读
    author = UserDescSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="article:detail")
    class Meta:
        model = Article
        fields = [
            # 'id',
            'url',
            'title',
            'created',
            'author',
        ]
        # read_only_fields = ['author']
class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
