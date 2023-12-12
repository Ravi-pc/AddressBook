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
    def __init__(self):
        self.contact_dict = {}


def contact_details():
    """
        Description: contact_details function used to get the details of a person for
                     the address book from the user.

        Parameter: None

        Return:    None

    """
    f_name = input('Enter the First name of the Person ')
    l_name = input('Enter the Last name of the Person ')
    address = input('Enter the Address of the Person ')
    city = input('Enter the City of the Person ')
    zip_code = input('Enter the Zip code of the area ')
    ph_no = input('Enter the Phone Number of the Person ')
    email = input('Enter the E-Mail of the Person ')
    contact1 = Contact(f_name, l_name, address, city, zip_code, ph_no, email, )


if __name__ == "__main__":
    print(f'Welcome to the Address Book Program in AddressBookMain class on Master Branch. ')
    contact_details()
