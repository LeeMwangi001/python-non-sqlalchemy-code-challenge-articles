class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise ValueError("title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("title must be between 5 and 50 characters")

        self._title = title
        self._author = author
        self._magazine = magazine
        Article.all.append(self)
        author._articles.append(self) 
        magazine._articles.append(self)  

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise ValueError("title must be a string")
        if not (5 <= len(new_title) <= 50):
            raise ValueError("title must be between 5 and 50 characters")
        self._title = new_title  

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter 
    def name(self, value):
        raise AttributeError("name is immutable")

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines()))

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("name must be a non-empty string")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        return list(set(article.author for article in self._articles))

    def add_article(self, article):
        if not isinstance(article, Article):
            raise ValueError("article must be an instance of Article")
        self._articles.append(article)

    def top_publisher(cls):
        """Returns the magazine with the most articles or None if there's a tie."""
        if not Magazine.all:
            return None
        articles_per_magazine = {magazine: 0 for magazine in Magazine.all}
        for article in Article.all:
            articles_per_magazine[article.magazine] += 1
        max_articles = max(articles_per_magazine.values())
        top_publishers = [magazine for magazine, count in articles_per_magazine.items() if count == max_articles]
        return top_publishers[0] if len(top_publishers) == 1 else None
