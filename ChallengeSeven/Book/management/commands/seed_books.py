from django.core.management.base import BaseCommand
from Book.models import BookData

class Command(BaseCommand):
    help = "Seed database with 20 books"

    def handle(self, *args, **kwargs):
        books = [
            {"name": "The Hobbit", "category": "Fantasy", "description": "A hobbit's adventure.", "rating": 4.8},
            {"name": "1984", "category": "Fiction", "description": "Dystopian novel.", "rating": 4.7},
            {"name": "To Kill a Mockingbird", "category": "Fiction", "description": "Classic literature.", "rating": 4.9},
            {"name": "A Brief History of Time", "category": "Science", "description": "Cosmology overview.", "rating": 4.6},
            {"name": "The Selfish Gene", "category": "Science", "description": "Evolutionary biology.", "rating": 4.5},
            {"name": "The Iliad", "category": "History", "description": "Ancient Greek epic.", "rating": 4.3},
            {"name": "The Odyssey", "category": "Adventure", "description": "Epic journey home.", "rating": 4.4},
            {"name": "The Art of War", "category": "History", "description": "Military strategy.", "rating": 4.6},
            {"name": "The Shining", "category": "Horror", "description": "Psychological horror novel.", "rating": 4.7},
            {"name": "Dracula", "category": "Horror", "description": "Classic vampire story.", "rating": 4.6},
            {"name": "Pride and Prejudice", "category": "Romance", "description": "Love and society.", "rating": 4.9},
            {"name": "Jane Eyre", "category": "Romance", "description": "Gothic romance.", "rating": 4.8},
            {"name": "Becoming", "category": "Biography", "description": "Michelle Obama's story.", "rating": 4.7},
            {"name": "Steve Jobs", "category": "Biography", "description": "Apple founder bio.", "rating": 4.5},
            {"name": "The Raven", "category": "Poetry", "description": "Poem by Edgar Allan Poe.", "rating": 4.4},
            {"name": "Leaves of Grass", "category": "Poetry", "description": "Collection by Walt Whitman.", "rating": 4.6},
            {"name": "The Da Vinci Code", "category": "Mystery", "description": "Mystery thriller.", "rating": 4.5},
            {"name": "Gone Girl", "category": "Mystery", "description": "Psychological thriller.", "rating": 4.6},
            {"name": "The Great Gatsby", "category": "Fiction", "description": "1920s tragedy.", "rating": 4.8},
            {"name": "Moby Dick", "category": "Adventure", "description": "Hunt for the white whale.", "rating": 4.3},
        ]

        for b in books:
            BookData.objects.get_or_create(name=b["name"], defaults=b)

        self.stdout.write(self.style.SUCCESS("Database seeded with 20 books."))