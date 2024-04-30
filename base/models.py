from django.contrib.auth.models import AbstractUser
from django.db import models

gender_choices = [('M', 'Male'), ('F', 'Female'), ('O', "Others")]


# Create your models here.
class Reader(AbstractUser):
    gender = models.CharField(max_length=10, choices=gender_choices)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField()
    reader_image = models.ImageField(upload_to='images/', blank=True, null=True, default='user.png')
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'gender', 'date_of_birth', 'bio', ]

    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.first_name + ' ' + self.last_name

    def get_email(self):
        return self.email


class ReaderProfile(models.Model):
    user = models.OneToOneField(to=Reader, on_delete=models.CASCADE)


class AuthorAward(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=10, choices=gender_choices)
    bio = models.TextField()
    date_of_birth = models.DateField()
    date_of_death = models.DateField(blank=True, null=True)
    awards = models.ManyToManyField(to=AuthorAward, blank=True)
    author_image = models.ImageField(upload_to='images/', blank=True, null=True, default='user.png')

    class Meta:
        ordering = ['first_name', 'middle_name', 'last_name', 'gender']

    def author_age(self):
        if self.date_of_death:
            age = self.date_of_death - self.date_of_birth
            return age.days // 365
        else:
            from django.utils import timezone

            today = timezone.now().today().date()
            age = today - self.date_of_birth
            return age.days // 365

    def __str__(self):
        return f"{self.first_name} {self.middle_name if self.middle_name else ''} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ManyToManyField(Author)
    date = models.DateTimeField(auto_now_add=True)
    awards = models.ManyToManyField(to=AuthorAward, blank=True)
    summary = models.TextField(null=True, blank=True)
    ISBN = models.IntegerField()
    category = models.CharField(max_length=250, help_text="Enter the book genre")
    publisher = models.CharField(max_length=250, help_text="Enter the publication company")
    published = models.DateTimeField(help_text="Enter the published date")
    book_image = models.ImageField(upload_to='images/', blank=True, null=True, default='book.jpeg')

    def __str__(self):
        authors = ", ".join(
            [f"{author.first_name} {author.middle_name if author.middle_name else ''}  {author.last_name}" for author in
             self.author.all()])
        return f"{self.title} By {authors}"


class Review(models.Model):
    owner = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='my_reviews')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description[:30]}..." if len(self.description) > 30 else f"{self.description}"


status_choice = [('M', 'Maintenance'), ('B', 'Borrowed'), ('A', 'Available'), ]
return_choices = [('G', 'Good'), ('B', 'Bad')]


class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="copies")
    edition = models.CharField(max_length=200, default="First")
    status = models.CharField(max_length=250, default='M', choices=status_choice)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.status}"


class LibrayRecords(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    projected_date = models.DateTimeField(null=True)
    borrowed_Copy = models.ForeignKey(to=BookCopy, on_delete=models.CASCADE)
    borrower = models.ForeignKey(to=Reader, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)  # returned or not
    return_date = models.DateTimeField(blank=True, null=True)
    return_status = models.CharField(max_length=250, choices=return_choices, null=True)

    def time_left(self):
        from django.utils.timesince import timeuntil
        return int(timeuntil(self.projected_date)[0])

    def __str__(self):
        return f"{self.borrowed_Copy.book.title}-{self.status}"
