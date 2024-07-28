from django.db import models
import datetime
from django.contrib.auth.models import User
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='images', default='https://media.istockphoto.com/id/1337144146/vector/default-avatar-profile-icon-vector.jpg?s=612x612&w=0&k=20&c=BIbFwuv7FxTWvh5S3vB6bkT0Qv8Vn8N5Ffseq84ClGI=',blank=True)
    created_on = models.DateField(default=datetime.date.today)
    updated_on = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    caption = models.TextField(blank=True)
    created_on = models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.caption

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_on = models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.text

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_on = models.DateField(default=datetime.date.today)


    def __str__(self):
        return f'{self.user.username} likes {self.post.caption}'

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_on = models.DateField(default=datetime.date.today)


    class Meta:
        unique_together = ('follower', 'following')
        

    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateField(default=datetime.date.today)


    def __str__(self):
        return f'Message from {self.sender.username} to {self.recipient.username}'