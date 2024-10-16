import { LightningElement, api, wire } from 'lwc';
import getContactList from '@salesforce/apex/ContactListController.getContactList';

export default class ContactListForAccount extends LightningElement {

    @api recordId;
    contacts;
    error;

    @wire(getContactList, { accountId: '$recordId'})
    wiredContacts({ error, data }) {
        if(data) {
            this.contacts = data;
            this.error = undefined;
        } else if(error) {
            this.error = error;
            this.contacts = undefined;
        }
    }
}