
#1-project
class Task:
    def __init__(self,title,description,duedate,status):
        self.title=title 
        self.description=description
        self.duedate=duedate
        self.status = status
    def mark(self):
        self.status='completed'
        return f"bu mashq {self.status} va vaqti {self.duedate}"
    def __str__(self):
        return f"{self.title} - {self.status} (Due: {self.duedate})"
class ToDoList:
    def __init__(self):
        self.tasks=[]
    def add_task(self,task):
        self.tasks.append(task)
    def all_incompleted(self):
        for s in self.tasks:
            if s.status=="incompleted":
                print(s)
    def all_completed(self):
        for t in self.tasks:
            if t.status=="completed":
                print(t)
    def list_all_tasks(self):
        for n in self.tasks:
            print(n)


task1 = Task("Uy ishi", "Matematika mashqlarini bajarish", "2025-10-16", "incompleted")
task2=Task("sinf ishi",'english','2025-10-18','completed')
task3=Task("zad ishi",'drawing a picture',"2025-10-17",'completed')
print(task3.mark())

todo = ToDoList()
todo.add_task(task1)
todo.add_task(task2)
todo.add_task(task3)


print("\nBarcha vazifalar:")
todo.list_all_tasks()

print("\nBajarilmaganlar:")
todo.all_incompleted()

print('\nBajarilganlar')
todo.all_completed()

while True:
    print("1. Yangi vazifa qo'shish")
    print("2. Vazifani bajarilgan deb belgilash")
    print("3. Barcha vazifalarni ko'rish")
    print("4. Faqat bajarilmaganlarni ko'rish")
    print("5. Chiqish")
    choice=input('tanlov tanlang')
    if choice == "1":
        if choice == "1":
            title = input("Vazifa nomi: ")
            desc = input("Tavsif: ")
            due = input("Muddati (yyyy-mm-dd): ")
            task = Task(title, desc, due, "incompleted")
            todo.add_task(task)
        print(" Vazifa qo'shildi.")
    
    elif choice == "2":
        title = input("Qaysi vazifa bajarildi (nomini kiriting): ")
        for t in todo.tasks:
            if t.title == title:
                t.mark()
                print(" Vazifa bajarilgan deb belgilandi.")
                break
            else:
                print("Bunday vazifa topilmadi.")
    elif choice == "3":
        print("barcha vazifalarni ko'rish")
        todo.list_all_tasks()
    elif choice == "4":
        print("faqat bajarilmaganlarini ko'rish")
        todo.all_incompleted()
    elif choice == "5":
        print("Dastur tugadi.")
        break
    else:
        print("Noto'g'ri tanlov, qayta urinib ko'ring.")


#2-project 
# Define Post class
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"

# Define Blog class
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print("Post added!")

    def list_posts(self):
        if not self.posts:
            print("No posts yet.")
        for post in self.posts:
            print(post)

    def display_by_author(self, author):
        found = [p for p in self.posts if p.author == author]
        if not found:
            print(f"No posts by {author}")
        for post in found:
            print(post)

    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print(f"Deleted post: {title}")
                return
        print(f"No post found with title {title}")

    def edit_post(self, title, new_title=None, new_content=None):
        for post in self.posts:
            if post.title == title:
                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content
                print(f"Post updated: {title}")
                return
        print(f"No post found with title {title}")

    def latest_posts(self, n=5):
        print(f"Latest {n} posts:")
        for post in self.posts[-n:][::-1]:
            print(post)

# Main program (CLI)
def main():
    blog = Blog()
    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
        elif choice == "2":
            blog.list_posts()
        elif choice == "3":
            author = input("Author name: ")
            blog.display_by_author(author)
        elif choice == "4":
            title = input("Title to delete: ")
            blog.delete_post(title)
        elif choice == "5":
            title = input("Title to edit: ")
            new_title = input("New title (or leave blank): ")
            new_content = input("New content (or leave blank): ")
            blog.edit_post(title, new_title if new_title else None, new_content if new_content else None)
        elif choice == "6":
            n = int(input("How many latest posts to show? "))
            blog.latest_posts(n)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()


#3-project 
# Define Account class
class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def __str__(self):
        return f"Account: {self.acc_number}\nHolder: {self.holder_name}\nBalance: ${self.balance:.2f}"

# Define Bank class
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print("Account added!")

    def find_account(self, acc_number):
        for acc in self.accounts:
            if acc.acc_number == acc_number:
                return acc
        return None

    def check_balance(self, acc_number):
        acc = self.find_account(acc_number)
        if acc:
            print(f"Balance for account {acc_number}: ${acc.balance:.2f}")
        else:
            print("Account not found.")

    def deposit(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            acc.balance += amount
            print(f"${amount:.2f} deposited. New balance: ${acc.balance:.2f}")
        else:
            print("Account not found.")

    def withdraw(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            if acc.balance >= amount:
                acc.balance -= amount
                print(f"${amount:.2f} withdrawn. New balance: ${acc.balance:.2f}")
            else:
                print("Insufficient funds!")
        else:
            print("Account not found.")

    def transfer(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)
        if sender and receiver:
            if sender.balance >= amount:
                sender.balance -= amount
                receiver.balance += amount
                print(f"${amount:.2f} transferred from {from_acc} to {to_acc}.")
            else:
                print("Insufficient funds to transfer!")
        else:
            print("One or both accounts not found.")

    def display_account(self, acc_number):
        acc = self.find_account(acc_number)
        if acc:
            print(acc)
        else:
            print("Account not found.")

# Main program (CLI)
def main():
    bank = Bank()
    while True:
        print("\n--- Simple Banking System ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            acc_number = input("Account Number: ")
            holder = input("Holder Name: ")
            balance = float(input("Initial Balance: "))
            bank.add_account(Account(acc_number, holder, balance))

        elif choice == "2":
            acc_number = input("Account Number: ")
            bank.check_balance(acc_number)

        elif choice == "3":
            acc_number = input("Account Number: ")
            amount = float(input("Amount to deposit: "))
            bank.deposit(acc_number, amount)

        elif choice == "4":
            acc_number = input("Account Number: ")
            amount = float(input("Amount to withdraw: "))
            bank.withdraw(acc_number, amount)

        elif choice == "5":
            from_acc = input("From Account: ")
            to_acc = input("To Account: ")
            amount = float(input("Amount to transfer: "))
            bank.transfer(from_acc, to_acc, amount)

        elif choice == "6":
            acc_number = input("Account Number: ")
            bank.display_account(acc_number)

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
