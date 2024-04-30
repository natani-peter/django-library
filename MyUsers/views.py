from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, EditForm
from base.models import Reader, LibrayRecords, Review, BookCopy
from base.forms import BookReviewForm


@login_required(login_url='/users/login')
def borrowed_book(request):
    if request.user.is_staff:
        books = LibrayRecords.objects.filter(status=False).order_by('-date')
        context = {'records': books}
        return render(request, 'MyUsers/borrowed_books.html', context)
    else:
        books = LibrayRecords.objects.filter(borrower=request.user, status=False).order_by('-date')
        context = {'records': books}
        return render(request, 'MyUsers/borrowed_books.html', context)


@login_required(login_url='/users/login')
def returned_book(request):
    books = LibrayRecords.objects.filter(status=True, borrower=request.user).order_by('-date')
    context = {'records': books}
    return render(request, 'MyUsers/returned_books.html', context)


@login_required(login_url='/users/login')
def userReviews(request):
    my_Reviews = Review.objects.filter(owner=request.user).order_by('-date')
    context = {'my_Reviews': my_Reviews}
    return render(request, 'MyUsers/my_reviews.html', context)


@login_required(login_url='/users/login')
def edit_review(request, pk: int):
    the_review = Review.objects.get(pk=pk)
    if request.user == the_review.owner:
        if request.method == 'POST':
            form = BookReviewForm(request.POST, instance=the_review)
            if form.is_valid():
                form.save()
                messages.success(request, 'Review Updated Successfully!')
                return redirect('users:userReviews')
        else:
            form = BookReviewForm(instance=the_review)

        context = {'form': form}
        return render(request, 'MyUsers/edit_review.html', context)


@login_required(login_url='/users/login')
def confirm_delete(request, pk: int):
    obj = Review.objects.get(pk=pk)
    context = {'obj': obj, 'pk': pk}
    return render(request, 'MyUsers/confirm-delete.html', context)


@login_required(login_url='/users/login')
def delete_review(request, pk: int):
    the_review = Review.objects.get(pk=pk)
    if request.user == the_review.owner:
        the_review.delete()
        messages.success(request, 'Review Deleted Successfully!')
        return redirect('users:userReviews')


def userProfile(request, pk: int):
    user = Reader.objects.get(pk=pk)
    context = {'user': user}
    return render(request, 'MyUsers/profile.html', context)


def editProfile(request, pk: int):
    user = Reader.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated')
            return redirect('users:userProfile', pk)
        else:
            messages.error(request, 'Please Be Conscious')
            return redirect('users:editProfile', pk)
    else:
        form = EditForm(instance=user)

    context = {'form': form, 'user': user}
    return render(request, 'MyUsers/edit_profile.html', context)


@login_required(login_url='users:login')
def MaintenanceBooks(request):
    if request.user.is_staff:
        books = BookCopy.objects.filter(status='M').distinct()
        number = books.count()
        context = {'books': books, 'number': number}
        return render(request, 'MyUsers/maintenance.html', context)
    else:
        messages.error(request, 'Tosiriwala dear')
        return redirect('base:index')


@login_required(login_url='users:login')
def EditBookCopy(request, pk: int):
    if request.user.is_staff:
        bookCopy = BookCopy.objects.get(pk=pk)
        bookCopy.status = 'A'
        bookCopy.save()
        return redirect('users:MaintenanceBooks')
    else:
        messages.error(request, 'Tosiriwala dear')
        return redirect('base:index')


@login_required(login_url='users:login')
def overDueBooks(request):
    from django.utils import timezone
    if request.user.is_staff:
        books = LibrayRecords.objects.filter(status=False).distinct()
        overdue = [record for record in books if record.projected_date < timezone.now()]
        context = {'records': overdue}
        return render(request, 'MyUsers/due_books.html', context)


def logUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        try:
            user = Reader.objects.get(email=username)
        except Reader.DoesNotExist:
            messages.error(request, 'Wrong Email Address or Password')
            return redirect('users:login')

        gate_pass = authenticate(request, username=username, password=request.POST['password'])
        if gate_pass:
            login(request, user)
            messages.success(request, f'You have successfully logged in as {user.username.title()}')
            return redirect('base:index')
        else:
            messages.error(request, 'Wrong Email Address or Password')
            return redirect('users:login')

    form = LoginForm()
    context = {'form': form}
    return render(request, 'MyUsers/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('base:index')


def registerUser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save(commit=False)
            user.username = form.cleaned_data['first_name'][0].upper() + form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            login(request, user)
            return redirect('base:index')
        else:
            messages.error(request, form.errors)
            return redirect('users:register')

    form = RegisterForm()
    context = {'form': form}
    return render(request, 'MyUsers/register.html', context)
