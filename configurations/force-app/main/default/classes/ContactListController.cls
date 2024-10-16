public with sharing class ContactListController {
    
    @AuraEnabled(cacheable=true)
    public static List<Contact> getContactList(Id accountId) {
        return [
            SELECT Id, Name, Email, Phone
            FROM Contact
            WHERE AccountId = :accountId
        ];
    }
}