from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.books.models import Book,Reviews
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from apps.users.models import Student

def search(request):
    book_list = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=book_list)
    return render(request, 'books/search_book_list.html', {'filter': book_filter})



@login_required
def RatingUpdate(request, pk=None):
    # obj = Reviews.objects.get(id=pk)
    stu=Student.objects.get(reg_no=request.user.id)
    print(stu)
    form = RatingForm()
    if request.method == 'POST':
        form = RatingForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj = Reviews()
            obj.student = stu
            print(obj)
            obj.save()
            return redirect('book-detail',pk=obj.book.id)

    return render(request, 'books/form.html', locals())


# Book List Displayed
class BookListView(ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'books'


# Book Detail Displayed
# class BookDetailView(DetailView):
#     model = Book


def BookDetailView(request, pk):
    book = get_object_or_404(Book, id=pk)
    reviews = Reviews.objects.filter(book=book).exclude(review="none")

    # stu = Student.objects.get(roll_no=request.user.id)
    rr = Reviews.objects.filter(student__id=request.user.id)
    print(rr)

    return render(request, 'books/book_detail.html', locals())


# Add a Book
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'quantity', 'category']
    template_name = 'management/book_form.html'

    def form_valid(self, form):
        form.instance.lib_author = self.request.user.username
        return super().form_valid(form)

    # Update a Book


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'quantity']

    def form_valid(self, form):
        form.instance.lib_author = self.request.user.username
        return super().form_valid(form)


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/'


