## Introduction

This folder consists of the source code for the symmetric-key encryption technique, AES.

This code is written for the 128-bit AES but may be easily scaled to different variants such as 192-bit or 256-bit AES.

## How to use

To successfully encrypt and decrypt the source image and look at the encrypted and decrypted image, use the following line:

```
python3 aes.py
```

## Bibliography

The s_box, inv_s_box and r_con matrices have been copied from the following [link](https://github.com/boppreh/aes/blob/master/aes.py).

### Note:

The modules for mixing columns and inverting it have been copied from the link mentioned above since the lecture notes weren't providing enough information regarding the same.