from datetime import datetime

# Homework 1: ToDo List Application

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True

    def list_tasks(self):
        for task in self.tasks:
            status = "Done" if task.completed else "Pending"
            print(f"{task.title} - {status} - Due: {task.due_date}")

    def incomplete_tasks(self):
        for task in self.tasks:
            if not task.completed:
                print(f"{task.title} - Due: {task.due_date}")

# Homework 2: Simple Blog System

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now()

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        for post in self.posts:
            print(f"{post.title} by {post.author} - {post.timestamp}\n{post.content}\n")

    def posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(f"{post.title} - {post.timestamp}\n{post.content}\n")

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content

    def latest_posts(self):
        sorted_posts = sorted(self.posts, key=lambda x: x.timestamp, reverse=True)
        for post in sorted_posts[:5]:
            print(f"{post.title} by {post.author} - {post.timestamp}\n{post.content}\n")

# Homework 3: Simple Banking System

class Account:
    def __init__(self, number, holder, balance=0):
        self.number = number
        self.holder = holder
        self.balance = balance

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, number):
        for acc in self.accounts:
            if acc.number == number:
                return acc
        return None

    def check_balance(self, number):
        acc = self.find_account(number)
        if acc:
            return acc.balance

    def deposit(self, number, amount):
        acc = self.find_account(number)
        if acc:
            acc.balance += amount

    def withdraw(self, number, amount):
        acc = self.find_account(number)
        if acc and acc.balance >= amount:
            acc.balance -= amount

    def transfer(self, from_number, to_number, amount):
        from_acc = self.find_account(from_number)
        to_acc = self.find_account(to_number)
        if from_acc and to_acc and from_acc.balance >= amount:
            from_acc.balance -= amount
            to_acc.balance += amount

    def account_details(self, number):
        acc = self.find_account(number)
        if acc:
            print(f"Account: {acc.number}, Holder: {acc.holder}, Balance: {acc.balance}")

    def overdraft_check(self, number):
        acc = self.find_account(number)
        if acc and acc.balance < 0:
            print(f"Warning: Account {acc.number} is overdrawn!")
