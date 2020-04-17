from django.shortcuts import render, redirect
from .models import Book, Author


def add_book(request):
# main page, renders books and book info. Able to view mor details or add a new book.
    books= Book.objects.all()
    context= {
        'books': books,
    }
    return render(request,'add_book.html', context)


def submit_book(request):
# This submits the new book form and redirects to the submitted book form. then back to main book page.
    book_title= request.POST['title']
    book_desc= request.POST['desc']

    Book.objects.create(title=book_title, desc=book_desc)

    return redirect('/submitted_book_form')


def submitted_book_form(request):
# redirection back to main book page.
    return redirect('/')


def book_info(request, book_id):
# displays the book info page for more details. click the view button on the main books page.
    the_book_info= Book.objects.get(id=book_id)
    books_authors= the_book_info.authors.all()
    all_authors= Author.objects.all()

    context= {
        'the_book_info' : the_book_info,
        'books_authors' : books_authors,
        'all_authors' : all_authors
    }
    return render(request, 'book_info.html', context)


def update_book_author(request):
# update/add books authors
    book_id= request.POST['book_id']
    author_id= request.POST['author_id']

    author_added = Author.objects.get(id= author_id)
    book_from_form = Book.objects.get(id= book_id)
    
    book_from_form.authors.add(author_added)
    
    return redirect(f"/book_info/{book_id}")



def add_author(request):
# This renders the main authors page. Able to view more details and add authors.
    authors= Author.objects.all()
    context= {
        'authors' : authors,
    }
    return render(request,'add_author.html', context)


def submit_author(request):
# this submits the form for a new author, redirects to submitted author form, then back to main authors page.
    first_name= request.POST['first_name']
    last_name= request.POST['last_name']
    notes= request.POST['notes']

    Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)

    return redirect('/submitted_author_form')


def submitted_author_form(request):
# redirection for author form. 
    return redirect('/add_author')


def author_info(request, author_id):
# displays the author info page for more details. click the view button on the main books page.
    the_author_info= Author.objects.get(id=author_id)
    authors_books= the_author_info.books.all()
    all_books= Book.objects.all()

    context= {
        'the_author_info' : the_author_info,
        'authors_books' : authors_books,
        'all_books' : all_books
    }
    return render(request, 'author_info.html', context)


def update_author_book(request):
# update/add authors books
    author_id= request.POST['author_id']
    book_id= request.POST['book_id']

    book_added = Book.objects.get(id= book_id)
    author_from_form = Author.objects.get(id= author_id)
    
    author_from_form.books.add(book_added)
    
    return redirect(f"/author_info/{author_id}")




