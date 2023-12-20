"""
@Author: Ravi Singh

@Date: 2023-12-12 12:20:30

@Last Modified by:

@Last Modified time: 2023-18-12 14:20:30

@Title : Multiple Address Book
"""
import csv
import json


class Contact:
    def __init__(self, f_name, l_name, address, city, zip_code, state, ph_no, e_mail):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.state = state
        self.ph_no = ph_no
        self.e_mail = e_mail
        self.file = "read_write.txt"

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
                    change = input(f'Enter the new State')
                    self.state = change
                case 6:
                    change = input(f'Enter new Phone Number: ')
                    self.ph_no = change
                case 7:
                    change = input(f'Enter new E-Mail: ')
                    self.e_mail = change
                case 0:
                    break

    def display_contact(self):
        """
                Description: display_contact function is to display the details of a contact
                             from the address book.

                Parameter: Self Object as a Parameter.

                Return:    None

        """

        print(f"""
                First Name: {self.f_name} 
                Last Name: {self.l_name} 
                Address : {self.address}
                City : {self.city}
                Zip Code : {self.zip_code}
                Phone Number: {self.ph_no}
                E-Mail : {self.e_mail}  
        """)

    def add_contact_to_file(self):
        """
        Description: This function return contact info dict.
        Parameter: self object as parameter.
        Return: contact info dict.
        """
        return {"f_name": self.f_name, "l_name": self.l_name, "address": self.address,
                "city": self.city, "state": self.state, "pin": self.zip_code, "phone": self.ph_no, "email": self.e_mail}


class AddressBook:
    def __init__(self, book_name):
        self.json_contact_dict = {}
        self.book_name = book_name
        self.contact_dict = {}

    def add_contact(self, contact_obj: Contact):
        """
            Description: add_contact function is used to add new contact to the contact
                         dictionary.

            Parameter: Self Object as a Parameter, Contact Object

            Return:    None

        """
        if contact_obj.f_name not in self.contact_dict:
            self.contact_dict.update({contact_obj.f_name: contact_obj})
        else:
            print(f'Name Already Present\n')

    def modify_contact(self, name):
        """
            Description: modify_contact function modifies the details of an existing contact
                        in the Address Book.

            Parameter: Self Object as a Parameter, First Name

            Return:    None

        """
        contact_obj: Contact = self.contact_dict.get(name)
        if contact_obj:
            contact_obj.update_contact()
        else:
            print("Element NOt Found or Dictionary is empty. ")

    def delete_contact(self, first_name):
        """
            Description: delete_contact function is used to delete the details of a person
                         from the address book.

            Parameter: Self Object as a Parameter, First Name

            Return:    None

        """
        contact_obj: Contact = self.contact_dict.get(first_name)
        if contact_obj:
            self.contact_dict.pop(first_name)
        else:
            print(f'Name not found or dictionary is empty.')

    def display_city_contact(self, city_name):
        """
            Description: display_city_contact displays the details of all the contacts in a
                         particular City or State.

            Parameter: Self Object as a Parameter, City Name

            Return:    None

        """
        contact = dict(filter(lambda x: x[1].city == city_name or x[1].state == city_name, self.contact_dict.items()))
        for i in contact.values():
            i.display_contact()

    def count_city_contact(self, city_name):
        """
            Description: count_city_contact function counts the number of contacts in a
                         particular City or State.

            Parameter: Self Object as a Parameter, City Name

            Return:    None

        """
        contact = dict(filter(lambda x: x[1].city == city_name or x[1].state == city_name, self.contact_dict.items()))
        print(f'There are {len(contact)}  contact in the {city_name}')

    def sort_contact(self):
        """
            Description: sort_contact function sort the contact of a particular Address
                        Book by their first name.

            Parameter: Self Object as a Parameter.

            Return:    None

        """
        for key, value in sorted(self.contact_dict.items()):
            value.display_contact()

    def sort_contact_city(self, city_name):
        """
            Description: sort_contact_city function sort the contacts by their city name or
                        state name.

            Parameter: Self Object as a Parameter, City Name

            Return:    None

        """
        sorted_contact = sorted(self.contact_dict.values(), key=lambda x: x.city == city_name, reverse=True)
        for i in sorted_contact:
            i: Contact
            print(i.f_name, '>>>>', i.city)

    def add_json_contact(self):
        """
        Description: This function is read and write data in csv file.
        Parameter: self object as parameter.
        Return: None
        """
        for key, value in self.contact_dict.items():
            self.json_contact_dict.update({key: value.add_contact_to_file()})


