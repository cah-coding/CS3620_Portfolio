from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=100)      # Name of the story
    description = models.TextField(blank=True)    # Short summary for homepage
    template = models.TextField()                 # Example: "The {noun1} jumped over the {noun2}."
    field_labels = models.JSONField()             # Example: ["noun1", "noun2", "adjective"]

    def __str__(self):
        return self.title
