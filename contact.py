"""
@Author: Ravi Singh

@Date: 2023-12-12 12:20:30

@Last Modified by:

@Last Modified time: 2023-13-12 11:20:30

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

    def update_contact(self, f_name):
        """
            Description: update_contact function is used to update the details of a person
                         from the address book.

            Parameter: First Name

            Return:    None

        """
        contact_obj: Contact = self.contact_dict.get(f_name)
        if contact_obj:
            while True:
                print(f'1. Update First Name.\n'
                      f'2. Update Last Name.\n'
                      f'3. Update Address\n'
                      f'4. Update City\n'
                      f'5. Update Zip Code\n'
                      f'6. Update Phone Number\n'
                      f'7. Update E-Mail\n'
                      f'0. Exit'
                      )
                option = int(input('Enter the option:  '))
                match option:
                    case 1:
                        change = input(f'Enter new first name: ')
                        self.contact_dict.update({f_name: change})
                    case 2:
                        change = input(f'Enter new last name: ')
                        self.contact_dict.update({f_name: change})
                    case 3:
                        change = input(f'Enter new Address: ')
                        self.contact_dict.update({f_name: change})
                    case 4:
                        change = input(f'Enter new City: ')
                        self.contact_dict.update({f_name: change})
                    case 5:
                        change = input(f'Enter new Zip Code: ')
                        self.contact_dict.update({f_name: change})
                    case 6:
                        change = input(f'Enter new Phone Number: ')
                        self.contact_dict.update({f_name: change})
                    case 7:
                        change = input(f'Enter new E-Mail: ')
                        self.contact_dict.update({f_name: change})
                    case 0:
                        break
        else:
            print(f'No Element found of this name')


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
              f'2. Update an Existing Contact\n'
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
            case 2:
                name = input('Enter the first name of the contact: ')
                address_book_obj.update_contact(name)


if __name__ == "__main__":
    print(f'Welcome to the Address Book Program in AddressBookMain class on Master Branch. ')
    contact_details()
