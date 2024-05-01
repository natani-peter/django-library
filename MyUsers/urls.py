from django.urls import path

from MyUsers import views

app_name = 'users'

urlpatterns = [
    path('login/', views.logUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('my-borrowed-books/', views.borrowed_book, name='borrowed'),
    path('my-returned-books/', views.returned_book, name='returned'),
    path('my-reviews/', views.userReviews, name='userReviews'),
    path('edit-review/<int:pk>/', views.edit_review, name='review_edit'),
    path('reply/<int:pk>/<int:book_id>/', views.replyReview, name='replyReview'),
    path('reply-to-reply/<int:pk>/<int:book_id>/', views.replyReply, name='reply_reply'),
    path('user/<int:pk>/', views.userProfile, name='userProfile'),
    path('confirm-delete-review/<int:pk>/', views.confirm_delete, name='confirm_delete'),
    path('delete-review/<int:pk>/', views.delete_review, name='review_delete'),
    path('edit-profile/<int:pk>/', views.editProfile, name='editProfile'),
    path('maintenance-books/', views.MaintenanceBooks, name='MaintenanceBooks'),
    path('change-status/<int:pk>/', views.EditBookCopy, name='editBookCopy'),
    path('overdue-books/', views.overDueBooks, name='overdueBooks'),
]
