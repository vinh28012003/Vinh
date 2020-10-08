books = [
    "Books 1", "Harry Potter", "Blink", "Romeo and Juliet"
]
while True:
    userInput = input("Enter here: ")
    #for book in books:
     #   if userInput == book.lower():
      #      print(book)
       #     break
        #else:
         #   print("Not found")

    if userInput in books:
    index = books.index(userInput)
    print(books[index])
    break