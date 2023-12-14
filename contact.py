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

    def update_contact(self):
        """
            Description: update_contact function is used to update the details of a person
                         from the address book.

            Parameter: First Name

            Return:    None

        """
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
                    self.f_name = change
                case 2:
                    change = input(f'Enter new last name: ')
                    self.l_name = change
                case 3:
                    change = input(f'Enter new Address: ')
                    self.address = change
                case 4:
                    change = input(f'Enter new City: ')
                    self.city = change
                case 5:
                    change = input(f'Enter new Zip Code: ')
                    self.zip_code = change
                case 6:
                    change = input(f'Enter new Phone Number: ')
                    self.ph_no = change
                case 7:
                    change = input(f'Enter new E-Mail: ')
                    self.e_mail = change
                case 0:
                    break


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

    def modify_contact(self, name):
        contact_obj: Contact = self.contact_dict.get(name)
        if contact_obj:
            contact_obj.update_contact()
        else:
            print("Element NOt Found or Dictionary is empty. ")

    def delete_contact(self, first_name):
        """
            Description: delete_contact function is used to delete the details of a person
                         from the address book.

            Parameter: First Name

            Return:    None

        """
        contact_obj: Contact = self.contact_dict.get(first_name)
        if contact_obj:
            self.contact_dict.pop(first_name)
        else:
            print(f'Name not found or dictionary is empty.')

    def display_contact(self):
        """
                Description: display_contact function is to display the details of a contact
                             from the address book.

                Parameter: None

                Return:    None

        """
        for key, value in self.contact_dict.items():
            print(f"""
                     First Name: {key} 
                     Last Name: {value.l_name} 
                     Address : {value.address}
                     City : {value.city}
                     Zip Code : {value.zip_code}
                     Phone Number: {value.ph_no}
                     E-Mail : {value.e_mail}  
             """)


class MultipleAddressBook:
    def __init__(self):
        self.address_book_dict = {}

    def add_address_book(self, address_book_obj):
        self.address_book_dict.update({address_book_obj.book_name: address_book_obj})

    def get_address_book(self, book_name):
        return self.address_book_dict.get(book_name)


def contact_details():
    """
        Description: contact_details function used to get the details of a person for
                     the address book from the user.

        Parameter: None

        Return:    None

    """
    multi_address_book_obj = MultipleAddressBook()
    while True:
        print(f'1. Add a new Address Book\n'
              f'2. Add New Contact\n'
              f'3. Update an Existing Contact\n'
              f'4. Delete an Existing Contact\n'
              f'5. Display the Contacts\n'
              f'0. Exit ')
        choice = int(input('Enter your choice: '))
        match choice:
            case 0:
                break
            case 1:
                book_name = input('Enter the name of the Address Book: ')
                address_book_obj = multi_address_book_obj.get_address_book(book_name)
                if address_book_obj is None:
                    address_book_obj = AddressBook(book_name)
                f_name = input('Enter the First name of the Person ')
                l_name = input('Enter the Last name of the Person ')
                address = input('Enter the Address of the Person ')
                city = input('Enter the City of the Person ')
                zip_code = input('Enter the Zip code of the area ')
                ph_no = input('Enter the Phone Number of the Person ')
                email = input('Enter the E-Mail of the Person ')
                contact_obj = Contact(f_name, l_name, address, city, zip_code, ph_no, email)
                address_book_obj.add_contact(contact_obj)
                multi_address_book_obj.add_address_book(address_book_obj)

            case 2:
                book_name = input('Enter the name of the Address Book: ')
                address_book_obj = multi_address_book_obj.get_address_book(book_name)
                name = input('Enter the first name of the contact: ')
                address_book_obj.modify_contact(name)
            case 3:
                book_name = input('Enter the name of the Address Book: ')
                address_book_obj = multi_address_book_obj.get_address_book(book_name)
                first_name = input('Enter the name of the contact you want to delete: ')
                address_book_obj.delete_contact(first_name)
            case 4:
                book_name = input('Enter the name of the Address Book: ')
                address_book_obj = multi_address_book_obj.get_address_book(book_name)
                address_book_obj.display_contact()


if __name__ == "__main__":
    print(f'Welcome to the Address Book Program in AddressBookMain class on Master Branch. ')
    contact_details()
