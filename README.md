# projectOTP
Send Messages using Python and SMS service provider.

# SMS service provider
Fast2SMS is used as the default sms service provider for this program. It will give you ₹50 or whatever currency it is at your country. It is easy to use. If you feel you can or have to use any other service provider you have to modify the code in send.py.

# Changes to be made in the script for use
For use the script has to be changed otherwise it will give a number of errors. Kindly make the changes give below. 

### Authorization
```
# refer  to line 7

'authorization' = '# Your Fast2SMS authorization key'

# in place of # Your Fast2SMS authorization key you need to fill your fast2sms api key which will be available to you in the Dev API section of the website. Remember to keep the inverted commas (' ').
```

### Sender ID
```
# refer to line 8

'sender_id' = 'FSTSMS'

# default sender_id is kept to 'FSTSMS' if you want to keep the sender_id as custom you need to change it.
```

### Messsage Type
```
# refer to line 13

'flash' = "1"

# this will send a flash message if you want to send a normal message set 'flash' to "0"
```

# Sending messages to multiple messages

If you want to send a message to multiple numbers write numbers seperated by commas when it asks for the numbe.
