
import dropbox
db = dropbox.Dropbox('b77FaSqXIFcAAAAAAAAAAUH7zEJfypOZlDkNltzYLDbGvdnONlTER4t2xGE5KxXx')
print(db.users_get_current_account())