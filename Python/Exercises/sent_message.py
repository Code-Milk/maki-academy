sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
    file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
    # Read the sent message from the file
    original_message = file.read()
      
    # Move the cursor to the beginning of the file
    file.seek(0)

    # Modify the message to simulate unsending
    unsent_message = 'This message has been unsent.'

    # Use Truncate to reset the content to the length of the unsend message
    file.truncate(len(unsent_message))

    # Write new message
    file.write(unsent_message)

# Print your messages
print('Original Message: ', original_message)
print('Unsent Message: ', unsent_message)