# GMS_SE_VirtualProgram_Passsword_Cracking
Solution to problem given at Goldman Sachs Software Engineering Virtual Program


# Password Cracker


## Given Question
- Review the links provided in the additional resources below to gain a background understanding of password cracking
- Try to crack the passwords provided in the 'password dump' file below using available tools
- Assess the 5 questions in the task instructions below in relation to the passwords provided (type of hashing algorithm, level of protection, possible controls that could be implemented, password policy, changes in policy)
- Draft an email/memo briefly explaining your findings in relation to controls used by the organization and your proposed uplifts.


You must determine the following:
1. What type of hashing algorithm was used to protect passwords?
2. What level of protection does the mechanism offer for passwords?
3. What controls could be implemented to make cracking much harder for the hacker in the event of a password database leaking again?
4. What can you tell about the organization’s password policy (e.g. password length, key space, etc.)?
5. What would you change in the password policy to make breaking the passwords harder?

### Resources
- [Password cracking explained (techniques described in 2013 still haven’t changed)](https://arstechnica.com/information-technology/2013/05/how-crackers-make-minced-meat-out-of-your-passwords/)
- [Password salting](https://en.wikipedia.org/wiki/Salt_(cryptography))
- [Hash functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
- [Password cracking tools](https://en.wikipedia.org/wiki/Password_cracking#Software)
- [Password strength checker](https://howsecureismypassword.net/)


# My answer
1. What type of hashing algorithm was used to protect passwords?

- The passwords were protected using Message Digest (MD5) hash algorithm, which is considered a weaker hash algorithm.
2. What level of protection does the mechanism offer for passwords?

- The level of protection provided by the MD5 hash algorithm is not considered strong enough, as it is vulnerable to collision attacks and can be cracked easily using tools like Hashcat and wordlists.
3. What controls could be implemented to make cracking much harder for the hacker in the event of a password database leaking again?

- Stronger password encryption mechanism such as SHA should be used for creating password hashes.
- Implement password complexity rules, such as minimum password length, the inclusion of special characters, capital and small letters, and numbers.
- Implement password rotation policies to ensure that passwords are changed regularly.
Use two-factor authentication to add an additional layer of security.
4. What can you tell about the organization’s password policy (e.g. password length, key space, etc.)?

- The minimum password length set by the organization is 6 characters.
- There are no specific requirements for password creation, and users can use any combination of words and letters to create a password.
5. What would you change in the password policy to make breaking the passwords harder?

- Implement a password policy that requires passwords to be random, rather than allowing users to choose their passwords.
- Increase the minimum password length to 8 characters.
- Include special characters, capital and small letters, and numbers in the password creation rules.
- Do not allow users to include their username, actual name, date of birth, or any personal information while creating a password.
- Educate users about password security and the importance of creating strong passwords.

<details>
    <summary><h2> Answer given By them</h2> </summary>
<!-- empty line -->
    As a result of the analysis the following uplifts are proposed to increase the overall level of password protection:

- Use a dedicated password hashing algorithm bcrypt, scrypt or PBKDF2 as this will greatly increase the time needed to crack individual passwords,
- Implement salting to prevent usage of rainbow tables to speed up cracking,
- Increase the minimum password length requirement to 10 characters – this will increase the computational effort required to crack password and will give additional time to change all passwords in the event of the password database being leaked,
- Prevent passwords to be the same as usernames or reused as part of the password – such password combination is easy to check without gaining access to the password database itself.
- It is advised to educate users on creating safe and easy to remember passwords. Having a password policy requiring long passwords with a number of special characters results in user writing passwords down or constantly resetting them. The best way to create a strong and user-friendly password is using passphrases (e.g. mygrannyschairhadstaples). The best way to create such passwords is to combine a couple of completely random word. It’s also advised to use some special characters and numbers as easy to remember substitutions to expand the key space (e.g. mYgranny$cha1rhadstaples)
- Educate users on the benefits of passwords managers. Having a password manager allows having very long and completely random passwords (e.g. M>?{tk6Cfep6BrZ4J)KZWQ8j) without the need to remember/write down. A strong passphrase is still required as a master key for to access the password manager.
</details>
<!-- empty line -->

#### Extracted passwods
To run tests, run the following command

```txt
3f230640b78d7e71ac5514e57935eb69:qazxsw
7c6a180b36896a0a8c02787eeafb0e4c:password1
e10adc3949ba59abbe56e057f20f883e:123456
5f4dcc3b5aa765d61d8327deb882cf99:password
25d55ad283aa400af464c76d713c07ad:12345678
d8578edf8458ce06fbc5bb76a58c5ca4:qwerty
fcea920f7412b5da7be0cf42b8c93759:1234567
25f9e794323b453885f5181f1b624d0b:123456789
96e79218965eb72c92a549dd5a330112:111111
e99a18c428cb38d5f260853678922e03:abc123
f6a0cb102c62879d397b12b62c092c06:bluered
6c569aabbf7775ef8fc570e228c16b98:password!
```

# Steps to extract passwords
1. Download and install hashcat(Binaries)
- https://hashcat.net/hashcat/
2. Move to the extracted folder in CMD
3. Check whether hashcat is working by typing `hashcat -b` It will show the efficiency of your system for different hashing algorithms.
4. Download any wordlist. You can use anything available.
- https://infosecscout.com/hashcat-tutorial-decrypt-md5/
- https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt
5. Download password-dump and wordlist files and move it to same folder(or give file address correctly in command)
6. To remove the salts in the password-dump file, You can use python program given above. (Salt is the extra characters added for better security)
`experthead:e10adc3949ba59abbe56e057f20f883e` Here `experthead` is the salt.

7. Now run the below command. This is called Dictionary Attack
`hashcat -a 0 -m 0 -O hashes.txt wordlist.txt`
- a 0 : to tell hashcat to use a dictionary attack
- m 0 : to tell hashcat to use only the MD5 function
- O : use the optimized version

8. If passwords doesn't show with warning `INFO: Removed 12 hashes found as potfile entries.INFO: Removed 12 hashes found as potfile entries.` use `--potfile-disable` along the the above command.

9. As we get all the passwords for given hashes no need to use advanced methods such as Bruteforce Attack or Mask Attack.



### Resources
- https://infosecscout.com/hashcat-tutorial-decrypt-md5/
- https://www.freecodecamp.org/news/hacking-with-hashcat-a-practical-guide/

## Screenshots

![Password Cracked](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

