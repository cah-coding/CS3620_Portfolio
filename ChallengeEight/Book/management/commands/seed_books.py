from django.core.management.base import BaseCommand
from Book.models import BookData

class Command(BaseCommand):
    help = "Seed database with 50 books"

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
            {"name": "Brave New World", "category": "Fiction", "description": "Dystopian society story.", "rating": 4.7},
            {"name": "Sapiens", "category": "Science", "description": "Human history and biology.", "rating": 4.8},
            {"name": "Educated", "category": "Biography", "description": "A woman's journey to education.", "rating": 4.7},
            {"name": "The Catcher in the Rye", "category": "Fiction", "description": "Teen angst and rebellion.", "rating": 4.2},
            {"name": "The Alchemist", "category": "Adventure", "description": "Spiritual journey to destiny.", "rating": 4.6},
            {"name": "The Time Machine", "category": "Science", "description": "Time travel classic.", "rating": 4.4},
            {"name": "Frankenstein", "category": "Horror", "description": "The creation of a monster.", "rating": 4.5},
            {"name": "Wuthering Heights", "category": "Romance", "description": "Tragic love on the moors.", "rating": 4.6},
            {"name": "Sherlock Holmes", "category": "Mystery", "description": "Detective stories.", "rating": 4.9},
            {"name": "Inferno", "category": "Mystery", "description": "Dante-inspired thriller.", "rating": 4.4},
            {"name": "The Road", "category": "Fiction", "description": "Post-apocalyptic journey.", "rating": 4.5},
            {"name": "The Martian", "category": "Science", "description": "Survival on Mars.", "rating": 4.7},
            {"name": "Into the Wild", "category": "Adventure", "description": "Man’s journey into wilderness.", "rating": 4.6},
            {"name": "It", "category": "Horror", "description": "Small town haunted by evil.", "rating": 4.7},
            {"name": "The Notebook", "category": "Romance", "description": "Enduring love story.", "rating": 4.8},
            {"name": "The Silent Patient", "category": "Mystery", "description": "Psychological suspense.", "rating": 4.6},
            {"name": "Dune", "category": "Science", "description": "Epic interstellar saga.", "rating": 4.9},
            {"name": "The Metamorphosis", "category": "Fiction", "description": "Man wakes up as insect.", "rating": 4.2},
            {"name": "Les Misérables", "category": "History", "description": "Redemption and revolution.", "rating": 4.9},
            {"name": "Don Quixote", "category": "Adventure", "description": "Knight’s delusional quest.", "rating": 4.4},
            {"name": "Heart of Darkness", "category": "History", "description": "Journey into the Congo.", "rating": 4.3},
            {"name": "A Game of Thrones", "category": "Fantasy", "description": "Epic fantasy politics.", "rating": 4.8},
            {"name": "The Fellowship of the Ring", "category": "Fantasy", "description": "Journey begins to destroy the ring.", "rating": 4.9},
            {"name": "Catching Fire", "category": "Adventure", "description": "Sequel to The Hunger Games.", "rating": 4.7},
            {"name": "The Hunger Games", "category": "Adventure", "description": "Survival competition dystopia.", "rating": 4.8},
            {"name": "A Tale of Two Cities", "category": "History", "description": "French Revolution story.", "rating": 4.6},
            {"name": "The Color Purple", "category": "Fiction", "description": "Southern woman’s resilience.", "rating": 4.8},
            {"name": "The Divine Comedy", "category": "Poetry", "description": "Journey through Hell and Heaven.", "rating": 4.7},
            {"name": "The Immortal Life of Henrietta Lacks", "category": "Biography", "description": "True science story.", "rating": 4.8},
            {"name": "The Name of the Wind", "category": "Fantasy", "description": "A wizard recounts his life.", "rating": 4.9},
            {"name": "The Girl with the Dragon Tattoo", "category": "Mystery", "description": "Dark Swedish crime story.", "rating": 4.6},
        ]

        for b in books:
            BookData.objects.get_or_create(name=b["name"], defaults=b)

        self.stdout.write(self.style.SUCCESS(f"Database seeded with {len(books)} books."))