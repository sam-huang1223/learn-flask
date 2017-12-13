# get all posts from a user
u = models.User.query.get(1)
#<User u'john'>
posts = u.posts.all()
#[<Post u'my first post!'>]

# obtain author of each post
for p in posts:
    print(p.id,p.author.nickname,p.body)
#1 john my first post!

# a user that has no posts
u = models.User.query.get(2)
#<User u'susan'>
u.posts.all()
#[]

# get all users in reverse alphabetical order
models.User.query.order_by('nickname desc').all()
#[<User u'susan'>, <User u'john'>]