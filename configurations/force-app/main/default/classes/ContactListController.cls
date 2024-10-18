public with sharing class ContactListController {
    
    @AuraEnabled(cacheable=true)
    public static List<Contact> getContactList(Id accountId) {
        return [
            SELECT Id, FirstName, LastName, Email, Phone, MailingCity, MailingCountry, MailingPostalCode, MailingState, MailingStreet 
            FROM Contact
            WHERE AccountId = :accountId
            ORDER BY Name ASC
        ];
    }
}