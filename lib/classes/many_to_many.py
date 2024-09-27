class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            raise AttributeError("Cannot change the title once set")

        if isinstance(title, str) and 6<= len(title) <= 50:
            self._title = title
        else: 
            raise ValueError("Must be a str and between 5-50 characters")
        
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else: 
            raise ValueError("must be of the type author")
        
    @property 
    def magazine(self): 
        return self._magazine
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else: 
            raise ValueError("must be of type Magazine")
        
class Author:
    all_authors = []
    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    @property
    def name(self):
       return self._name
     
    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the name once set")
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else: 
            raise ValueError("expected a str and more than 0 characters")

    def articles(self):
        all_articles = []
        for article in Article.all:
            if article.author == self: 
                all_articles.append(article)
        return all_articles

    def magazines(self):
        all_magazines = []
        for article in Article.all:
            if article.author == self:
                all_magazines.append(article.magazine)
        return list(set(all_magazines))
    
    def add_article(self, magazine, title):
        new_article = Article(self,magazine,title)
        return new_article

    def topic_areas(self):
        all_topics = []
        
        if not self.articles():
            return None
        
        for article in self.articles():
            all_topics.append(article.magazine.category)
        return list(set(all_topics))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self): 
        return self._name 
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else: 
            raise ValueError("must be a str and between 2-16 characters")
    @property
    def category(self): 
        return self._category 
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else: 
            raise ValueError("must be a str and greater than zero")
       
        

    def articles(self):
        list_of_articles = []
        for article in Article.all:
            if article.magazine == self:
                list_of_articles.append(article)
        return list_of_articles

    def contributors(self):
        list_of_contributors = []
        for article in self.articles():
            list_of_contributors.append(article.author)
        return list(set(list_of_contributors))

    def article_titles(self):
        list_of_article_titles = []
        for article in self.articles():
            list_of_article_titles.append(article.title)
        if not list_of_article_titles:
            return None
        return list_of_article_titles
        

    def contributing_authors(self):
        author_article_count = {}

        for article in self.articles():
            author = article.author

            if author in author_article_count:
                author_article_count[author] += 1
            else: author_article_count[author] = 1

        list_of_authors = [author for author, count in author_article_count.items() if count > 2]
        if not list_of_authors:
            return None
        return list_of_authors