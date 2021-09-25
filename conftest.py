import pytest

from fixture.application import Applcation


@pytest.fixture(scope="session")
def app(request):
    fixture = Applcation("C:\\Users\\marat\\Downloads\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture



