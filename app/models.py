from django.db import models
import base64

# Create your models here.
class Repository(models.Model):
    repo_id = models.IntegerField(primary_key=True)
    repo_title = models.TextField(blank=False)
    repo_password = models.TextField(blank=False)
    repo_post_count = models.IntegerField()

    def to_dict_json(self):
        return {
            'repo_id':self.repo_id,
            'repo_title':self.repo_title,
            'repo_password':self.repo_password,
            'repo_post_count':self.repo_post_count,
        }

class Post(models.Model): 
    post_id = models.IntegerField(primary_key=True) 
    title = models.TextField(blank=False)
    content = models.TextField(blank=False)
    pub_date = models.DateTimeField('date published')
    count = models.IntegerField()
    repo_id = models.ForeignKey("Repository", on_delete=models.CASCADE, db_column="repo_id")

    def to_dict_json(self):
        print(self.content)
        return {
            'post_id':self.post_id,
            'title':self.title,
            'content':base64.b64decode(self.content).decode('utf-8'),
            'pub_date':str(self.pub_date)[:16],
            'count':self.count,
        }


