from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.books.models import *
from apps.users.models import *
import datetime

#borrow a book
@login_required
def Borrow(request,pk):
        bk =get_object_or_404(Book,pk=pk)
        stu = request.user.students
        if stu.books_due < 4:
            if bk.available_copies >2:
               message = "Your request to borrow a book has been received!"
               borrower = Borrower()
               borrower.student = stu
               borrower.book = bk
               borrower.issue_date = datetime.datetime.now()
               borrower.return_date =datetime.date.today()+datetime.timedelta(weeks=3)
               bk.available_copies = bk.available_copies - 1
               bk.save()
               stu.books_due = stu.books_due + 1
               stu.save()
               borrower.save()
               print(borrower)
            else:
                message = "Remaining copies less than 2,reserved."
        else:
             message = "you have exceeded limit."
        return render(request, 'management/result.html', locals())


#return a book
@login_required
def returnbook(request, pk):
    if not request.user.is_staff:
        return redirect('frontpage')

    borrower = Borrower.objects.get(id=pk)
    book_pk=borrower.book.id
    student_pk=borrower.student.id

    student = Student.objects.get(id=student_pk)
    student.books_due=student.books_due-1
    student.save()

    book=Book.objects.get(id=book_pk)
    book.quantity=book.quantity+1
    book.save()
    borrower.delete()
    message = "Book has been returned."
    return render(request, 'management/result.html', locals())

#show student book list
@login_required
def student_BookListView(request):
    student=request.user.students
    bor=Borrower.objects.filter(student=student)
    bor_list=[]
    for b in bor:
        bor_list.append(b)
    return render(request, 'management/student_book_list.html', locals())

def search_student(request):
    student_list = Student.objects.all()
    student_filter = StudentFilter(request.GET, queryset=student_list)
    return render(request, 'management/search_student_list.html', {'filter': student_filter})