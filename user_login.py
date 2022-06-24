#method take the argument and take first three char of First and Last Name and Last three char of user ID and return it as username
def get_login_name(fn,ln,si):
    firstName = fn[0 : 3]
    lastName = ln[0 : 3]
    studentId = si[-3 :]
    user_name = firstName + lastName + studentId
    return user_name