class MultipleAddressBook:
    def __init__(self):
        self.file_json = "contacts.json"
        self.address_book_dict = {}
        self.file = "contacts.txt"
        self.file_csv = "contacts.csv"

    def add_address_book(self, address_book_obj):
        """
            Description: add_address_book function adds the address book to the
                         multi address book dictionary.

            Parameter: Self object as a parameter, Address Book Object

            Return:    None

        """

        self.address_book_dict.update({address_book_obj.book_name: address_book_obj})

    def get_address_book(self, book_name):
        """
            Description: get_address_book function gets the address book dictionary from
                         multi address book dictionary.

            Parameter: Self object as a parameter, Book Name

            Return:    None

        """
        return self.address_book_dict.get(book_name)

    def to_txt_file(self):
        """
            Description: to_txt_file function writes the details of a contact
                        in a text format in different file.

            Parameter: Self Object as a Parameter

            Return:    None

        """

        with open(self.file, 'a', newline="") as file:
            for book, book_obj in self.address_book_dict.items():
                book_obj: AddressBook
                for contact, contact_obj in book_obj.contact_dict.items():
                    contact_obj: Contact
                    file.write(str(f'{contact_obj.add_contact_to_file()}\n'))

    def to_csv_file(self):
        with open(self.file_csv, 'w', newline="") as file:
            field_names = ['book_name', 'f_name', 'l_name', 'address', 'city', 'state', 'zip_code', 'ph_no',
                           'e_mail']
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            for book, book_obj in self.address_book_dict.items():
                book_obj: AddressBook
                for contact, contact_obj in book_obj.contact_dict.items():
                    data = contact_obj.add_contact_to_file()
                    data.update({'book_name': contact})
                    writer.writerow(data)

    def to_json_file(self):

        """
        Description: This function for writing data in json file.
        Parameter: self object as parameter.
        Return: None
        """
        json_dict = {}
        for name, obj in self.address_book_dict.items():
            json_dict.update({name: obj.json_contact_dict})
        with open(self.file_json, 'a') as file:
            json.dump(json_dict, file, indent=4)
            file.close()


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
              f'6. Get All the contacts of a city\n'
              f'7. Get number of contacts in state or city\n'
              f'8. Sort the Contacts\n'
              f'9. Sort the contacts by City or State.\n'
              f'10. Read and Write Contacts in the Address Book in Text File\n'
              f'11. Read and Write Contacts in the Address Book in CSV file\n'
              f'12. Read and Write Contacts in the Address Book in json file' 
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
                state = input('Enter the State: ')
                ph_no = input('Enter the Phone Number of the Person ')
                email = input('Enter the E-Mail of the Person ')
                contact_obj = Contact(f_name, l_name, address, city, zip_code, state, ph_no, email)
                address_book_obj.add_contact(contact_obj)
                multi_address_book_obj.add_address_book(address_book_obj)
                address_book_obj.add_json_contact()

            case 3:
                book_name = input('Enter the name of the Address Book: ')
                address_book_obj = multi_address_book_obj.get_address_book(book_name)
                name = input('Enter the first name of the contact: ')
                address_book_obj.modify_contact(name)
            case 4:
                book_name = input('Enter the name of the Address Book: ')
                address_book_obj = multi_address_book_obj.get_address_book(book_name)
                first_name = input('Enter the name of the contact you want to delete: ')
                address_book_obj.delete_contact(first_name)
            case 5:
                book_name = input('Enter the name of the Address Book: ')
                address_book_obj = multi_address_book_obj.get_address_book(book_name)
                address_book_obj.display_contact()
            case 6:
                book_name = input('Enter the name of the Address Book: ')
                address_book_obj = multi_address_book_obj.get_address_book(book_name)
                city_name = input('Enter the City or State Name: ')
                address_book_obj.display_city_contact(city_name)
            case 7:
                book_name = input('Enter the name of the Address Book: ')
                address_book_obj = multi_address_book_obj.get_address_book(book_name)
                city_name = input('Enter the City or State Name: ')
                address_book_obj.count_city_contact(city_name)
            case 8:
                book_name = input('Enter the name of the Address Book: ')
                address_book_obj = multi_address_book_obj.get_address_book(book_name)
                address_book_obj.sort_contact()
            case 9:
                book_name = input('Enter the name of the Address Book: ')
                address_book_obj = multi_address_book_obj.get_address_book(book_name)
                city_name = input('Enter the City or State Name: ')
                address_book_obj.sort_contact_city(city_name)
            case 10:
                multi_address_book_obj.to_txt_file()
            case 11:
                multi_address_book_obj.to_csv_file()
            case 12:
                multi_address_book_obj.to_json_file()


if __name__ == "__main__":
    print(f'Welcome to the Address Book Program in AddressBookMain class on Master Branch. ')
    contact_details()
