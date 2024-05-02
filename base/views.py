from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import models, forms
import datetime


# Create your views here.
def two_weeks(created: datetime):
    projected_two_weeks = created + datetime.timedelta(weeks=2)
    return projected_two_weeks


def home_page(request):
    param: str = request.GET.get('q') if request.GET.get('q') else ''
    if param.__contains__('by'):
        param = param.split('by')[0].strip()

    all_books = models.Book.objects.filter(title__icontains=param).order_by('title').distinct()
    books_with_available_copies = [(book, book.copies.filter(status='A').count()) for book in all_books if
                                   book.copies.filter(status='A').count() > 0]
    number_of_books = len(books_with_available_copies)
    context = {'available_copies': books_with_available_copies, 'number_of_books': number_of_books}
    return render(request, 'base/index.html', context)


def about_book_page(request, pk: int):
    book = models.Book.objects.get(id=pk)
    if book.reviews.all():
        reviews = book.reviews.all()  # list of book review with each review having a rating
        book_ratings = [review.rating for review in reviews]
        book_rating = sum(book_ratings) / len(book_ratings)
    else:
        reviews = ''
        book_rating = 0
    context = {'book': book, 'reviews': reviews, 'book_rating': book_rating}
    return render(request, 'base/book_details.html', context)


@login_required(login_url='/users/login/')
def add_book_review(request, pk: int):
    reviewBook = models.Book.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.BookReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.owner = request.user
            review.book = reviewBook
            review.save()
            return redirect('base:about_book', reviewBook.id)
        else:
            messages.error(request, 'Invalid Data Sent')

    else:
        form = forms.BookReviewForm()

    context = {'form': form, 'reviewBook': reviewBook}
    return render(request, 'base/book_review.html', context)


@login_required(login_url='/users/login/')
def borrow_book(request, pk: int):
    # we borrow copies of a book
    book = models.Book.objects.get(id=pk)
    copy = book.copies.filter(status='A').first()
    if copy:
        copy.status = 'B'
        newLibraryRecord = models.LibrayRecords()
        newLibraryRecord.borrowed_Copy = copy
        newLibraryRecord.borrower = request.user
        newLibraryRecord.save()
        newLibraryRecord.projected_date = two_weeks(newLibraryRecord.date)
        newLibraryRecord.save()
        copy.save()

        return redirect('base:index')
    else:
        messages.error(request, 'No Available Copies')
        return redirect('base:about_book', pk)


@login_required(login_url='/users/login/')
def collect_status(request, pk: int):
    form = forms.StatusForm()
    context = {'form': form, 'record_id': pk}
    return render(request, 'base/status.html', context)


@login_required(login_url='/users/login/')
def return_book(request, pk: int):
    if request.user.is_staff:
        import datetime
        record: models.LibrayRecords = models.LibrayRecords.objects.filter(id=pk, status=False).first()
        copy = record.borrowed_Copy
        condition = request.POST.get('return_status')
        return_status = 'A' if condition == 'G' else 'M'
        copy.status = return_status
        record.status = True
        record.return_date = datetime.datetime.now()
        record.return_status = condition
        record.save()
        copy.save()
        messages.success(request, 'The book has been returned')
        return redirect('users:borrowed')
    else:
        messages.error(request, 'Osiriwala !')
        return redirect('base:index')


def author(request):
    authors = models.Author.objects.all()
    context = {'authors': authors}
    return render(request, 'base/authors.html', context)


def authorDetails(request, pk: int):
    myAuthor = models.Author.objects.get(id=pk)
    context = {'author': myAuthor}
    return render(request, 'base/author_detail.html', context)
