"""
@Author: Ravi Singh

@Date: 2023-12-12 12:20:30

@Last Modified by:

@Last Modified time: 2023-12-12 15:20:30

@Title : Multiple Address Book
"""


class Contact:
    def __init__(self, f_name, l_name, address, city, zip_code, ph_no, e_mail):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.ph_no = ph_no
        self.e_mail = e_mail


class AddressBook:
    def __init__(self, book_name):
        self.book_name = book_name
        self.contact_dict = {}

    def add_contact(self, contact_obj: Contact):
        """
            Description: add_contact function is used to add new contact to the contact
                         dictionary.

            Parameter: Contact Object

            Return:    None

        """
        self.contact_dict.update({contact_obj.f_name: contact_obj})


def contact_details():
    """
        Description: contact_details function used to get the details of a person for
                     the address book from the user.

        Parameter: None

        Return:    None

    """
    book_name = input('Enter the name of the Address Book: ')
    address_book_obj = AddressBook(book_name)
    while True:
        print(f'1. Add New Contact\n'
              f'0. Exit ')
        choice = int(input('Enter your choice: '))
        match choice:
            case 0:
                break
            case 1:
                f_name = input('Enter the First name of the Person ')
                l_name = input('Enter the Last name of the Person ')
                address = input('Enter the Address of the Person ')
                city = input('Enter the City of the Person ')
                zip_code = input('Enter the Zip code of the area ')
                ph_no = input('Enter the Phone Number of the Person ')
                email = input('Enter the E-Mail of the Person ')
                contact_obj = Contact(f_name, l_name, address, city, zip_code, ph_no, email, )
                address_book_obj.add_contact(contact_obj)


if __name__ == "__main__":
    print(f'Welcome to the Address Book Program in AddressBookMain class on Master Branch. ')
    contact_details()
