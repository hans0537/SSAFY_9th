from django import template

register = template.Library()

# 필터로 하고 싶은 일을 함수로 작성

# article 안의 content를 검사해서 '#'으로 시작하는 글자(해시태크)를 링크로 만들어 주기
@register.filter
def hashtag_link(article):
    content = article.content
    hashtags = article.hashtags.all()

    # 해시태그들 링크로 만들어 주기
    for hashtag in hashtags:
        content = content.replace(hashtag.content, f"<a href='/articles/{hashtag.pk}/hashtag/'>{hashtag.content}</a> ")
        # content = content.replace(hashtag.content, f"<a href='{% url 'articles:hashtag' hashtag.pk %}'>{hashtag.content}</a> ")

    return content