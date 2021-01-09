# RFID-Multitool
A script to perform various functions based on scanning a PN532 RFID reader.

### Dependencies
- My [PN532-python-lib](https://github.com/combateer3/PN532-python-lib)

### Description
`map.csv` holds pairs of UIDs and actions. When a tag is read, the script will perform the action tied to that particular UID.  For example, a particular tag could map an action
to send me a text of my Raspberry Pi's IP address.  Another could send me an email of some compiled data from another script.
